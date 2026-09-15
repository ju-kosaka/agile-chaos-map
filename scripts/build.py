#!/usr/bin/env python3
"""data/elements/*.json を結合し、also_in と crossing を機械的に計算して
data/elements.json を出力する。手で also_in を書かないための装置。

使い方:
    python3 scripts/build.py          # 検証 + 出力
    python3 scripts/build.py --check  # 検証のみ（出力しない）
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ELEM_DIR = ROOT / "data" / "elements"
OUT = ROOT / "data" / "elements.json"
LAYER_FILES = ["F", "I", "II", "III", "IV", "V"]
LAYERS = ["I", "II", "III", "IV", "V"]


def norm(s):
    """照合用の正規化。全角半角・大小・記号・空白の揺れを潰す。"""
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s)
    s = s.lower()
    # 括弧とその中身を落とす（「ふりかえり（レトロスペクティブ）」→「ふりかえり」）
    s = re.sub(r"[（(\[][^）)\]]*[）)\]]", "", s)
    # 記号・空白をすべて除去
    s = re.sub(r"[\s\-_'’‘\"“”/·・,，.。:：;；&＆]", "", s)
    return s


def load_elements():
    elements = []
    seen_ids = set()
    for layer in LAYER_FILES:
        path = ELEM_DIR / f"{layer}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        for e in data:
            if e["id"] in seen_ids:
                raise SystemExit(f"重複ID: {e['id']}")
            seen_ids.add(e["id"])
            elements.append(e)
    return elements


def build_prior_index(prior):
    """先行マップの収録項目を、正規化名 -> マップID の索引にする。"""
    index = {}
    for m in prior["maps"]:
        mid = m["id"]
        for item in m["items"]:
            names = []
            for key in ("en", "ja"):
                if item.get(key):
                    names.append(item[key])
            names.extend(item.get("aka_en", []))
            names.extend(item.get("aka_ja", []))
            for n in names:
                index.setdefault(norm(n), set()).add(mid)
    return index


def check_docs_numbers(elements):
    """README.md / docs/DESIGN.md に手書きされた数値が、実データと合っているか検査する。

    要素を足すたびにドキュメントの数値が黙って古くなる事故を止めるための装置。
    これらは生成物ではないので build では直さない。ズレを報告するだけにしている。
    """
    import collections

    issues = []
    n = len(elements)
    urls = {s["url"] for e in elements for s in e["sources"]}
    cat = collections.Counter(e["category"] for e in elements)
    cap = collections.Counter()
    for e in elements:
        for c in e.get("capabilities", []):
            cap[c] += 1
    own = sum(1 for e in elements if not e.get("also_in"))
    own_pct = round(100 * own / n) if n else 0

    def expect(path, pattern, actual, label):
        if not path.exists():
            return
        text = path.read_text(encoding="utf-8")
        m = re.search(pattern, text)
        if not m:
            issues.append(f"[{path.name}] {label}: 記述が見つからない（書式が変わった？）")
            return
        got = int(m.group(1))
        if got != actual:
            issues.append(f"[{path.name}] {label}: 記載 {got} ≠ 実データ {actual}")

    readme = ROOT / "README.md"
    design = ROOT / "docs" / "DESIGN.md"

    expect(readme, r"現在 \*\*(\d+)要素", n, "要素数")
    expect(readme, r"出典URL (\d+)件\*\*", len(urls), "出典URL数")
    expect(readme, r"バッジの無い(\d+)件", own, "先行マップに無い件数")
    expect(readme, r"バッジの無い\d+件（(\d+)%）", own_pct, "先行マップに無い割合")

    layer_names = {
        "I": "認知と自己", "II": "人とチーム", "III": "流れとものづくり",
        "IV": "価値と事業", "V": "組織とガバナンス",
    }
    for layer, jp in layer_names.items():
        expect(readme, rf"\| {layer} \| {jp} \|[^|]*\| (\d+) \|", cat[layer], f"{layer}層の件数")
    expect(readme, r"\| 土台 \| 根っこにある考え方 \|[^|]*\| (\d+) \|", cat["F"], "土台の件数")

    for c in ["C1", "C2", "C3", "C4", "C5"]:
        expect(readme, rf"{c} (\d+)", cap[c], f"{c} の件数")

    expect(design, r"\| 本マップの要素 \| (\d+)件 \|", n, "要素数")
    expect(design, r"どちらにも無い（本マップが足した分）\*\* \| \*\*(\d+)件", own, "先行マップに無い件数")
    expect(design, r"どちらにも無い（本マップが足した分）\*\* \| \*\*\d+件（(\d+)%）", own_pct, "先行マップに無い割合")

    return issues


def main():
    check_only = "--check" in sys.argv
    elements = load_elements()
    prior = json.loads((ROOT / "data" / "prior_art.json").read_text(encoding="utf-8"))
    cats = json.loads((ROOT / "data" / "categories.json").read_text(encoding="utf-8"))
    prior_index = build_prior_index(prior)

    valid_subs = {s["id"] for s in cats["foundation"]["subcategories"]}
    for layer in cats["layers"]:
        valid_subs |= {s["id"] for s in layer["subcategories"]}
    valid_caps = {c["id"] for c in cats["capabilities"]}
    valid_flow = {f["id"] for f in cats["flow"]}
    valid_ai = {t["id"] for t in cats["ai_impact_types"]}

    problems = []
    stats = {"also_in": {"agile-alliance-subway": 0, "agile-studio-apm": 0, "none": 0}}

    for e in elements:
        eid = e["id"]

        # --- 必須項目 ---
        for key in ("name", "name_en", "summary", "category", "subcategory",
                    "affinity", "capabilities", "flow", "ai_impact", "sources"):
            if key not in e:
                problems.append(f"[{eid}] 必須キー欠落: {key}")

        # --- 分類の妥当性 ---
        if e.get("subcategory") not in valid_subs:
            problems.append(f"[{eid}] 未定義の中分類: {e.get('subcategory')}")
        if not e.get("subcategory", "").startswith(e.get("category", "") + "-"):
            problems.append(f"[{eid}] 大枠と中分類が不整合: {e.get('category')} / {e.get('subcategory')}")
        for c in e.get("capabilities", []):
            if c not in valid_caps:
                problems.append(f"[{eid}] 未定義のケイパビリティ: {c}")
        if e.get("flow") not in valid_flow:
            problems.append(f"[{eid}] 未定義のフロー段: {e.get('flow')}")
        if e.get("ai_impact", {}).get("type") not in valid_ai:
            problems.append(f"[{eid}] 未定義のAIインパクト類型: {e.get('ai_impact', {}).get('type')}")

        # --- 帰属スコア ---
        aff = e.get("affinity", {})
        if set(aff.keys()) != set(LAYERS):
            problems.append(f"[{eid}] affinity が5層すべてを持っていない: {sorted(aff.keys())}")
        else:
            for layer, v in aff.items():
                if not isinstance(v.get("score"), int) or not (0 <= v["score"] <= 5):
                    problems.append(f"[{eid}] {layer} のスコアが0-5でない: {v.get('score')}")
                if not v.get("why"):
                    problems.append(f"[{eid}] {layer} に根拠文がない")

            ranked = sorted(aff.items(), key=lambda kv: -kv[1]["score"])
            top_layer, top = ranked[0]
            second_layer, second = ranked[1]

            # 配置層が最高点であること（同点は可。土台Fは対象外）
            if e["category"] != "F" and aff[e["category"]]["score"] < top["score"]:
                problems.append(
                    f"[{eid}] 配置層が最高点より低い: category={e['category']}"
                    f"({aff[e['category']]['score']}) < {top_layer}({top['score']})"
                )
            # 越境判定: 配置層以外で、配置層との差が1以内かつ4点以上
            # （4点＝「その大枠の主要な構成要素」。3点だと大半が該当して情報にならない）
            # 土台Fは定義上すべての層にかかるので越境の対象外にする
            base = aff[e["category"]]["score"] if e["category"] in aff else top["score"]
            if e["category"] == "F":
                e["crossing"] = []
                e["crossing_tied"] = []
            else:
                e["crossing"] = [
                    l for l, v in ranked
                    if l != e["category"] and base - v["score"] <= 1 and v["score"] >= 4
                ]
                # 同点の層＝どちらに置いてもおかしくない、本当の越境
                e["crossing_tied"] = [
                    l for l, v in ranked
                    if l != e["category"] and v["score"] == base and v["score"] >= 4
                ]
            e["affinity_top"] = top_layer
            e["affinity_gap"] = top["score"] - second["score"]

        # --- also_in（機械判定・完全一致のみ） ---
        names = [e.get("name"), e.get("name_en")] + e.get("aka", []) + e.get("aka_en", [])
        hits = set()
        for n in names:
            hits |= prior_index.get(norm(n), set())
        e["also_in"] = sorted(hits)
        if hits:
            for h in hits:
                stats["also_in"][h] += 1
        else:
            stats["also_in"]["none"] += 1

        # --- 出典 ---
        if not e.get("sources"):
            problems.append(f"[{eid}] 出典がない")
        for s in e.get("sources", []):
            if not s.get("url", "").startswith("http"):
                problems.append(f"[{eid}] 出典URLが不正: {s.get('url')}")
            if not s.get("note"):
                problems.append(f"[{eid}] 出典に概要（note）がない: {s.get('url')}")
            if s.get("strength") not in (1, 2, 3):
                problems.append(f"[{eid}] 出典強度が1-3でない: {s.get('strength')}")

        # --- 非日本語文字の混入（生成時の事故検出） ---
        blob = json.dumps(e, ensure_ascii=False)
        stray = set(re.findall(r"[가-힣Ѐ-ӿ一-鿿]", blob))
        hangul_cyrillic = {c for c in stray if not ("一" <= c <= "鿿")}
        if hangul_cyrillic:
            problems.append(f"[{eid}] 日本語以外の文字が混入: {sorted(hangul_cyrillic)}")

    # --- 集計 ---
    by_layer = {}
    for e in elements:
        by_layer.setdefault(e["category"], []).append(e)

    print("=" * 62)
    print("要素数:", len(elements))
    for layer in LAYER_FILES:
        items = by_layer.get(layer, [])
        subs = {}
        for e in items:
            subs.setdefault(e["subcategory"], 0)
            subs[e["subcategory"]] += 1
        detail = " ".join(f"{k}:{v}" for k, v in sorted(subs.items()))
        print(f"  {layer:4} {len(items):3}件   {detail}")

    print("-" * 62)
    print("先行マップとの重なり（機械判定・完全一致）")
    total = len(elements)
    aa = stats["also_in"]["agile-alliance-subway"]
    apm = stats["also_in"]["agile-studio-apm"]
    none = stats["also_in"]["none"]
    print(f"  Agile Alliance 収録    : {aa:3}件")
    print(f"  Agile Studio APM 収録  : {apm:3}件")
    print(f"  どちらにも無い（本マップ独自）: {none:3}件 / {total}件 "
          f"({none * 100 // total}%)")
    print("  層別の独自率:")
    for layer in LAYER_FILES:
        items = by_layer.get(layer, [])
        if not items:
            continue
        n = sum(1 for e in items if not e["also_in"])
        print(f"    {layer:4} {n:3}/{len(items):3}件が独自 ({n * 100 // len(items):3}%)")

    # --- 先行マップ側から見た被覆（照合の取りこぼしを可視化する） ---
    print("-" * 62)
    print("先行マップ側から見た被覆（本マップがどう受けているか）")
    mine_idx, folded_idx = {}, {}
    for e in elements:
        for n in [e["name"], e["name_en"]] + e.get("aka", []) + e.get("aka_en", []):
            mine_idx.setdefault(norm(n), []).append(e["id"])
        for n in e.get("includes", []):
            folded_idx.setdefault(norm(n), []).append(e["id"])
    for m in prior["maps"]:
        direct = folded = missing = 0
        missing_names = []
        for it in m["items"]:
            keys = [norm(n) for n in
                    ([it.get("en"), it.get("ja")] + it.get("aka_en", [])) if n]
            if any(k in mine_idx for k in keys):
                direct += 1
            elif any(k in folded_idx for k in keys):
                folded += 1
            else:
                missing += 1
                missing_names.append(it.get("ja") or it.get("en"))
        print(f"  {m['name'][:28]:30} 全{len(m['items']):3}項目  "
              f"同名の要素あり{direct:3}  親要素に畳んだ{folded:3}  採録せず{missing:3}")
        if missing_names:
            print(f"    採録していない項目: {'、'.join(missing_names)}")

    print("-" * 62)
    cross = [e for e in elements if e.get("crossing")]
    tied = [e for e in elements if e.get("crossing_tied")]
    print(f"越境要素（配置層と1点差以内で4点以上の層を持つ）: {len(cross)}件")
    print(f"  うち同点（どちらに置いてもよい真の越境）      : {len(tied)}件")

    ai_types = {}
    for e in elements:
        t = e["ai_impact"]["type"]
        ai_types[t] = ai_types.get(t, 0) + 1
    print("AI時代インパクトの内訳:", ", ".join(f"{k} {v}件" for k, v in sorted(ai_types.items())))

    strengths = {}
    for e in elements:
        for s in e["sources"]:
            strengths[s["strength"]] = strengths.get(s["strength"], 0) + 1
    print("出典強度の内訳:", ", ".join(f"強度{k}: {v}本" for k, v in sorted(strengths.items(), reverse=True)))
    print("出典URL総数:", sum(len(e["sources"]) for e in elements))

    doc_issues = check_docs_numbers(elements)
    if doc_issues:
        problems.extend(doc_issues)

    print("=" * 62)
    if problems:
        print(f"検証で見つかった問題: {len(problems)}件")
        for p in problems:
            print("  -", p)
    else:
        print("検証: 問題なし")

    if not check_only:
        payload = {
            "version": "1.0",
            "updated": "2026-09-15",
            "count": len(elements),
            "elements": elements,
        }
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"出力: {OUT.relative_to(ROOT)}")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
