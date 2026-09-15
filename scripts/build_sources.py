#!/usr/bin/env python3
"""elements.json と research_refs.json から docs/SOURCES.md を生成する。

SOURCES.md は生成物。手で書かない（二重管理でズレるため）。
2部構成:
  第1部 要素の出典   … 各要素が根拠にしたURL
  第2部 設計に使った参照 … 大枠の設計そのものに使ったURL
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "SOURCES.md"

STRENGTH_LABEL = {
    3: "一次",
    2: "準一次",
    1: "解説のみ",
}


def main():
    data = json.loads((ROOT / "data" / "elements.json").read_text(encoding="utf-8"))
    cats = json.loads((ROOT / "data" / "categories.json").read_text(encoding="utf-8"))
    refs = json.loads((ROOT / "data" / "research_refs.json").read_text(encoding="utf-8"))
    elements = data["elements"]

    layer_name = {cats["foundation"]["id"]: cats["foundation"]["name"]}
    for l in cats["layers"]:
        layer_name[l["id"]] = l["name"]

    # URL単位に集約（同じURLを複数要素が使っている場合をまとめる）
    by_url = {}
    for e in elements:
        for s in e["sources"]:
            rec = by_url.setdefault(s["url"], {
                "title": s["title"], "note": s["note"],
                "strength": s["strength"], "used_by": []
            })
            rec["used_by"].append(e)
            # 同一URLで強度が違う場合は高いほうを採る
            rec["strength"] = max(rec["strength"], s["strength"])

    lines = []
    w = lines.append
    w("# 出典一覧")
    w("")
    w(f"生成物です。`scripts/build_sources.py` が `data/elements.json` と "
      f"`data/research_refs.json` から生成します。**手で編集しないでください。**")
    w("")
    w(f"- 要素数: **{len(elements)}件**")
    w(f"- 要素の出典として参照しているURL: **{len(by_url)}件**（延べ "
      f"{sum(len(e['sources']) for e in elements)}本）")
    n_research = sum(len(g["refs"]) for g in refs["groups"])
    w(f"- 設計に使った参照URL: **{n_research}件**")
    w("")
    w("## 出典強度の見方")
    w("")
    w("| 強度 | 意味 | 本数 |")
    w("|---|---|---|")
    counts = defaultdict(int)
    for rec in by_url.values():
        counts[rec["strength"]] += 1
    for s in (3, 2, 1):
        meaning = {
            3: "一次ソース（原論文・原典・策定団体の公式ページ）",
            2: "権威ある二次ソース（策定者本人の記事、標準団体・研究機関の解説）",
            1: "一般の解説記事のみ。次フェーズで一次ソースを探し直す対象",
        }[s]
        w(f"| {s}（{STRENGTH_LABEL[s]}） | {meaning} | {counts[s]}件 |")
    w("")
    weak = [(u, r) for u, r in by_url.items() if r["strength"] == 1]
    if weak:
        w("**強度1のまま残っているもの（要再調査）**")
        w("")
        for u, r in sorted(weak):
            ids = "、".join(e["name"] for e in r["used_by"])
            w(f"- [{r['title']}]({u}) — 使用箇所: {ids}")
        w("")
    w("---")
    w("")
    w("## 第1部 要素の出典")
    w("")
    w("大枠ごとに、その層の要素が根拠にしているURLを並べます。")
    w("同じURLを複数の要素が使っている場合は1件にまとめ、使用箇所を列挙しています。")
    w("")

    order = ["F", "I", "II", "III", "IV", "V"]
    printed = set()
    for layer in order:
        items = [e for e in elements if e["category"] == layer]
        if not items:
            continue
        w(f"### {layer}. {layer_name[layer]}（{len(items)}要素）")
        w("")
        w("| 要素 | 出典 | 強度 | 概要 |")
        w("|---|---|---|---|")
        for e in items:
            for i, s in enumerate(e["sources"]):
                name = e["name"] if i == 0 else "〃"
                mark = "" if s["url"] not in printed else "（再掲）"
                printed.add(s["url"])
                note = s["note"].replace("|", "｜")
                title = s["title"].replace("|", "｜")
                w(f"| {name} | [{title}]({s['url']}){mark} | {s['strength']} | {note} |")
        w("")

    w("---")
    w("")
    w("## 第2部 設計に使った参照")
    w("")
    w("要素の出典ではなく、**大枠をどう切るかを決めるために読んだもの**です。")
    w("")
    for g in refs["groups"]:
        w(f"### {g['name']}")
        w("")
        for r in g["refs"]:
            w(f"- **[{r['title']}]({r['url']})**")
            w(f"  - {r['note']}")
            w(f"  - {r['access']}")
        w("")

    w("---")
    w("")
    w("## 到達性の確認について")
    w("")
    w(refs["access_note"])
    w("")
    w("確認は `python3 scripts/check_urls.py` で全件まとめて実行できます"
      "（同一ドメインへの連続アクセスでレート制限に当たらないよう、ドメイン単位で直列化しています）。")
    w("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"生成: {OUT.relative_to(ROOT)}")
    print(f"  要素 {len(elements)}件 / 出典URL {len(by_url)}件 / 設計参照 {n_research}件")
    print(f"  強度3: {counts[3]}件, 強度2: {counts[2]}件, 強度1: {counts[1]}件")


if __name__ == "__main__":
    main()
