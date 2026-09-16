#!/usr/bin/env python3
"""出典URLを実際に取得して、**中身が目的の文献かどうか**まで確かめる。

`build.py` は URL が http で始まるかしか見ない。404 でも、まったく別の文献でも通る
（実測: `oreilly.co.jp/books/9784873118161/` は 200 で通るが中身は別の本だった）。
人がレビューしているうちは人が捕まえていたが、自律運転ではここが空く。

**照合は要素名ではなく `sources[].title` で行う。** 要素名で照合すると誤検出する
（Royce 1970 の原論文に "waterfall" という語は1度も出てこない）。
著者が書いたタイトルは「その文献が何か」を述べているので、別文献とすり替わったら一致しなくなる。

判定:
    ok        200 かつ タイトル由来の語が本文に見つかった
    mismatch  200 だが見つからない → **中身が違う可能性。中断させる**
    bot       403 / 202 / 406 / 429 → 実在も架空も同じ応答を返すので自己承認させない。
              強度2以下であることを要求する
    dead      404 / 410 / 接続失敗 → **中断させる**
    unverif   本文からテキストを取り出せない → 強度2以下であることを要求する

使い方:
    python3 scripts/verify_sources.py            # git HEAD から増えた出典だけ
    python3 scripts/verify_sources.py --all      # 全出典（遅い）
    python3 scripts/verify_sources.py --url URL --title TITLE   # 1本だけ試す
"""
import json
import re
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ELEM_DIR = ROOT / "data" / "elements"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

BOT_CODES = {"202", "403", "406", "429", "503"}
DEAD_CODES = {"000", "404", "410"}
# タイトルから拾わない語（どの文献にも出るので弁別にならない）
STOPWORDS = set("""the and for with from into about a an of on in to by at as is are
公式 サイト ページ 記事 解説 入門 まとめ について とは 株式会社 について""".split())


def norm(s):
    return unicodedata.normalize("NFKC", s or "").lower()


def tokens_from_title(title):
    """タイトルから弁別に使える語を切り出す。

    英語は4文字以上の語、日本語は3文字以上の連なり。括弧の中（出版社名など）も使う。
    """
    t = norm(title)
    out = []
    for m in re.findall(r"[a-z0-9][a-z0-9'\-]{3,}", t):
        if m not in STOPWORDS:
            out.append(m)
    for m in re.findall(r"[ぁ-んァ-ヶ一-鿿ー]{3,}", t):
        if m not in STOPWORDS:
            out.append(m)
    # 英語は連語のほうが強い弁別になるので2語・3語の並びも足す
    words = [w for w in re.findall(r"[a-z0-9][a-z0-9'\-]{2,}", t) if w not in STOPWORDS]
    for n in (3, 2):
        for i in range(len(words) - n + 1):
            out.append(" ".join(words[i:i + n]))
    return sorted(set(out), key=len, reverse=True)


def fetch(url, pause=2.0):
    time.sleep(pause)
    hdr = subprocess.run(
        ["curl", "-sSL", "--max-time", "30", "-A", UA, "-o", "/dev/null",
         "-w", "%{http_code}|%{content_type}|%{size_download}", url],
        capture_output=True, text=True).stdout.strip()
    parts = (hdr or "000||0").split("|")
    code = parts[0] or "000"
    ctype = parts[1] if len(parts) > 1 else ""
    if code not in ("200",):
        return code, ctype, ""
    # 本文を取る。PDF は pdftotext を通す
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        tmp = Path(f.name)
    subprocess.run(["curl", "-sSL", "--max-time", "30", "-A", UA, "-o", str(tmp), url],
                   capture_output=True)
    body = ""
    try:
        if "pdf" in ctype.lower():
            r = subprocess.run(["pdftotext", "-f", "1", "-l", "5", str(tmp), "-"],
                               capture_output=True, text=True)
            body = r.stdout
        else:
            raw = tmp.read_bytes().decode("utf-8", errors="replace")
            raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S | re.I)
            body = re.sub(r"<[^>]+>", " ", raw)
    finally:
        tmp.unlink(missing_ok=True)
    return code, ctype, body


