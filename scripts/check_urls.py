#!/usr/bin/env python3
"""elements.json に載っている全出典URLを叩いて到達性を確かめる。

サンプリングせず全件見る。件数を必ず表示し、0件の「異常なし」を偽の合格にしない。
200 が返っても中身が空のSPAがあるため、本文の長さも併せて記録する。

使い方: python3 scripts/check_urls.py [--out path.tsv]
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def collect_urls():
    urls = {}
    d = json.loads((ROOT / "data" / "elements.json").read_text(encoding="utf-8"))
    for e in d["elements"]:
        for s in e["sources"]:
            urls.setdefault(s["url"], []).append(e["id"])
    # 先行マップのURLは内部の照合用なので、ここでは叩かない（ops/prior_art.json にある）
    return urls


def check(url):
    try:
        r = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "30", "-A", UA,
             "-w", "\\n@@@%{http_code}\\t%{size_download}", url],
            capture_output=True, timeout=60,
        )
        out = r.stdout.decode("utf-8", errors="replace")
        marker = out.rfind("@@@")
        if marker < 0:
            return url, "ERR", 0
        code, size = out[marker + 3:].strip().split("\t")
        return url, code, int(size)
    except Exception as exc:  # noqa: BLE001
        return url, f"ERR:{type(exc).__name__}", 0


def main():
    out_path = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else \
        ROOT / "scripts" / ".url_check.tsv"
    urls = collect_urls()
    print(f"検査対象URL（重複除去後）: {len(urls)}件")
    if not urls:
        print("エラー: 対象URLが0件。抽出に失敗している", file=sys.stderr)
        return 1

    # 同一ドメインに並列で叩くとレート制限で403が返り、無効なURLと誤診する。
    # ドメインごとに直列化し、間隔を空ける。ドメイン間だけ並列にする。
    from collections import defaultdict
    from urllib.parse import urlparse
    import time

    buckets = defaultdict(list)
    for u in urls:
        buckets[urlparse(u).netloc].append(u)
    print(f"ドメイン数: {len(buckets)}（最大 {max(len(v) for v in buckets.values())}件/ドメイン）")

    done = [0]

    def run_bucket(items):
        out = []
        for j, u in enumerate(items):
            out.append(check(u))
            done[0] += 1
            if done[0] % 25 == 0:
                print(f"  ... {done[0]}/{len(urls)}")
            if j < len(items) - 1:
                time.sleep(1.5)
        return out

    results = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        for chunk in pool.map(run_bucket, buckets.values()):
            results.extend(chunk)

    lines = ["\t".join((code, str(size), url, ",".join(urls[url])))
             for url, code, size in sorted(results, key=lambda r: (r[1], r[0]))]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    counts = {}
    for _, code, _ in results:
        counts[code] = counts.get(code, 0) + 1
    print("\n=== ステータス別の件数 ===")
    for code, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {code}: {n}件")

    bad = [(u, c, s) for u, c, s in results if c != "200"]
    print(f"\n=== 200以外（差し替え対象）: {len(bad)}件 ===")
    for u, c, s in sorted(bad, key=lambda r: r[0]):
        print(f"  {c}  {u}")
        for eid in urls[u]:
            print(f"        └ 使用箇所: {eid}")

    thin = [(u, c, s) for u, c, s in results if c == "200" and s < 2000]
    print(f"\n=== 200だが本文が極端に短い（中身が無い疑い）: {len(thin)}件 ===")
    for u, c, s in sorted(thin, key=lambda r: r[2]):
        print(f"  {s}バイト  {u}")

    print(f"\n結果: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
