# アジャイル・カオスマップ

「アジャイル」という一語に押し込められてきた要素を分解し、**対象の単位**（誰の・何の話か）で
並べ直した一覧。アジャイルという看板を外しても残る、**仕事の仕方の部品表**として作っています。

現在 **177要素 / 5層＋土台 / 出典URL 167件**。

## まず見る

```bash
open docs/index.html
```

外部ライブラリ・CDNを一切使わない単一HTMLです。`file://` で直接開けます（ローカルサーバ不要）。

- **ビュー切替** — レイヤー（既定）／ AI時代の能力 ／ 活動の流れ の3つで同じデータを並べ替えられる
- **要素をクリック** — 5つの大枠すべてへの帰属スコアと配置理由、AI時代のインパクト、出典が出る
- **フィルタ** — AI時代の3類型、先行マップ収録の有無、名前での絞り込み

## 大枠

| | 大枠 | 対象の単位 | 件数 |
|---|---|---|---|
| I | 認知と自己 | ひとりの頭の中 | 24 |
| II | 人とチーム | 小集団 | 33 |
| III | 流れとものづくり | 作業と成果物 | 47 |
| IV | 価値と事業 | 顧客と事業 | 36 |
| V | 組織とガバナンス | 組織 | 30 |
| 土台 | 根っこにある考え方 | 5層すべての下敷き | 7 |