def offline_ok(url):
    """ネットワークに依らずに実在を確かめられる場合だけ True。

    Agile Alliance の用語集は bot対策で 202（本文0バイト）を返すので、叩いても
    実在の証拠にならない。ただし公式用語集のスラッグ一覧を ops/prior_art.json に
    記録してあるので、それと突き合わせれば到達性に頼らず確かめられる。
    （原簿はローカル専用。無ければこの照合は行わない）
    """
    import urllib.parse
    if "agilealliance.org/glossary/" not in url:
        return False
    pa = ROOT / "ops" / "prior_art.json"
    if not pa.exists():
        return False
    try:
        prior = json.loads(pa.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    slugs = set()
    for m in prior.get("maps", []):
        for it in m.get("items", []):
            if it.get("slug"):
                slugs.add(it["slug"])
            v = it.get("url") or ""
            if "glossary" in v:
                slugs.add(urllib.parse.urlparse(v).path.strip("/").split("/")[-1])
    slug = urllib.parse.urlparse(url).path.strip("/").split("/")[-1]
    return slug in slugs


def judge(url, title, pause=2.0):
    if offline_ok(url):
        return "ok", "公式用語集の一覧（ops/prior_art.json）と一致。到達性に依らず確認", []
    code, ctype, body = fetch(url, pause)
    if code in DEAD_CODES:
        return "dead", f"HTTP {code}", []
    if code in BOT_CODES:
        return "bot", f"HTTP {code}（bot対策。実在の証拠にならない）", []
    if code != "200":
        return "dead", f"HTTP {code}", []
    text = norm(body)
    squeezed = " ".join(text.split())
    # JSで中身を後から入れるページは、200で返ってくるのに本文が空に近い。
    # これを mismatch（＝中身が違う）と判定すると誤検出になる。実測: APA PsycNET は
    # 本文226文字の "loading..." だけを返す。しきい値は余裕を持って500にしてある。
    # JSシェルの判定は「本文がほぼ空なのに noscript の文言だけある」ときに限る。
    # 実測: thoughtworks.com は本文35,918文字あるのに先頭に "enable javascript" の
    # 案内を置いていて、これだけで unverif に落としていた（誤爆）。
    # 中身のあるページを unverif にすると、正当な強度3の出典が採れなくなる。
    js_shell = (len(squeezed) < 1500 and
                any(k in squeezed[:400] for k in
                    ("loading...", "javascript is required", "enable javascript",
                     "お使いのブラウザ", "please enable")))
    if len(squeezed) < 500 or js_shell:
        why = "JSで本文を読み込むページ" if js_shell else "本文が短すぎる"
        return "unverif", f"{why}（{len(squeezed)}文字・{ctype}）", []
    toks = tokens_from_title(title)
    hits = [t for t in toks if t in text]
    if hits:
        return "ok", f"タイトル由来の語が一致: {hits[:3]}", hits
    return "mismatch", f"タイトル由来の語が本文に1つも無い（試した語 {len(toks)}個）", []


def load_current():
    out = []
    for p in sorted(ELEM_DIR.glob("*.json")):
        for e in json.loads(p.read_text(encoding="utf-8")):
            for s in e.get("sources", []):
                out.append((e["id"], s["url"], s.get("title", ""), s.get("strength")))
    return out


def load_head():
    """git HEAD 時点の出典URL集合。差分だけ検査するために使う。"""
    urls = set()
    for name in ("F", "I", "II", "III", "IV", "V"):
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:data/elements/{name}.json"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            continue
        for e in json.loads(r.stdout):
            for s in e.get("sources", []):
                urls.add(s["url"])
    return urls


def main():
    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]
        title = sys.argv[sys.argv.index("--title") + 1] if "--title" in sys.argv else ""
        verdict, why, _ = judge(url, title, pause=0)
        print(f"{verdict:9} {why}\n          {url}")
        return 0 if verdict in ("ok", "bot", "unverif") else 1

    current = load_current()
    if "--all" in sys.argv:
        targets = current
    else:
        head = load_head()
        targets = [t for t in current if t[1] not in head]

    if not targets:
        print("検査対象の出典なし（HEAD から増えていない）")
        return 0

    print(f"出典を実際に取得して中身を確かめる: {len(targets)}本")
    problems, notes = [], []
    for eid, url, title, strength in targets:
        verdict, why, _ = judge(url, title)
        mark = {"ok": "✓", "bot": "△", "unverif": "△", "mismatch": "✗", "dead": "✗"}[verdict]
        print(f"  {mark} {verdict:9} [{eid}] {why}")
        print(f"              {url}")
        if verdict in ("dead", "mismatch"):
            problems.append(f"[{eid}] {verdict}: {why} / {url}")
        elif verdict in ("bot", "unverif"):
            if strength and strength > 2:
                problems.append(
                    f"[{eid}] {verdict} なのに強度{strength}。"
                    f"自己承認できない出典は強度2以下にする / {url}")
            else:
                notes.append(f"[{eid}] {verdict}（強度{strength}で採録）/ {url}")

    print("-" * 62)
    if notes:
        print(f"確かめきれなかったが強度2以下なので通す: {len(notes)}本")
        for n in notes:
            print("  -", n)
    if problems:
        print(f"★出典の問題: {len(problems)}件")
        for p in problems:
            print("  -", p)
        return 1
    print("出典: 問題なし")
    return 0


if __name__ == "__main__":
    sys.exit(main())
