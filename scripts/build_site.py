#!/usr/bin/env python3
"""elements.json + categories.json から docs/index.html を生成する。

外部ライブラリ・CDNを一切使わない単一HTML。file:// で直接開ける。
（データは fetch できないので JSON をページに埋め込む）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>アジャイル・カオスマップ ― AI時代に効く仕事の部品表</title>
<style>
:root {
  --bg: #f7f7f5;
  --panel: #ffffff;
  --ink: #1a1a1a;
  --ink-soft: #5c5c5c;
  --ink-faint: #8a8a8a;
  --line: #e0e0dc;
  --line-soft: #efefec;
  --accent: #1f6feb;
  --chip-bg: #ffffff;
  --shadow: 0 1px 2px rgba(0,0,0,.06), 0 4px 12px rgba(0,0,0,.04);
  --radius: 10px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #15161a;
    --panel: #1e2027;
    --ink: #e8e8e6;
    --ink-soft: #a8a9ad;
    --ink-faint: #74757a;
    --line: #32343c;
    --line-soft: #26282f;
    --chip-bg: #24262e;
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 4px 14px rgba(0,0,0,.3);
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Hiragino Sans", "Noto Sans JP", "Yu Gothic UI", sans-serif;
  font-size: 15px;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); }

/* ---------- ヘッダー ---------- */
header {
  padding: 28px 24px 0;
  max-width: 1600px;
  margin: 0 auto;
}
h1 {
  font-size: clamp(20px, 3vw, 30px);
  line-height: 1.35;
  margin: 0 0 6px;
  letter-spacing: .01em;
}
.lede {
  color: var(--ink-soft);
  max-width: 70ch;
  margin: 0 0 18px;
  font-size: 14px;
}
.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 18px;
  padding: 12px 16px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  margin-bottom: 18px;
  font-size: 13px;
}
.stat b { font-size: 17px; font-variant-numeric: tabular-nums; }
.stat span { color: var(--ink-soft); }

/* ---------- コントロール ---------- */
.controls {
  position: sticky;
  top: 0;
  z-index: 20;
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--line);
  padding: 10px 0;
  margin-bottom: 18px;
}
.controls-inner {
  max-width: 1600px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px 16px;
  align-items: center;
}
.group { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.group > .label {
  font-size: 11px;
  color: var(--ink-faint);
  letter-spacing: .06em;
  margin-right: 2px;
}
button.seg, button.tog {
  font: inherit;
  font-size: 12.5px;
  padding: 5px 11px;
  border: 1px solid var(--line);
  background: var(--panel);
  color: var(--ink-soft);
  border-radius: 999px;
  cursor: pointer;
  line-height: 1.5;
}
button.seg:hover, button.tog:hover { border-color: var(--ink-faint); }
button.seg[aria-pressed="true"] {
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}
button.tog[aria-pressed="true"] {
  border-color: currentColor;
  font-weight: 600;
}
button.tog[data-dim="true"] { opacity: .4; }
input[type="search"] {
  font: inherit;
  font-size: 13px;
  padding: 5px 11px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel);
  color: var(--ink);
  width: 170px;
}
.count { font-size: 12px; color: var(--ink-faint); font-variant-numeric: tabular-nums; }

/* ---------- マップ本体 ---------- */
main { max-width: 1600px; margin: 0 auto; padding: 0 24px 60px; }
.layer {
  border: 1px solid var(--line);
  border-left: 5px solid var(--layer-color, var(--line));
  border-radius: var(--radius);
  background: var(--panel);
  margin-bottom: 16px;
  overflow: hidden;
}
.layer-head {
  padding: 13px 16px 11px;
  border-bottom: 1px solid var(--line-soft);
  display: flex;
  flex-wrap: wrap;
  gap: 4px 12px;
  align-items: baseline;
}
.layer-no {
  font-size: 12px;
  font-weight: 700;
  color: var(--layer-color);
  letter-spacing: .1em;
}
.layer-name { font-size: 17px; font-weight: 700; margin: 0; }
.layer-tag { font-size: 12.5px; color: var(--ink-soft); }
.layer-n { font-size: 11.5px; color: var(--ink-faint); margin-left: auto; font-variant-numeric: tabular-nums; }
.layer-desc {
  padding: 10px 16px 0;
  font-size: 12.5px;
  color: var(--ink-soft);
  max-width: 80ch;
}
.subs { padding: 12px 16px 16px; display: grid; gap: 14px; }
@media (min-width: 900px)  { .subs { grid-template-columns: repeat(2, minmax(0,1fr)); } }
@media (min-width: 1300px) { .subs { grid-template-columns: repeat(3, minmax(0,1fr)); } }
.sub { min-width: 0; }
.sub-head {
  font-size: 12px;
  font-weight: 700;
  color: var(--ink-soft);
  padding-bottom: 5px;
  margin-bottom: 7px;
  border-bottom: 1px dashed var(--line);
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.sub-note { font-weight: 400; font-size: 11px; color: var(--ink-faint); }
.chips { display: flex; flex-wrap: wrap; gap: 5px; }

.chip {
  font: inherit;
  font-size: 12.5px;
  text-align: left;
  padding: 4px 9px 4px 8px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--chip-bg);
  color: var(--ink);
  cursor: pointer;
  line-height: 1.45;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  max-width: 100%;
}
.chip:hover { border-color: var(--layer-color, var(--accent)); }
.chip[data-hidden="true"] { display: none; }
.chip .dot {
  width: 6px; height: 6px; border-radius: 50%;
  flex: 0 0 auto;
}
.chip .nm { overflow-wrap: anywhere; }
.chip .badge {
  font-size: 9.5px;
  padding: 0 4px;
  border-radius: 4px;
  border: 1px solid var(--line);
  color: var(--ink-faint);
  flex: 0 0 auto;
  line-height: 1.6;
}
.chip .badge.cross { border-color: currentColor; }

/* 土台の帯 */
.foundation {
  border: 1px dashed var(--line);
  border-radius: var(--radius);
  background: var(--panel);
  padding: 13px 16px 16px;
  margin-bottom: 16px;
}
.foundation .layer-head { border: 0; padding: 0 0 6px; }

/* ---------- 詳細パネル ---------- */
.overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,.35);
  z-index: 40;
  display: none;
}
.overlay[data-open="true"] { display: block; }
.detail {
  position: fixed;
  top: 0; right: 0; bottom: 0;
  width: min(520px, 100vw);
  background: var(--panel);
  border-left: 1px solid var(--line);
  z-index: 50;
  overflow-y: auto;
  transform: translateX(100%);
  transition: transform .18s ease;
  box-shadow: var(--shadow);
}
.detail[data-open="true"] { transform: none; }
.detail-inner { padding: 20px 22px 60px; }
.detail h2 { font-size: 20px; margin: 0 0 2px; line-height: 1.4; }
.detail .en { font-size: 12.5px; color: var(--ink-faint); margin: 0 0 12px; }
.detail .sum { font-size: 14px; margin: 0 0 18px; }
.detail h3 {
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--ink-faint);
  margin: 20px 0 8px;
  padding-bottom: 4px;
  border-bottom: 1px solid var(--line-soft);
}
.close {
  position: absolute; top: 12px; right: 14px;
  font: inherit; font-size: 20px; line-height: 1;
  background: none; border: 0; color: var(--ink-faint); cursor: pointer;
  padding: 6px;
}
.where {
  display: inline-block;
  font-size: 12px;
  padding: 2px 9px;
  border-radius: 999px;
  color: #fff;
  margin-bottom: 6px;
}
.score-row {
  display: grid;
  grid-template-columns: max-content 62px 1fr;
  gap: 4px 10px;
  align-items: start;
  padding: 6px 0;
  border-bottom: 1px solid var(--line-soft);
  font-size: 12.5px;
}
.score-row .ly { color: var(--ink-soft); white-space: nowrap; }
.score-row.is-home .ly { font-weight: 700; color: var(--ink); }
.bar { display: flex; gap: 2px; padding-top: 6px; }
.bar i { width: 10px; height: 6px; border-radius: 1px; background: var(--line); }
.bar i.on { background: var(--bar-color, var(--accent)); }
.score-row .wh { color: var(--ink-soft); min-width: 0; overflow-wrap: anywhere; }
.ai-box {
  border: 1px solid var(--line);
  border-left: 3px solid var(--ai-color, var(--line));
  border-radius: 7px;
  padding: 10px 12px;
  font-size: 12.5px;
}
.ai-box .t { font-weight: 700; color: var(--ai-color); }
.src { font-size: 12.5px; margin-bottom: 12px; }
.src .note { color: var(--ink-soft); font-size: 12px; }
.src .meta { color: var(--ink-faint); font-size: 11px; }
.taglist { display: flex; flex-wrap: wrap; gap: 5px; font-size: 11.5px; }
.taglist span {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 1px 8px;
  color: var(--ink-soft);
}
.empty { color: var(--ink-faint); font-size: 13px; padding: 30px 0; text-align: center; }
footer {
  max-width: 1600px; margin: 0 auto; padding: 24px 24px 50px;
  font-size: 12px; color: var(--ink-faint);
  border-top: 1px solid var(--line);
}
footer a { color: var(--ink-soft); }
@media (max-width: 640px) {
  header { padding: 20px 14px 0; }
  main { padding: 0 14px 40px; }
  .controls-inner { padding: 0 14px; }
  input[type="search"] { width: 100%; }
  /* 狭い幅では grid をやめる。max-content 列が理由文に引っ張られて
     はみ出すため、層名＋バーを1行・理由を次行の flex に切り替える */
  .score-row { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 10px; }
  .score-row .ly, .score-row .bar { flex: 0 0 auto; }
  .score-row .wh { flex: 1 1 100%; padding-left: 2px; }
  .controls { position: static; backdrop-filter: none; }
}
</style>
</head>
<body>

<header>
  <h1>アジャイル・カオスマップ</h1>
  <p class="lede">
    「アジャイル」という一語に押し込められてきた要素を、<b>対象の単位</b>（誰の・何の話か）で並べ直した一覧。
    アジャイルという看板を外しても残る、仕事の仕方の部品表として作っています。
    各要素には、5つの大枠すべてに対する<b>帰属スコアと配置の理由</b>、<b>AI時代にどう効くか</b>（増幅／代替／反転増 × 強度0〜5）、そして出典がついています。
  </p>
  <div class="stats" id="stats"></div>
</header>

<div class="controls">
  <div class="controls-inner">
    <div class="group">
      <span class="label">ビュー</span>
      <button class="seg" data-view="layer" aria-pressed="true">レイヤー</button>
      <button class="seg" data-view="cap" aria-pressed="false">AI時代の能力</button>
      <button class="seg" data-view="flow" aria-pressed="false">活動の流れ</button>
    </div>
    <div class="group" id="ai-filters">
      <span class="label">AI時代</span>
    </div>
    <div class="group" id="prior-filters">
      <span class="label">先行マップ</span>
    </div>
    <div class="group">
      <input type="search" id="q" placeholder="名前・人名・出典で絞り込む" aria-label="名前・人名・出典で絞り込む">
      <span class="count" id="count"></span>
    </div>
  </div>
</div>

<main id="map"></main>

<footer>
  <p>
    大枠は「対象の単位」で切っています。先行するプラクティスマップ
    （<a href="https://www.agilealliance.org/agile101/subway-map-to-agile-practices/">Agile Alliance の Subway Map</a>、
    <a href="https://www.agile-studio.jp/agile-practice-map">Agile Studio のアジャイルプラクティスマップ</a>）は
    「出自（どの手法から来たか）」で切っており、軸が異なります。
    重なる要素には <b>収録済み</b> のバッジを付けているので、バッジの無い要素がこのマップの足している部分です。
  </p>
  <p>出典は全要素に付いています。要素をクリックすると根拠とリンクが出ます。一覧は <code>docs/SOURCES.md</code>。</p>
</footer>

<div class="overlay" id="overlay"></div>
<aside class="detail" id="detail" aria-hidden="true">
  <button class="close" id="close" aria-label="閉じる">&times;</button>
  <div class="detail-inner" id="detail-inner"></div>
</aside>

<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const { elements, categories, priorMaps } = DATA;

const LAYERS = {};
categories.layers.forEach(l => LAYERS[l.id] = l);
LAYERS[categories.foundation.id] = Object.assign({}, categories.foundation, { color: '#8a8a8a', no: 0 });
const CAPS = {}; categories.capabilities.forEach(c => CAPS[c.id] = c);
const FLOWS = {}; categories.flow.forEach(f => FLOWS[f.id] = f);
const AICOLOR = {}; categories.ai_impact_types.forEach(t => AICOLOR[t.id] = t.color);
const SUBNOTE = {};
[categories.foundation, ...categories.layers].forEach(l =>
  l.subcategories.forEach(s => SUBNOTE[s.id] = s));

const PRIOR_LABEL = {
  'agile-alliance-subway': 'Agile Alliance',
  'agile-studio-apm': 'Agile Studio'
};

const state = {
  view: 'layer',
  ai: new Set(categories.ai_impact_types.map(t => t.id)),
  minScore: 0,
  prior: new Set(['in', 'out']),
  q: ''
};

/* ---------- 統計 ---------- */
function renderStats() {
  const own = elements.filter(e => e.also_in.length === 0).length;
  const tied = elements.filter(e => e.crossing_tied && e.crossing_tied.length).length;
  const flip5 = elements.filter(e =>
    e.ai_impact.type === '反転増' && e.ai_impact.score === 5).length;
  const srcs = new Set();
  elements.forEach(e => e.sources.forEach(s => srcs.add(s.url)));
  const items = [
    [elements.length, '要素'],
    [`${categories.layers.length}＋1`, '大枠（5層＋土台）'],
    [own, '先行マップに無い要素'],
    [flip5, 'AIで人間側の重要度が最も上がる要素'],
    [tied, '大枠をまたぐ要素'],
    [srcs.size, '出典URL']
  ];
  document.getElementById('stats').innerHTML = items
    .map(([n, t]) => `<div class="stat"><b>${n}</b> <span>${t}</span></div>`).join('');
}

/* ---------- フィルタUI ---------- */
function renderFilters() {
  const aiWrap = document.getElementById('ai-filters');
  categories.ai_impact_types.forEach(t => {
    const b = document.createElement('button');
    b.className = 'tog';
    b.textContent = t.id;
    b.style.color = t.color;
    b.setAttribute('aria-pressed', 'true');
    b.title = t.description;
    b.onclick = () => {
      state.ai.has(t.id) ? state.ai.delete(t.id) : state.ai.add(t.id);
      b.setAttribute('aria-pressed', state.ai.has(t.id));
      b.dataset.dim = !state.ai.has(t.id);
      apply();
    };
    aiWrap.appendChild(b);
  });
  // 強度での絞り込み。反転増は106件あり、そのままでは軸として分離しない
  const sb = document.createElement('button');
  sb.className = 'tog';
  sb.textContent = '強度4以上';
  sb.title = 'AI時代インパクトの強度が4以上の要素だけを表示する';
  sb.setAttribute('aria-pressed', 'false');
  sb.dataset.dim = 'true';
  sb.onclick = () => {
    state.minScore = state.minScore ? 0 : 4;
    sb.setAttribute('aria-pressed', state.minScore > 0);
    sb.dataset.dim = state.minScore === 0;
    apply();
  };
  aiWrap.appendChild(sb);
  const pWrap = document.getElementById('prior-filters');
  [['out', '未収録（本マップ独自）'], ['in', '収録済み']].forEach(([k, label]) => {
    const b = document.createElement('button');
    b.className = 'tog';
    b.textContent = label;
    b.setAttribute('aria-pressed', 'true');
    b.onclick = () => {
      state.prior.has(k) ? state.prior.delete(k) : state.prior.add(k);
      b.setAttribute('aria-pressed', state.prior.has(k));
      b.dataset.dim = !state.prior.has(k);
      apply();
    };
    pWrap.appendChild(b);
  });
  document.querySelectorAll('button.seg').forEach(b => {
    b.onclick = () => {
      state.view = b.dataset.view;
      document.querySelectorAll('button.seg')
        .forEach(x => x.setAttribute('aria-pressed', x === b));
      render();
    };
  });
  document.getElementById('q').oninput = ev => {
    state.q = ev.target.value.trim().toLowerCase();
    apply();
  };
}

/* ---------- チップ ---------- */
function chip(e) {
  const b = document.createElement('button');
  b.className = 'chip';
  b.dataset.id = e.id;
  const color = (LAYERS[e.category] || {}).color || '#888';
  b.style.setProperty('--layer-color', color);

  const dot = document.createElement('span');
  dot.className = 'dot';
  dot.style.background = AICOLOR[e.ai_impact.type];
  dot.title = 'AI時代: ' + e.ai_impact.type;
  b.appendChild(dot);

  const nm = document.createElement('span');
  nm.className = 'nm';
  nm.textContent = e.name;
  b.appendChild(nm);

  if (e.crossing_tied && e.crossing_tied.length) {
    const g = document.createElement('span');
    g.className = 'badge cross';
    g.style.color = (LAYERS[e.crossing_tied[0]] || {}).color;
    g.textContent = '↔' + (LAYERS[e.crossing_tied[0]] || {}).id;
    g.title = '越境: ' + e.crossing_tied
      .map(l => LAYERS[l].name).join('・') + ' の話でもある';
    b.appendChild(g);
  }
  if (e.also_in.length) {
    const g = document.createElement('span');
    g.className = 'badge';
    g.textContent = '収録済';
    g.title = e.also_in.map(k => PRIOR_LABEL[k]).join(' / ') + ' に収録';
    b.appendChild(g);
  }
  b.onclick = () => openDetail(e);
  return b;
}

/* ---------- 描画 ---------- */
function groupBox(id, title, tagline, desc, color, no) {
  const sec = document.createElement('section');
  sec.className = 'layer';
  sec.style.setProperty('--layer-color', color);
  sec.innerHTML = `
    <div class="layer-head">
      <span class="layer-no">${no}</span>
      <h2 class="layer-name">${title}</h2>
      <span class="layer-tag">${tagline || ''}</span>
      <span class="layer-n" data-n></span>
    </div>
    ${desc ? `<p class="layer-desc">${desc}</p>` : ''}
    <div class="subs"></div>`;
  return sec;
}

function render() {
  const map = document.getElementById('map');
  map.innerHTML = '';

  if (state.view === 'layer') {
    categories.layers.slice().reverse().forEach(l => {
      const sec = groupBox(l.id, l.name, l.tagline, l.description, l.color,
                           `${l.id}. 第${l.no}層`);
      fillSubs(sec.querySelector('.subs'), l.subcategories,
               elements.filter(e => e.category === l.id));
      map.appendChild(sec);
    });
    // 土台の帯は最後（5層すべての下敷きであることを位置で示す）
    const f = categories.foundation;
    const fb = document.createElement('section');
    fb.className = 'foundation';
    fb.style.setProperty('--layer-color', '#8a8a8a');
    fb.innerHTML = `<div class="layer-head">
        <span class="layer-no">土台</span>
        <h2 class="layer-name">${f.name}</h2>
        <span class="layer-tag">${f.tagline}</span>
        <span class="layer-n" data-n></span>
      </div>
      <p class="layer-desc" style="padding-left:0">${f.description}</p>
      <div class="subs"></div>`;
    fillSubs(fb.querySelector('.subs'), f.subcategories,
             elements.filter(e => e.category === 'F'));
    map.appendChild(fb);

  } else if (state.view === 'cap') {
    categories.capabilities.forEach(c => {
      const sec = groupBox(c.id, c.name, '', c.description, c.color, c.id);
      const mine = elements.filter(e => e.capabilities.includes(c.id));
      const subs = [...new Set(mine.map(e => e.category))]
        .sort((a, b) => (LAYERS[a].no || 0) - (LAYERS[b].no || 0))
        .map(k => ({ id: k, name: LAYERS[k].name, note: 'この層から' }));
      fillSubs(sec.querySelector('.subs'), subs, mine, e => e.category);
      map.appendChild(sec);
    });

  } else {
    categories.flow.forEach(f => {
      const sec = groupBox(f.id, f.name, '', f.description, '#5c5c5c', f.id);
      const mine = elements.filter(e => e.flow === f.id);
      const subs = [...new Set(mine.map(e => e.category))]
        .sort((a, b) => (LAYERS[a].no || 0) - (LAYERS[b].no || 0))
        .map(k => ({ id: k, name: LAYERS[k].name, note: 'この層から' }));
      fillSubs(sec.querySelector('.subs'), mine.length ? subs : [], mine, e => e.category);
      map.appendChild(sec);
    });
  }
  apply();
}

function fillSubs(host, subs, items, keyFn) {
  const key = keyFn || (e => e.subcategory);
  subs.forEach(s => {
    const mine = items.filter(e => key(e) === s.id);
    if (!mine.length) return;
    const d = document.createElement('div');
    d.className = 'sub';
    const note = (SUBNOTE[s.id] && SUBNOTE[s.id].note) || s.note || '';
    d.innerHTML = `<div class="sub-head"><span>${s.name}</span>
      <span class="sub-note">${note}</span></div>`;
    const c = document.createElement('div');
    c.className = 'chips';
    mine.forEach(e => c.appendChild(chip(e)));
    d.appendChild(c);
    host.appendChild(d);
  });
}

/* ---------- フィルタ適用 ---------- */
function visible(e) {
  if (!state.ai.has(e.ai_impact.type)) return false;
  if (e.ai_impact.score < state.minScore) return false;
  const inPrior = e.also_in.length > 0;
  if (inPrior && !state.prior.has('in')) return false;
  if (!inPrior && !state.prior.has('out')) return false;
  if (state.q) {
    const hay = [e.name, e.name_en, ...(e.aka || []), ...(e.aka_en || []), e.summary,
                 ...(e.includes || []),
                 ...(e.sources || []).map(s => (s.title || '') + ' ' + (s.note || ''))]
      .join(' ').toLowerCase();
    if (!hay.includes(state.q)) return false;
  }
  return true;
}

function apply() {
  const shown = new Set(elements.filter(visible).map(e => e.id));
  document.querySelectorAll('.chip').forEach(c => {
    c.dataset.hidden = !shown.has(c.dataset.id);
  });
  // 空になったグループを畳む
  document.querySelectorAll('.sub').forEach(s => {
    const any = [...s.querySelectorAll('.chip')].some(c => c.dataset.hidden !== 'true');
    s.style.display = any ? '' : 'none';
  });
  document.querySelectorAll('.layer, .foundation').forEach(sec => {
    const n = [...sec.querySelectorAll('.chip')].filter(c => c.dataset.hidden !== 'true').length;
    sec.style.display = n ? '' : 'none';
    const t = sec.querySelector('[data-n]');
    if (t) t.textContent = n + '件';
  });
  document.getElementById('count').textContent = `${shown.size} / ${elements.length} 件`;
  const main = document.getElementById('map');
  let empty = main.querySelector('.empty');
  if (!shown.size) {
    if (!empty) {
      empty = document.createElement('p');
      empty.className = 'empty';
      empty.textContent = '条件に合う要素がありません。絞り込みを緩めてください。';
      main.appendChild(empty);
    }
  } else if (empty) { empty.remove(); }
}

/* ---------- 詳細 ---------- */
function openDetail(e) {
  const box = document.getElementById('detail-inner');
  const color = (LAYERS[e.category] || {}).color || '#888';
  const home = LAYERS[e.category];
  const sub = SUBNOTE[e.subcategory] || {};

  const rows = ['I', 'II', 'III', 'IV', 'V'].map(l => {
    const a = e.affinity[l];
    const bars = Array.from({ length: 5 }, (_, i) =>
      `<i class="${i < a.score ? 'on' : ''}"></i>`).join('');
    return `<div class="score-row ${l === e.category ? 'is-home' : ''}">
      <span class="ly">${l}. ${LAYERS[l].name}</span>
      <span class="bar" style="--bar-color:${LAYERS[l].color}">${bars}</span>
      <span class="wh">${a.why}</span>
    </div>`;
  }).join('');

  const srcs = e.sources.map(s => `<div class="src">
      <a href="${s.url}" target="_blank" rel="noopener">${s.title}</a>
      <div class="note">${s.note}</div>
      <div class="meta">出典強度 ${s.strength}／3 ・ ${s.url}</div>
    </div>`).join('');

  const caps = e.capabilities.map(c =>
    `<span style="color:${CAPS[c].color}">${CAPS[c].name}</span>`).join('');

  const priorLine = e.also_in.length
    ? e.also_in.map(k => PRIOR_LABEL[k]).join(' / ') + ' に同名の項目あり'
    : '先行マップ2つ（Agile Alliance / Agile Studio）には無い要素';

  box.innerHTML = `
    <span class="where" style="background:${color}">${e.category}. ${home.name} ／ ${sub.name || e.subcategory}</span>
    <h2>${e.name}</h2>
    <p class="en">${e.name_en}${(e.aka || []).length ? ' ／ ' + e.aka.join('、') : ''}</p>
    <p class="sum">${e.summary}</p>

    <h3>AI時代にどう効くか</h3>
    <div class="ai-box" style="--ai-color:${AICOLOR[e.ai_impact.type]}">
      <span class="t">${e.ai_impact.type}</span>
      <span style="color:var(--ink-faint)">（強度 ${e.ai_impact.score}／5）</span>
      <div>${e.ai_impact.why}</div>
    </div>

    <h3>なぜこの大枠に入れたか（5つの大枠すべてへの帰属スコア）</h3>
    ${rows}
    ${(e.crossing_tied && e.crossing_tied.length)
      ? `<p style="font-size:12px;color:var(--ink-soft);margin-top:8px">
          <b>越境</b>: ${e.crossing_tied.map(l => LAYERS[l].name).join('・')} と同点。
          どちらに置いてもおかしくない要素です。</p>` : ''}

    <h3>タグ</h3>
    <div class="taglist">${caps}
      <span>流れ: ${(FLOWS[e.flow] || {}).name || e.flow}</span></div>

    ${(e.includes || []).length ? `<h3>この要素に含めたもの</h3>
      <div class="taglist">${e.includes.map(i => `<span>${i}</span>`).join('')}</div>` : ''}

    <h3>先行マップとの関係</h3>
    <p style="font-size:12.5px;color:var(--ink-soft);margin:0">${priorLine}</p>

    <h3>出典</h3>
    ${srcs}
  `;
  document.getElementById('detail').dataset.open = 'true';
  document.getElementById('detail').setAttribute('aria-hidden', 'false');
  document.getElementById('overlay').dataset.open = 'true';
  document.getElementById('detail').scrollTop = 0;
}

function closeDetail() {
  document.getElementById('detail').dataset.open = 'false';
  document.getElementById('detail').setAttribute('aria-hidden', 'true');
  document.getElementById('overlay').dataset.open = 'false';
}
document.getElementById('close').onclick = closeDetail;
document.getElementById('overlay').onclick = closeDetail;
document.addEventListener('keydown', ev => { if (ev.key === 'Escape') closeDetail(); });

renderStats();
renderFilters();
render();
</script>
</body>
</html>
"""


def main():
    elements = json.loads((ROOT / "data" / "elements.json").read_text(encoding="utf-8"))
    cats = json.loads((ROOT / "data" / "categories.json").read_text(encoding="utf-8"))
    prior = json.loads((ROOT / "data" / "prior_art.json").read_text(encoding="utf-8"))

    payload = {
        "elements": elements["elements"],
        "categories": cats,
        "priorMaps": [{"id": m["id"], "name": m["name"], "url": m["url"]}
                      for m in prior["maps"]],
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    # <script> の中に埋めるので、終了タグとして解釈されうる文字列を無害化する
    blob = blob.replace("</", "<\\/")

    html = HTML.replace("__DATA__", blob)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print(f"生成: {OUT.relative_to(ROOT)}  ({kb:.0f} KB, 要素 {len(payload['elements'])}件)")


if __name__ == "__main__":
    main()