分類の物差しは「**対象の単位**」ひとつです。先行するプラクティスマップ
（[Agile Alliance の Subway Map](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/)、
[Agile Studio のアジャイルプラクティスマップ](https://www.agile-studio.jp/agile-practice-map)）は
「**出自**（どの手法から来たか）」で切っており、軸が異なります。

先行マップ2つの収録項目は全件取得して照合してあり、重なる要素には「収録済」バッジが付きます。
**バッジの無い129件がこのマップの足している部分**です（機械判定・完全一致）。

## ファイル構成

```
agile-chaos-map/
├── data/
│   ├── elements/            ← ★編集するのはここ。層ごとの要素定義
│   │   ├── F.json  I.json  II.json  III.json  IV.json  V.json
│   ├── categories.json      ← 大枠・中分類・ケイパビリティ・フローの定義
│   ├── prior_art.json       ← 先行マップの収録項目（also_in 判定の原簿）
│   ├── research_refs.json   ← 設計に使った参照
│   └── elements.json        ← 生成物。編集しない
├── docs/                    ← GitHub Pages の配信元（Settings → Pages: main / docs）
│   ├── index.html           ← 生成物。編集しない
│   ├── DESIGN.md            ← 設計・方向性3案・スコアのルーブリック・決定ログ
│   ├── SOURCES.md           ← 生成物。編集しない
│   └── .nojekyll            ← Jekyll を通さず素通しで配信するための空ファイル
└── scripts/
    ├── build.py             ← 結合＋検証＋also_in/crossing の計算
    ├── build_sources.py     ← SOURCES.md の生成
    ├── build_site.py        ← docs/index.html の生成
    └── check_urls.py        ← 全出典URLの到達性チェック
```

**生成物は手で編集しない**でください（二重管理でズレます）。

## 要素を直す・足す

1. `data/elements/<層>.json` を編集する
2. 検証とビルドを回す

```bash
python3 scripts/build.py          # 検証 + data/elements.json 生成
python3 scripts/build_sources.py  # docs/SOURCES.md 生成
python3 scripts/build_site.py     # docs/index.html 生成
```

`build.py` は次を機械的に検査します。**警告が出たら直してから次へ進んでください。**

- 必須キーの欠落、未定義の分類ID、IDの重複
- 帰属スコアが5層すべて揃っているか、0〜5の範囲か、根拠文があるか
- **配置した大枠が最高点になっているか**（同点は可。低い場合は配置かスコアが誤り）
- 出典のURL形式・概要（note）・強度（1〜3）
- 日本語以外の文字（ハングル・キリル）の混入

`also_in`（先行マップ収録）と `crossing`（越境）は**計算値**です。手で書かないでください。

### 要素の書き方

```json
{
  "id": "kebab-case-id",
  "name": "日本語名", "name_en": "English Name",
  "aka": ["別名"], "aka_en": ["Alias"],
  "summary": "40字前後の一言概要。",
  "category": "II", "subcategory": "II-1",
  "affinity": {
    "I":  {"score": 3, "why": "なぜその点なのか（1行）"},
    "II": {"score": 5, "why": "..."},
    "III":{"score": 1, "why": "..."},
    "IV": {"score": 0, "why": "..."},
    "V":  {"score": 4, "why": "..."}
  },
  "capabilities": ["C5", "C4"],
  "flow": "B5",
  "ai_impact": {"type": "反転増", "score": 4, "why": "..."},
  "includes": ["この要素に畳んだ下位項目"],
  "sources": [{"url": "https://...", "title": "...", "note": "一言概要", "strength": 3}]
}
```

### 採録の基準（4つすべて満たす）

1. **固有名がある** — 実務者が名前で呼んでいる
2. **出典がある** — URLで示せる出所がある
3. **一言で説明できる** — 40字前後で書ける
4. **粒度が合っている** — 判定は「**その手法をやめても残るか**」。
   残るなら独立要素、残らないなら親要素の `includes` に畳む

詳しい設計思想・方向性3案の比較・スコアのルーブリックは [docs/DESIGN.md](docs/DESIGN.md) にあります。

## 出典URLの検証

```bash
python3 scripts/check_urls.py
```

全出典URL＋先行マップのURLを1件ずつ叩き、ステータスと本文サイズを記録します。

**注意**: `agilealliance.org` / `scaledagile.com` / `thesystemsthinker.com` などは
連続アクセスに対して 403 / 202 / 406 を返します。これは **bot対策であって URL の無効ではありません**。
実際、単発・間隔をあけたアクセスでは 200 と実体（例: Agile Alliance の用語集ページは約56万バイト）が返ります。
スクリプトはドメイン単位で直列化して間隔を空けていますが、それでも弾かれることがあります。
**403が出たら「URLが死んでいる」と結論せず、逐次アクセスで確かめてください。**
UA偽装などでの回避はしません（規約はサイト提供者のものです）。

Agile Alliance の用語集URLについては、ネットワークに依存しない照合ができます
（`data/prior_art.json` に記録した公式用語集78語のスラッグと突き合わせる）。

### 最新の検証結果（2026-09-15・`scripts/.url_check.tsv`）

| ステータス | 件数 | 判断 |
|---|---|---|
| 200 | 111 | 到達 |
| 202 | 53 | bot対策（`agilealliance.org` 49・`scrum.org` 4）。単発アクセスでは200と実体が返ることを確認済み |
| 403 | 5 | 同上（`odnetwork.org` / `queue.acm.org` / `positiveorgs` / `coachingfederation.org` / `about.gitlab.com`） |
| **404・接続不可** | **0** | — |

検査対象 169URL。初回の検証で 404 が12件・接続不可が2件見つかり、**全14本を差し替え済み**です
（うちDORAの2件は先方の改名によるもの: Westrum organizational culture → `generative-organizational-culture`、
shifting left on security → `pervasive-security`）。

## 見た目の検証

HTMLを変更したら、**実際に開いて複数の画面幅で目視してから**完了としてください。

```bash
# Playwright で 1440 / 900 / 390px のスクショとコンソールエラーを確認
python3 -m playwright install chromium   # 初回のみ
python3 <スクショスクリプト>
```

確認済みの項目（2026-09-15 時点）:

- 1440 / 900 / 390px のいずれも横スクロールなし
- コンソールエラー・警告なし
- 詳細パネル内も横スクロールなし（狭い幅では層名＋バーを1行、理由を次行に折り返す）
- ライト／ダーク両方で描画確認

## この先の候補（次フェーズ）

- 要素ごとの詳細ページと、関連要素どうしのリンク
- 出典強度1の要素（現在1件）の一次ソース探し直し
- ケイパビリティのタグ付けのさらなる精査（C1 53件 / C2 66 / C3 65 / C4 60 / C5 26。C5だけ薄い）
- 学習導線（どの順で身につけるか）の追加
