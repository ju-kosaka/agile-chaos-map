# 出典一覧

生成物です。`scripts/build_sources.py` が `data/elements.json` と `data/research_refs.json` から生成します。**手で編集しないでください。**

- 要素数: **201件**
- 要素の出典として参照しているURL: **197件**（延べ 255本）
- 設計に使った参照URL: **17件**

## 出典強度の見方

| 強度 | 意味 | 本数 |
|---|---|---|
| 3（一次） | 一次ソース（原論文・原典・策定団体の公式ページ） | 160件 |
| 2（準一次） | 権威ある二次ソース（策定者本人の記事、標準団体・研究機関の解説） | 36件 |
| 1（解説のみ） | 一般の解説記事のみ。次フェーズで一次ソースを探し直す対象 | 1件 |

**強度1のまま残っているもの（要再調査）**

- [Lewin's Change Management Model](https://www.mindtools.com/ajm9l1e/lewins-change-management-model) — 使用箇所: レヴィンの3段階モデル

---

## 第1部 要素の出典

大枠ごとに、その層の要素が根拠にしているURLを並べます。
同じURLを複数の要素が使っている場合は1件にまとめ、使用箇所を列挙しています。

### F. 根っこにある考え方（7要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| アジャイルソフトウェア開発宣言 | [アジャイルソフトウェア開発宣言（日本語公式）](https://agilemanifesto.org/iso/ja/manifesto.html) | 3 | 2001年に17名が署名した4つの価値の原文。左記の価値のほうをより重んじると明記されている |
| アジャイル宣言の背後にある原則 | [アジャイル宣言の背後にある原則（日本語公式）](https://agilemanifesto.org/iso/ja/principles.html) | 3 | 宣言を具体化する12の原則の原文 |
| スクラムの価値基準 | [The Scrum Guide](https://scrumguides.org/scrum-guide.html) | 3 | 5つの価値基準をスクラムの成功条件として明記している公式定義 |
| 経験主義 | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | スクラムは経験主義とリーン思考に立脚し、透明性・検査・適応の3本柱を持つと規定 |
| システム思考 | [The Systems Thinker](https://thesystemsthinker.com/) | 2 | システム思考の実務的な論考を蓄積している媒体。因果ループとレバレッジポイントの解説を含む |
| 〃 | [Gerald M. Weinberg（本人サイト）](https://geraldmweinberg.com/Site/Home.html) | 3 | 『Quality Software Management: Systems Thinking』でシステム思考をソフトウェア開発に持ち込み、因果の連鎖を図示する「効果の図」を示した著者の公式サイト |
| 複雑適応系 | [About the Cynefin Framework（The Cynefin Company）](https://thecynefin.co/about-us/about-cynefin-framework/) | 3 | 複雑な領域では原因と結果が事後にしか分からず、探索・感知・対応の順で動くべきという整理 |
| フィードバックループ | [The DevOps Handbook（IT Revolution）](https://itrevolution.com/product/the-devops-handbook-second-edition/) | 2 | フロー・フィードバック・継続的学習という三つの道のうち、第二の道としてフィードバックを位置づける |
| 〃 | [アジャイル宣言の背後にある原則](https://agilemanifesto.org/iso/ja/principles.html)（再掲） | 3 | 動くソフトウェアを短い間隔で提供し、定期的に振り返るという原則がループの短縮を求めている |

### I. 認知と自己（27要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| コンテキストスイッチ | [Multitasking: Switching costs（American Psychological Association）](https://www.apa.org/topics/research/multitasking) | 2 | Rubinstein・Meyer・Evans の実験を引いて、切替には「目標の切替」と「ルールの再活性化」の2段階があり時間を失うと説明する心理学会の解説 |
| 〃 | [The Financial Cost of Task Switching（Scrum.org）](https://www.scrum.org/resources/blog/financial-cost-task-switching) | 2 | Weinberg の見積り（2案件並行で各40%、20%が切替で消える）を金額換算した記事。工学的な経験則であり実験結果ではない点も明記されている |
| シングルタスク（WIP=1） | [Kanban（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/kanban/) | 3 | 仕掛り作業（WIP）を制限して流れを作るカンバンの定義。WIP=1はこの制限を最小にした形 |
| フロー状態 | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco) | 3 | 『ピープルウエア』でフロー状態に入るまでの立ち上がり時間と、中断がそれを毎回ゼロに戻すことを論じた著者本人の所属組織 |
| 〃 | [Flow, the secret to happiness（Mihaly Csikszentmihalyi, TED）](https://www.ted.com/talks/mihaly_csikszentmihalyi_flow_the_secret_to_happiness) | 3 | フロー概念の提唱者本人による講演。挑戦の難度と技能が釣り合ったときに没入が生じるという説明 |
| 〃 | [Sustainable Pace（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/sustainable-pace/) | 3 | 長時間労働ではなく持続できる速度で働くというXPの原則。没入できる状態を守る前提条件として関係する |
| メイカーのスケジュール | [Maker's Schedule, Manager's Schedule（Paul Graham）](https://www.paulgraham.com/makersschedule.html) | 3 | 1本の会議が午後を丸ごと壊すという、作る人と管理する人の時間感覚の違いを説明した原典エッセイ |
| ディープワーク | [Deep Work（Cal Newport）](https://calnewport.com/deep-work-rules-for-focused-success-in-a-distracted-world/) | 3 | 著者本人による書籍紹介ページ。深い仕事と浅い仕事の区別と、深い仕事の希少価値を説く |
| 持続可能なペース | [Sustainable Pace（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/sustainable-pace/)（再掲） | 3 | 無期限に維持できる速度で働くというXP由来のプラクティスの定義 |
| 〃 | [アジャイル宣言の背後にある原則](https://agilemanifesto.org/iso/ja/principles.html)（再掲） | 3 | 第8原則が一定のペースを継続的に維持できることを求めている（日本語公式） |
| 中断のない作業環境 | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco)（再掲） | 3 | 『ピープルウエア』の著者本人の所属組織による紹介。数百人規模の実測から職場環境と生産性の関係を示した Coding War Games を含む |
| 認知負荷理論 | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts) | 3 | 認知負荷の3分類をチームの責任範囲設計に持ち込んだ公式解説 |
| 〃 | [Minimize Team Cognitive Load to Increase Flow（IT Revolution）](https://itrevolution.com/articles/minimize-cognitive-load-of-teams/) | 2 | チームの認知負荷を下げることが流れを速くするという、Skelton・Pais による解説記事 |
| ワーキングメモリの限界 | [The Magical Number Seven, Plus or Minus Two（George A. Miller, 1956）](https://psychclassics.yorku.ca/Miller/) | 3 | 情報処理の限界を7±2と定式化した古典論文の全文（Classics in the History of Psychology） |
| チャンキング | [The Magical Number Seven, Plus or Minus Two（George A. Miller, 1956）](https://psychclassics.yorku.ca/Miller/)（再掲） | 3 | チャンク（塊）という概念を提示し、塊の数が限界であって情報量ではないことを示した原典 |
| 情報ラジエーター | [Information Radiators（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/information-radiators/) | 3 | チームの作業場所に大きく掲示して自然に目に入るようにする可視化装置の定義 |
| 認知バイアス | [Daniel Kahneman – Facts（The Nobel Prize）](https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/facts/) | 3 | 不確実性下の判断における系統的な偏りの研究でノーベル経済学賞を受けた業績の公式紹介 |
| ダブルループ学習 | [Teaching Smart People How to Learn（Chris Argyris, HBR）](https://hbr.org/1991/05/teaching-smart-people-how-to-learn) | 3 | 単ループ学習と二重ループ学習の違いを、優秀な人ほど学べない理由とともに示した原典記事 |
| 守破離 | [ShuHaRi（Martin Fowler）](https://martinfowler.com/bliki/ShuHaRi.html) | 3 | 守破離をソフトウェア開発の学習段階に当てはめ、型の習得を飛ばす危険を説く解説 |
| 意図的な練習 | [The Making of an Expert（Ericsson et al., HBR）](https://hbr.org/2007/07/the-making-of-an-expert) | 3 | 一流の技能は才能ではなく意図的な練習の蓄積で作られると示した Ericsson らの記事 |
| T型スキル | [T-shaped People and Teams（Scrum.org）](https://www.scrum.org/resources/blog/t-shaped-people-and-teams) | 2 | 自己管理するチームが機能するための前提としてT型人材を説明した記事 |
| アンラーニング | [Teaching Smart People How to Learn（Chris Argyris, HBR）](https://hbr.org/1991/05/teaching-smart-people-how-to-learn)（再掲） | 2 | 成功してきた人ほど防衛的になり学び直せないという、アンラーニングの難しさの理論的背景 |
| 成長マインドセット | [What Having a Growth Mindset Actually Means（Carol Dweck, HBR）](https://hbr.org/2016/01/what-having-a-growth-mindset-actually-means) | 3 | 提唱者本人が、努力を褒めるだけの誤用を正した記事 |
| 変革のJカーブ | [The Satir Change Model（Steven M. Smith）](https://stevenmsmith.com/ar-satir-change-model/) | 2 | 変化がもたらす混乱期（カオス）を経て新しい状態に至る5段階モデルの解説 |
| 暗黙知と形式知 | [知識創造企業（新装版）野中郁次郎・竹内弘高（東洋経済新報社）](https://str.toyokeizai.net/books/9784492522325/) | 3 | 暗黙知と形式知の区別を経営学に持ち込み、知識創造のメカニズムを示した原典の出版社ページ |
| 〃 | [知識創造企業（野中郁次郎 / Nonaka Institute of Knowledge）](http://nonaka-ik.org/nonaka/books/219.html) | 3 | 著者本人の研究所による書籍紹介 |
| フロネシス（実践知） | [The Big Idea: The Wise Leader（Ikujiro Nonaka & Hirotaka Takeuchi, HBR 2011）](https://hbr.org/2011/05/the-big-idea-the-wise-leader) | 3 | 知識創造の次の段階として、実践知を備えたリーダーの6つの能力を提示した本人らの論文 |
| 自己決定理論 | [Theory（Center for Self-Determination Theory）](https://selfdeterminationtheory.org/theory/) | 3 | Deci と Ryan による理論の公式サイト。基本的心理欲求としての自律性・有能感・関係性を定義 |
| モチベーション3.0 | [The puzzle of motivation（Dan Pink, TED）](https://www.ted.com/talks/dan_pink_the_puzzle_of_motivation) | 2 | 外的報酬が創造的作業ではむしろ成績を下げるという実験群を紹介した講演 |
| 内発的動機づけ | [Theory（Center for Self-Determination Theory）](https://selfdeterminationtheory.org/theory/)（再掲） | 3 | 内発的動機と外発的動機の連続体、外的報酬による内発的動機の低下を扱う理論の公式解説 |
| ジョブ・クラフティング | [Job Crafting Exercise（University of Michigan, Center for Positive Organizations）](https://positiveorgs.bus.umich.edu/cpo-tools/job-crafting-exercise/) | 3 | Wrzesniewski・Dutton・Berg が開発した、仕事の時間と関係を描き直す演習の公式ページ |
| 自己効力感 | [Teaching Tip Sheet: Self-Efficacy（American Psychological Association）](https://www.apa.org/pi/aids/resources/education/self-efficacy) | 2 | Bandura の自己効力感の定義と、それを高める4つの源泉を整理した心理学会の解説 |
| 燃え尽き（バーンアウト） | [Burn-out an occupational phenomenon（WHO）](https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases) | 3 | 燃え尽きを個人の疾患ではなく職場に起因する現象としてICD-11に位置づけた公式発表 |
| 〃 | [Slack: Getting Past Burnout, Busywork, and the Myth of Total Efficiency（Tom DeMarco）](https://www.penguinrandomhouse.com/books/39276/slack-by-tom-demarco/) | 3 | 燃え尽きと無駄な忙しさを、完全効率を目指す組織構造の帰結として扱った書籍の出版社ページ |

### II. 人とチーム（42要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| ダンバー数 | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | ダンバー数の各層を組織のグルーピング（5-8人、15人、50人、150人…）に対応させる設計指針 |
| 〃 | [When Teams Grow Too Large（Team Topologies）](https://teamtopologies.com/news-blogs-newsletters/when-teams-grow-too-large-solving-cognitive-load-issues) | 3 | 15人を超えると信頼関係の維持が難しくなり認知負荷が上がると述べた公式ニュースレター |
| 2枚のピザルール | [Two-pizza teams（AWS ホワイトペーパー）](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html) | 3 | Amazon が採用する、ピザ2枚で足りる規模の自律チームという組織単位の公式説明 |
| クロスファンクショナルチーム | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | スクラムチームは機能横断であり、各スプリントで価値を生むために必要なすべてのスキルを備えると定義 |
| 4つのチームタイプ | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | 4つのチームタイプと3つのインタラクションモード（コラボレーション／X-as-a-Service／ファシリテーション）の公式定義 |
| 安定したチーム | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | チームを長期に維持し、仕事の側をチームへ流すという組織設計の原則 |
| ダイナミックリチーミング | [Dynamic Reteaming: The Art and Wisdom of Changing Teams（Heidi Helfand）](https://leanpub.com/dynamicreteaming) | 3 | 著者自身による原著の刊行ページ。チームの変え方を Isolation / One by One / Grow and Split / Merging / Switching の5つのパターンとして定義 |
| 〃 | [【資料公開】チームトポロジーで紐解くプロダクト開発組織の進化とスケーリング](https://www.ryuzee.com/contents/blog/14599) | 2 | チーム構造を変更するときにチームトポロジーと組み合わせて5つのパターンを使う、という実務での位置づけ |
| コミュニケーションパスの爆発 | [When Teams Grow Too Large（Team Topologies）](https://teamtopologies.com/news-blogs-newsletters/when-teams-grow-too-large-solving-cognitive-load-issues)（再掲） | 3 | 20人で190通りの経路が生じるという、規模と調整コストの関係の説明 |
| フィーチャーチーム | [Feature Teams（LeSS）](https://less.works/less/structure/feature-teams) | 3 | コンポーネントチームとの違いと、顧客中心に機能を丸ごと担う単位の定義 |
| 心理的安全性 | [The Fearless Organization（Amy C. Edmondson）](https://fearlessorganization.com/) | 3 | 概念の提唱者本人による公式サイト。学習する組織の前提としての心理的安全性を扱う |
| 〃 | [Generative organizational culture（DORA）](https://dora.dev/capabilities/generative-organizational-culture/) | 3 | Westrum の文化類型に基づき、情報の流れと心理的安全性がデリバリー性能に効くことを示したDORAのケイパビリティ解説 |
| チームの5つの機能不全 | [The Five Dysfunctions of a Team（The Table Group）](https://www.tablegroup.com/topics-and-resources/teamwork-5-dysfunctions/) | 3 | Patrick Lencioni 本人の組織による公式解説。5層のピラミッドとしてのモデル |
| 健全な衝突 | [The Five Dysfunctions of a Team（The Table Group）](https://www.tablegroup.com/topics-and-resources/teamwork-5-dysfunctions/)（再掲） | 2 | 衝突への恐怖を第2の機能不全として位置づけ、健全な対立の必要性を説く |
| ワーキングアグリーメント | [アジャイルプラクティスマップ（Agile Studio）](https://www.agile-studio.jp/agile-practice-map) | 2 | スクラム（補完）路線の駅としてワーキングアグリーメントを収録している日本語のプラクティスマップ |
| 信頼の構築 | [Understanding The Trust Equation（Trusted Advisor Associates）](https://trustedadvisor.com/why-trust-matters/understanding-trust/understanding-the-trust-equation) | 2 | 信頼＝(信頼性＋確実性＋親密さ)÷自己志向 という分解を提示した公式解説 |
| ピープルウエア | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco)（再掲） | 3 | 開発の主要な問題は技術的ではなく社会学的だと論じた『ピープルウエア』の著者本人の所属組織 |
| エゴレスプログラミング | [The Psychology of Computer Programming（Gerald M. Weinberg）](https://geraldmweinberg.com/Site/Programming_Psychology.html) | 3 | 1971年にエゴレスプログラミングの概念を提示した、人間中心のソフトウェア開発論の原典。著者本人のサイト |
| タックマンモデル | [Developmental sequence in small groups（Bruce W. Tuckman, 1965）](https://psycnet.apa.org/record/1965-12187-001) | 3 | 形成・混乱・統一・機能の4段階を初めて提示した原論文の書誌（APA PsycNet） |
| 自己管理型チーム | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | スクラムチームは自己管理型であり、誰が何をいつどのように行うかを内部で決めると定義 |
| 〃 | [The New New Product Development Game（Takeuchi & Nonaka, HBR 1986）](https://hbr.org/1986/01/the-new-new-product-development-game) | 3 | 自己組織化するプロジェクトチームを、優れた新製品開発に共通する6つの特性の一つとして挙げた原典 |
| インセプションデッキ | [アジャイルプラクティスマップ（Agile Studio）](https://www.agile-studio.jp/agile-practice-map)（再掲） | 2 | 価値探索路線の駅としてインセプションデッキを収録 |
| サーバントリーダーシップ | [What is Servant Leadership?（Robert K. Greenleaf Center）](https://www.greenleaf.org/what-is-servant-leadership/) | 3 | 提唱者 Greenleaf の名を冠したセンターによる公式定義 |
| スキルマップ | [アジャイルプラクティスマップ（Agile Studio）](https://www.agile-studio.jp/agile-practice-map)（再掲） | 2 | チームビルディング路線の駅としてスキルマップを収録 |
| 幸福指標 | [Niko-niko Calendar（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/niko-niko/) | 3 | 1日の終わりに気分を記号で記録し、チームの傾向を可視化する日本発のプラクティス |
| 結束したチーム | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco)（再掲） | 3 | 『ピープルウエア』で jelled team という語を用い、噛み合ったチームの特徴を示した著者本人の所属組織 |
| 〃 | [Tim Lister（The Atlantic Systems Guild）](https://systemsguild.eu/tim-lister) | 3 | 『ピープルウエア』『熊とワルツを』の共著者本人の所属組織 |
| チーム殺し | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco)（再掲） | 3 | 『ピープルウエア』で teamicide という語を造り、組織がチームを壊す典型的な振る舞いを列挙した著者本人の所属組織 |
| エンジニアリングマネージャー | [エンジニアのためのマネジメントキャリアパス（Camille Fournier『The Manager's Path』邦訳・オライリー・ジャパン）](https://www.oreilly.co.jp/books/9784873118482/) | 3 | メンターからテックリード・エンジニアリングリード・技術部長・CTOまで、段階ごとの役割を定義した書籍 |
| 〃 | [The Engineering Manager 101（LeadDev）](https://leaddev.com/career-development/engineering-manager-101) | 2 | チームの成果・生産性・個人の成長に責任を持つ役割という説明。自分ではコードを書かずレビューと方向づけに回る |
| テックリード | [Talking with Tech Leads（Patrick Kua・Thoughtworks）](https://www.thoughtworks.com/insights/books/talking-with-tech-leads) | 2 | 初めてテックリードになった人と熟練者への聞き取りを集めた書籍。1つのチームに専念する役割として説明している |
| 〃 | [The Definition of a Tech Lead（Patrick Kua）](https://www.patkua.com/blog/the-definition-of-a-tech-lead/) | 2 | チームを率い技術的な方向づけに責任を持つソフトウェアエンジニア、という提唱者本人による定義。EMやチームリードと共同で率いる場合もあるとする |
| 〃 | [エンジニアのためのマネジメントキャリアパス（Camille Fournier『The Manager's Path』邦訳・オライリー・ジャパン）](https://www.oreilly.co.jp/books/9784873118482/)（再掲） | 3 | テックリードを、メンターの次・エンジニアリングリードの手前に置かれた1つの段階として定義した書籍 |
| オンボーディング | [Toward a theory of organizational socialization（Van Maanen & Schein・MIT Sloan・1977）](https://dspace.mit.edu/handle/1721.1/1934) | 3 | 新しく入った人が組織の一員になる過程を組織社会化として定式化した論文。オンボーディングの理論的な源流 |
| 〃 | [スクラム未経験者がチームに加わるときに、どうオンボーディングするとよいでしょうか？（Ryuzee.com）](https://www.ryuzee.com/faq/0086/) | 2 | 経験や力量にあわせて段階的に受け入れる。価値観・ワーキングアグリーメント・完成の定義を先に渡してから作業に入れる |
| 〃 | [新たに開発者が増えたときにどうフォローすればいいですか？（Ryuzee.com）](https://www.ryuzee.com/faq/0069/) | 2 | ペア作業と助走期間を勧め、その間チームの処理量が一時的に落ちることを計画に織り込むべきとする |
| ファシリテーション | [Facilitation（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/facilitation/) | 3 | 議論の内容ではなくプロセスに責任を持つ役割としてのファシリテーションの定義 |
| コーチング | [ICF Core Competencies（International Coaching Federation）](https://coachingfederation.org/about/credentials/core-competencies/) | 3 | 国際コーチング連盟が定める職業としてのコーチングの中核能力 |
| 傾聴 | [ICF Core Competencies（International Coaching Federation）](https://coachingfederation.org/about/credentials/core-competencies/)（再掲） | 3 | アクティブリスニングを職業コーチの中核能力の一つとして定義している |
| フィードバック | [Use Situation-Behavior-Impact to Understand Intent（Center for Creative Leadership）](https://www.ccl.org/articles/leading-effectively-articles/closing-the-gap-between-intent-vs-impact-sbii/) | 3 | SBI（状況・行動・影響）の枠組みを開発した機関による解説 |
| 1on1 | [Coach managers to coach（Google re:Work）](https://rework.withgoogle.com/en/guides/managers-coach-managers-to-coach) | 2 | Google が管理職の実践として1対1の対話を位置づけたガイド |
| 非暴力コミュニケーション | [What is NVC?（Center for Nonviolent Communication）](https://www.cnvc.org/learn/what-is-nvc) | 3 | Marshall Rosenberg が1984年に設立した団体による公式定義。観察・感情・必要・要求の4要素 |
| ふりかえり | [Heartbeat Retrospective（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/heartbeat-retrospective/) | 3 | 反復のたびに行う定期的なふりかえりの定義 |
| 〃 | [ふりかえり実践会](https://hurikaeri.jp/) | 2 | 日本語で手法とTIPSを体系的に公開しているコミュニティ。手法カタログの一次入口 |
| 発散と収束 | [The Double Diamond（Design Council）](https://www.designcouncil.org.uk/our-resources/the-double-diamond/) | 3 | 発見・定義・開発・提供の4段階を2つのダイヤモンドで表した枠組みの公式解説 |
| 合意形成の作法 | [Consent Decision Making（Sociocracy For All）](https://www.sociocracyforall.org/consent-decision-making/) | 2 | 全員の積極的賛成ではなく、重大な反対の不在で決めるという手続きの解説 |
| 場（Ba） | [知識創造企業（新装版）野中郁次郎・竹内弘高（東洋経済新報社）](https://str.toyokeizai.net/books/9784492522325/)（再掲） | 3 | 知識創造が起きるための共有された文脈として「場」を位置づけた原典の出版社ページ |
| ペアプログラミング | [Pair Programming（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/pair-programming/) | 3 | 2人が1台で協働し、役割を交代しながら進めるXPのプラクティスの定義 |
| 〃 | [On Pair Programming（Martin Fowler）](https://martinfowler.com/articles/on-pair-programming.html) | 3 | ペアの型・効用・向かない状況を整理した実務的な解説 |
| モブプログラミング | [Mob Programming（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/mob-programming/) | 3 | チーム全員が同じ課題に同じ時間・場所で取り組む進め方の定義 |
| スウォーミング | [Kanban（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/kanban/)（再掲） | 2 | WIP制限のもとで完了を優先する動きとして、群がる働き方が導かれる |
| 共同所有 | [Collective Ownership（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/collective-ownership/) | 3 | 誰もがどのコードでも変更できるというXPの所有モデルの定義 |
| 非同期コミュニケーション | [Asynchronous communication（GitLab Handbook）](https://about.gitlab.com/company/culture/all-remote/asynchronous/) | 3 | 全社リモートを前提に非同期を既定とする理由と実践を公開している一次資料 |
| 分散チーム | [The Remote Playbook（GitLab Handbook）](https://about.gitlab.com/company/culture/all-remote/guide/) | 3 | 全社リモートの運用を体系的に公開している一次資料 |
| 〃 | [Team Room（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/team-room/) | 3 | 同席を前提としたチームルームの定義。分散チームではこの機能を別手段で置き換える必要がある |

### III. 流れとものづくり（53要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| スクラム | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | Schwaber と Sutherland による公式の定義。スクラムの目的・責任・イベント・作成物・コミットメントを規定 |
| 〃 | [Scrum（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/scrum/) | 3 | 反復で複雑な製品を開発するフレームワークとしての簡潔な定義 |
| 〃 | [The New New Product Development Game（Takeuchi & Nonaka, HBR 1986）](https://hbr.org/1986/01/the-new-new-product-development-game)（再掲） | 3 | スクラムという名称の由来になったラグビーの比喩を示した論文。フレームワークの直接の源流 |
| スプリント（タイムボックス） | [スプリントにおけるコミットメントとは何か（Ryuzee.com）](https://www.ryuzee.com/contents/blog/3567) | 2 | スプリントでのコミットメントは「量を約束する」ことではなく「選んだものを完了させようと全力を尽くす」ことだとする整理 |
| 〃 | [Timebox（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/timebox/) | 3 | あらかじめ決めた時間枠を延長しないという規律の定義 |
| 〃 | [Iteration（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/iteration/) | 3 | 一定期間ごとに動くものを作る反復の単位 |
| デイリースクラム | [Daily Meeting（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/daily-meeting/) | 3 | 毎日同じ時刻に短時間で行う同期のためのミーティングの定義 |
| 〃 | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | デイリースクラムは開発者のための15分のイベントであり、進捗報告の場ではないと規定 |
| スプリントレビュー | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | スプリントレビューは作業結果を検査し今後の適応を決める場であり、単なるデモではないと規定 |
| エクストリームプログラミング | [Extreme Programming（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/xp/) | 3 | Kent Beck らによる、変化する要求に対応するための技術プラクティス群の定義 |
| カンバン | [Kanban（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/kanban/)（再掲） | 3 | 仕掛り制限と可視化によって流れを作る手法の定義 |
| 〃 | [The Official Kanban Guide（Kanban University）](https://kanban.university/kanban-guide/) | 3 | カンバンの実践（可視化・WIP制限・流れの管理・ポリシーの明示・改善）の公式定義 |
| スクラムバン | [Scrumban（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/scrumban/) | 3 | スクラムの構造とカンバンのフロー管理を組み合わせた進め方の定義 |
| 完成の定義 | [Definition of Done（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/definition-of-done/) | 3 | 完了と呼べる状態をチームで明文化する取り決めの定義 |
| 〃 | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | 完成の定義をインクリメントの品質基準として位置づけている |
| 準備完了の定義 | [Definition of Ready（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/definition-of-ready/) | 3 | 着手可能とみなす条件の定義。硬直化すると段階的なゲートに戻る危険も指摘されている |
| 反復型・漸進型開発 | [Iterative Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/iterative-development/) | 3 | 同じ部分を繰り返し作り直して改善する進め方の定義 |
| 〃 | [Incremental Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/incremental-development/) | 3 | 機能を小さな単位で積み増していく進め方の定義 |
| ラグビー型の開発 | [The New New Product Development Game（Hirotaka Takeuchi & Ikujiro Nonaka, HBR 1986）](https://hbr.org/1986/01/the-new-new-product-development-game)（再掲） | 3 | ラグビーのスクラムに喩えて全体一体型の開発を提示した原典。スクラムという名称はここから来ている |
| ウォーターフォール | [Managing the Development of Large Software Systems（Winston W. Royce, 1970）](https://web.archive.org/web/20240120100744/https://www.praxisframework.org/files/royce1970.pdf) | 3 | 段階型の図を最初に示した原論文。著者自身は一度流すだけでは失敗すると書いている（Wayback保存版） |
| 〃 | [The New Methodology（Martin Fowler）](https://martinfowler.com/articles/newMethodology.html) | 2 | 設計と施工を分ける計画駆動の重量級プロセスと、アジャイルの対比を整理した解説 |
| リトルの法則 | [The Official Kanban Guide（Kanban University）](https://kanban.university/kanban-guide/)（再掲） | 3 | フローの計測指標（WIP・スループット・リードタイム）とその関係を定義 |
| WIP制限 | [The Official Kanban Guide（Kanban University）](https://kanban.university/kanban-guide/)（再掲） | 3 | WIPを明示的に制限することをカンバンの必須実践として定義 |
| リードタイムとサイクルタイム | [Lead Time（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/lead-time/) | 3 | 要求が発生してから提供されるまでの経過時間の定義 |
| 〃 | [DORA's software delivery metrics: the four keys](https://dora.dev/guides/dora-metrics-four-keys/) | 3 | 変更のリードタイムを含む4つのデリバリー指標の公式定義 |
| バッチサイズの縮小 | [Working in small batches（DORA）](https://dora.dev/capabilities/working-in-small-batches/) | 3 | 小さなバッチで働くことがデリバリー性能を高めるというDORAのケイパビリティ解説 |
| 累積フロー図 | [The Official Kanban Guide（Kanban University）](https://kanban.university/kanban-guide/)（再掲） | 2 | フローの可視化手段として累積フロー図を位置づけている |
| フロー効率とリソース効率 | [This is Lean（Niklas Modig & Pär Åhlström）](https://thisislean.com/) | 3 | リソース効率とフロー効率の対立（効率性のパラドックス）を提示した書籍の公式サイト |
| 制約理論 | [Theory of Constraints（TOC Institute）](https://www.tocinstitute.org/theory-of-constraints.html) | 2 | Goldratt の制約理論と、制約を特定し従属させる5段階の解説 |
| 待ち行列の効果 | [Work in process limits（DORA）](https://dora.dev/capabilities/wip-limits/) | 3 | 仕掛りを制限することがデリバリー性能を高めるという調査結果。待ち行列が伸びる仕組みへの実務的な対処 |
| ゆとり（スラック） | [Slack: Getting Past Burnout, Busywork, and the Myth of Total Efficiency（Tom DeMarco）](https://www.penguinrandomhouse.com/books/39276/slack-by-tom-demarco/)（再掲） | 3 | 完全効率という神話を退け、組織が変化するために必要な余白を論じた書籍の出版社ページ |
| トヨタ生産方式 | [トヨタ生産方式（トヨタ自動車）](https://global.toyota/jp/company/vision-and-philosophy/production-system/) | 3 | 自働化とジャスト・イン・タイムの2本柱を、生み出した企業自身が説明した一次資料 |
| 〃 | [Toyota Production System（Lean Enterprise Institute）](https://www.lean.org/lexicon-terms/toyota-production-system/) | 3 | ムダの排除で品質・コスト・リードタイムを改善する仕組みとして用語を定義している |
| テスト駆動開発 | [Test Driven Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/tdd/) | 3 | テストを先に書いて設計を駆動する開発サイクルの定義 |
| 〃 | [TestDrivenDevelopment（Martin Fowler）](https://martinfowler.com/bliki/TestDrivenDevelopment.html) | 3 | TDDの3ステップと、設計技法としての位置づけの解説 |
| リファクタリング | [Refactoring（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/refactoring/) | 3 | 外部から見た振る舞いを保ったまま内部構造を改善する作業の定義 |
| 〃 | [DefinitionOfRefactoring（Martin Fowler）](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) | 3 | 用語の厳密な定義と、書き直しとの違いの説明 |
| 継続的インテグレーション | [Continuous Integration（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/continuous-integration/) | 3 | 頻繁な統合と自動検証によって統合の痛みを取り除く実践の定義 |
| 〃 | [Continuous Integration（Martin Fowler）](https://martinfowler.com/articles/continuousIntegration.html) | 3 | CIの実践条件（1日1回以上の統合、自己テスト可能なビルド等）を整理した定番記事 |
| 継続的デリバリー | [Continuous Deployment（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/continuous-deployment/) | 3 | 変更を自動で本番まで届ける実践の定義 |
| 〃 | [Continuous delivery（DORA）](https://dora.dev/capabilities/continuous-delivery/) | 3 | 継続的デリバリーをデリバリー性能の中核ケイパビリティとして扱う公式解説 |
| トランクベース開発 | [Trunk Based Development](https://trunkbaseddevelopment.com/) | 3 | 短命ブランチと幹への高頻度統合を解説する専門サイト |
| 〃 | [Trunk-based development（DORA）](https://dora.dev/capabilities/trunk-based-development/) | 3 | トランクベース開発とデリバリー性能の相関を示すDORAの解説 |
| テストピラミッド | [TestPyramid（Martin Fowler）](https://martinfowler.com/bliki/TestPyramid.html) | 3 | 自動テストを粒度で層に分け、下層を厚くする配分の考え方 |
| 振る舞い駆動開発／受け入れテスト駆動開発 | [Behavior Driven Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/bdd/) | 3 | 期待される振る舞いを自然言語に近い形で記述し開発を駆動する実践の定義 |
| 〃 | [Acceptance Test Driven Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/atdd/) | 3 | 受け入れ条件を先にテストとして定義する実践の定義 |
| シンプルな設計 | [Simple Design（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/simple-design/) | 3 | 現在の要求を満たす最小限の設計を保つXPのプラクティスの定義 |
| 〃 | [Yagni（Martin Fowler）](https://martinfowler.com/bliki/Yagni.html) | 3 | 推測にもとづく機能追加のコストを整理し、必要になるまで作らない理由を説明 |
| 技術的負債 | [TechnicalDebt（Martin Fowler）](https://martinfowler.com/bliki/TechnicalDebt.html) | 3 | Ward Cunningham の比喩の説明と、意図的／不注意・慎重／無謀の4象限 |
| ユビキタス言語 | [Ubiquitous Language（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/ubiquitous-language/) | 3 | 開発者と利用者が共有する厳密な言語を作るという原則の定義 |
| 〃 | [UbiquitousLanguage（Martin Fowler）](https://martinfowler.com/bliki/UbiquitousLanguage.html) | 3 | Eric Evans のDDDにおける共通言語の位置づけの解説 |
| フィーチャーフラグ | [Feature Toggles (aka Feature Flags)（Martin Fowler）](https://martinfowler.com/articles/feature-toggles.html) | 3 | トグルの種類（リリース／実験／運用／許可）と管理の指針を整理した記事 |
| コードレビュー | [Google Engineering Practices – Code Review](https://google.github.io/eng-practices/review/) | 3 | レビューの目的・観点・速度についてGoogleが公開している実務ガイド |
| マイクロサービス | [Microservices（James Lewis・Martin Fowler）](https://martinfowler.com/articles/microservices.html) | 3 | 2014年の定義記事。技術層ではなく業務機能で分け、チームがプロダクトとして所有し続けるという組織の主張を含む |
| 〃 | [Microservice Architecture pattern（Chris Richardson）](https://microservices.io/patterns/microservices.html) | 3 | 独立してデプロイでき疎結合な複数のサービスとして構成し、各サービスをチームが所有する、というパターンの定義 |
| DevOps | [DORA（DevOps Research and Assessment）](https://dora.dev/) | 3 | DevOpsの実践と組織の成果の関係を継続的に調査・公開している研究プログラムの公式サイト |
| 〃 | [The DevOps Handbook（IT Revolution）](https://itrevolution.com/product/the-devops-handbook-second-edition/)（再掲） | 3 | フロー・フィードバック・継続的学習という三つの道を体系化した書籍の公式ページ |
| サイト信頼性エンジニアリング | [Site Reliability Engineering（Google SRE Book）](https://sre.google/sre-book/introduction/) | 3 | Googleが公開しているSREの原典。運用をソフトウェアの問題として扱う立場を説明 |
| SLOとエラーバジェット | [Service Level Objectives（Google SRE Book）](https://sre.google/sre-book/service-level-objectives/) | 3 | SLI・SLO・SLA の区別と、エラーバジェットによる速度と信頼性の調停の解説 |
| オブザーバビリティ | [Monitoring and observability（DORA）](https://dora.dev/capabilities/monitoring-and-observability/) | 3 | 監視と可観測性をデリバリー性能に効くケイパビリティとして扱う公式解説 |
| 非難なきポストモーテム | [Postmortem Culture: Learning from Failure（Google SRE Book）](https://sre.google/sre-book/postmortem-culture/) | 3 | 個人を責めずに仕組みの改善に集中する障害検証の文化の解説 |
| プラットフォームエンジニアリング | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | プラットフォームチームを4タイプの一つとして定義し、認知負荷の軽減を目的に据える |
| 〃 | [What is platform engineering?（platformengineering.org）](https://platformengineering.org/blog/what-is-platform-engineering) | 2 | 内部開発者プラットフォームを製品として扱う考え方の解説 |
| シフトレフト | [Pervasive security（DORA）](https://dora.dev/capabilities/pervasive-security/) | 3 | セキュリティを開発プロセスの早期から全体に組み込むことがデリバリー性能に効くという解説。旧称 shifting left on security |
| Infrastructure as Code | [InfrastructureAsCode（Martin Fowler）](https://martinfowler.com/bliki/InfrastructureAsCode.html) | 3 | インフラ構成をコードとして扱い、バージョン管理とテストの対象にする考え方 |
| 相対見積り | [Relative Estimation（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/relative-estimation/) | 3 | 既知の項目との比較で規模を見積もる手法の定義 |
| プランニングポーカー | [Planning Poker（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/planning-poker/) | 3 | 同時提示によってアンカリングを避け、差異の議論を促す見積り手法の定義 |
| ベロシティ | [Velocity（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/velocity/) | 3 | 反復ごとの完了量の実績値。計画のための指標であると定義 |
| バーンダウン／バーンアップ | [Burndown Chart（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/burndown-chart/) | 3 | 残作業の推移を時系列で示す図の定義 |
| #NoEstimates | [#NoEstimates – Alternative to Estimate-Driven Software Development（Vasco Duarte）](https://www.methodsandtools.com/archive/noestimates.php) | 2 | 運動の中心人物の一人による解説。見積りの代わりに完了した項目数の実績で予測する方法 |
| 確率的な予測 | [The Official Kanban Guide（Kanban University）](https://kanban.university/kanban-guide/)（再掲） | 2 | フローの実測データにもとづく予測をカンバンの実践として位置づけている |
| クネビン・フレームワーク | [About the Cynefin Framework（The Cynefin Company）](https://thecynefin.co/about-us/about-cynefin-framework/)（再掲） | 3 | Dave Snowden が創設した組織による公式解説。5つのドメインと対応する行動様式 |
| スパイク | [Estimation（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/estimation/) | 2 | 見積りの不確実性を減らすための調査作業としてスパイクが位置づけられる文脈 |
| 不確実性のコーン | [Estimation（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/estimation/)（再掲） | 2 | 見積りの不確実性が進行とともに縮小することを含む、見積りの位置づけの解説 |
| リスクを織り込む計画 | [Tom DeMarco（The Atlantic Systems Guild）](https://systemsguild.eu/tom-demarco)（再掲） | 3 | 『熊とワルツを』でソフトウェアプロジェクトの代表的リスク（スケジュール欠陥・要求の膨張・離職・仕様の崩壊・性能未達）と管理法を示した著者本人の所属組織 |

### IV. 価値と事業（38要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| 継続的ディスカバリー | [What is a Product Trio?（Teresa Torres, Product Talk）](https://www.producttalk.org/2021/08/product-trio/) | 3 | 継続的ディスカバリーを担う三人組の役割と、毎週の顧客接点という習慣の解説 |
| ジョブ理論 | [Jobs to Be Done（Clayton Christensen Institute）](https://www.christenseninstitute.org/theory/jobs-to-be-done/) | 3 | Christensen の提唱した理論を、本人が設立した研究所が解説する公式ページ |
| ユーザーインタビュー | [Customer Development（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/customer-development/) | 3 | 建物の外に出て顧客から学ぶという Steve Blank の手法の定義 |
| ペルソナ | [Personas（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/personas/) | 3 | 利用者の典型像を具体的に描いて設計判断に使う手法の定義 |
| カスタマージャーニーマップ | [Journey Mapping 101（Nielsen Norman Group）](https://www.nngroup.com/articles/journey-mapping-101/) | 3 | ジャーニーマップの構成要素と作り方を整理したUX研究機関の解説 |
| オポチュニティ・ソリューションツリー | [Why You Should Use an Opportunity Solution Tree（Teresa Torres）](https://www.producttalk.org/2016/08/opportunity-solution-tree/) | 3 | 成果・機会・解決策・実験を階層で結ぶ発想法の提唱者による解説 |
| デザイン思考 | [Resources（Stanford d.school）](https://dschool.stanford.edu/resources) | 3 | デザイン思考の教育と実践資料を公開しているスタンフォード大学 d.school の公式リソース |
| インパクトマッピング | [Impact Mapping（Gojko Adzic）](https://www.impactmapping.org/) | 3 | 目標・アクター・インパクト・成果物の4階層で施策を導く手法の公式サイト |
| リーンスタートアップ | [The Lean Startup Methodology](https://theleanstartup.com/principles) | 3 | Eric Ries による公式サイト。構築・計測・学習のループと検証的学習の原則 |
| MVP | [Minimum Viable Product（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/mvp/) | 3 | 最小限の労力で最大の検証学習を得るための製品版という定義 |
| 構築・計測・学習ループ | [The Lean Startup Methodology](https://theleanstartup.com/principles)（再掲） | 3 | 構築・計測・学習のフィードバックループを最短化することを中核原則とする公式解説 |
| ピボット | [The Lean Startup Methodology](https://theleanstartup.com/principles)（再掲） | 3 | 検証結果にもとづく方向転換としてのピボットを定義した公式解説 |
| リーンキャンバス | [Lean Canvas（LEANSTACK / Ash Maurya）](https://leanstack.com/lean-canvas) | 3 | ビジネスモデルキャンバスをスタートアップ向けに改変した1枚のフレームの公式解説 |
| A/Bテスト | [A/B Testing 101（Nielsen Norman Group）](https://www.nngroup.com/articles/ab-testing/) | 3 | A/Bテストの仕組みと、使える場面・使えない場面の整理 |
| リーンの原則とムダ | [Lean Thinking（Lean Enterprise Institute）](https://www.lean.org/lexicon-terms/lean-thinking/) | 3 | 価値・価値の流れ・流れ・引き・完全性という5原則の定義 |
| WSJF | [WSJF（SAFe）](https://framework.scaledagile.com/wsjf) | 3 | 遅延コスト÷ジョブサイズで優先順位を算出する手法の公式定義 |
| 遅延コスト | [Cost of Delay（Black Swan Farming, Joshua Arnold）](https://blackswanfarming.com/cost-of-delay/) | 2 | 遅延コストの算出と、優先順位づけへの適用を体系的に解説 |
| 投資対効果 | [Return on Investment (ROI) Formula（Corporate Finance Institute）](https://corporatefinanceinstitute.com/resources/accounting/return-on-investment-roi-formula/) | 2 | 投資額に対する利益の比率の定義・計算式と、期間を考慮しないという限界の説明 |
| 正味現在価値 | [Net Present Value (NPV)（Corporate Finance Institute）](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/) | 2 | 将来キャッシュフローを割引率で現在価値に換算して投資を評価する方法の定義と計算例 |
| 狩野モデル | [アジャイルプラクティスマップ（Agile Studio）](https://www.agile-studio.jp/agile-practice-map)（再掲） | 2 | 価値探索路線の駅として狩野分析を収録している日本語のプラクティスマップ |
| 〃 | [Kano Model（American Society for Quality）](https://asq.org/quality-resources/kano-model) | 2 | 狩野紀昭による品質の分類モデルの解説 |
| MoSCoW | [MoSCoW Prioritisation（Agile Business Consortium / DSDM Project Framework）](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) | 3 | DSDM を策定した団体による公式定義。Must/Should/Could/Won't の4段階と適用範囲 |
| 最終責任時点 | [Last Responsible Moment（Agile Pain Relief 用語集）](https://agilepainrelief.com/glossary/last-responsible-moment/) | 2 | Poppendieck のリーン開発に由来する原則の定義。重要な選択肢が失われる直前が決定の期限であるとする |
| オプション思考 | [Real Options（InfoQ）](https://www.infoq.com/articles/real-options-enhance-agility/) | 2 | Chris Matts らによる、意思決定を選択肢として扱う考え方の解説 |
| OKR | [What is an OKR?（What Matters / John Doerr）](https://www.whatmatters.com/faqs/okr-meaning-definition-example) | 3 | OKRを広めた John Doerr による公式の定義と実例 |
| プロダクトゴール | [The Scrum Guide](https://scrumguides.org/scrum-guide.html)（再掲） | 3 | プロダクトゴールをプロダクトバックログのコミットメントとして定義している |
| アウトカムとアウトプット | [Evidence-Based Management（Scrum.org）](https://www.scrum.org/resources/evidence-based-management) | 3 | 現在価値・未実現価値・市場投入時間・イノベーション能力という成果側の指標群を定義 |
| North Star指標 | [North Star Metric（Amplitude）](https://amplitude.com/blog/product-north-star-metric) | 2 | プロダクトの価値を代表する単一指標の選び方と、入力指標との関係の解説 |
| ビルドトラップ | [Escaping the Build Trap（Melissa Perri, Mind the Product）](https://www.mindtheproduct.com/escaping-build-trap-melissa-perri/) | 3 | 提唱者本人の講演を収録した記事。価値を機能の産出量で測ることが組織を罠に閉じ込めると説明 |
| 虚栄の指標 | [The Lean Startup Methodology](https://theleanstartup.com/principles)（再掲） | 2 | イノベーション会計の文脈で、行動につながらない指標を退ける考え方を提示 |
| 品質とは誰かにとっての価値 | [Gerald M. Weinberg（本人サイト）](https://geraldmweinberg.com/Site/Home.html)（再掲） | 3 | 『Quality Software Management: Systems Thinking』で品質を「誰かにとっての価値」と定義した著者の公式サイト |
| プロダクトマネージャー | [Behind Every Great Product（Marty Cagan・Silicon Valley Product Group）](https://www.svpg.com/behind-every-great-product/) | 3 | プロダクトの定義だけでなく事業の成果に責任を持つ役割だ、と提唱者本人が6つの実例で定義した記事 |
| 〃 | [What, exactly, is a Product Manager?（Martin Eriksson）](https://www.mindtheproduct.com/what-exactly-is-a-product-manager/) | 2 | 事業・技術・ユーザー体験の交点に立つ役割という2011年の定番の定義 |
| 〃 | [プロダクトマネージャーとプロダクトオーナーは別のものですか？（Ryuzee.com）](https://www.ryuzee.com/faq/0078/) | 2 | 業務範囲はプロダクトマネージャー＞プロダクトオーナーで、POはスクラムチームのデリバリー中心という日本語圏での整理 |
| ユーザーストーリー | [User Stories（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/user-stories/) | 3 | 利用者にとっての価値を短く記述し、詳細は会話で詰めるという要求形式の定義 |
| 3つのC | [The Three C's（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/three-cs/) | 3 | Ron Jeffries によるカード・会話・確認の3要素の定義 |
| INVEST | [INVEST（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/invest/) | 3 | Bill Wake による、良いユーザーストーリーの6つの性質の定義 |
| 受け入れ基準 | [Acceptance Testing（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/acceptance-testing/) | 3 | 受け入れ条件を満たすかを確認するテストの定義 |
| ストーリー分割 | [Story Splitting（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/story-splitting/) | 3 | 大きなストーリーを価値を保ったまま分割する技法の定義 |
| ユーザーストーリーマッピング | [Story Mapping（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/story-mapping/) | 3 | 利用者の活動の流れに沿ってストーリーを二次元に配置する手法の定義 |
| 〃 | [Story Mapping（Jeff Patton）](https://jpattonassociates.com/story-mapping/) | 3 | 手法の提唱者本人による解説。平坦なバックログが失う全体像を取り戻す目的 |
| プロダクトバックログ | [Product Backlog（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/backlog/) | 3 | プロダクトに必要な作業を優先順位づけて並べた一覧の定義 |
| 〃 | [Backlog Refinement（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/backlog-refinement/) | 3 | バックログ項目を継続的に分割・見直し・詳細化する活動の定義 |

### V. 組織とガバナンス（34要素）

| 要素 | 出典 | 強度 | 概要 |
|---|---|---|---|
| コンウェイの法則 | [Conway's Law（Melvin E. Conway）](https://www.melconway.com/Home/Conways_Law.html) | 3 | 提唱者本人による、組織のコミュニケーション構造が設計を規定するという命題の説明 |
| 〃 | [ConwaysLaw（Martin Fowler）](https://martinfowler.com/bliki/ConwaysLaw.html) | 3 | 法則のソフトウェア設計への含意と、組織を先に設計するという発想の解説 |
| 逆コンウェイ戦略 | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | 望ましいアーキテクチャに合わせてチーム構造を設計するという逆コンウェイの実践 |
| バリューストリーム型組織 | [Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)（再掲） | 3 | ストリームアラインドチームを基本形とし、価値の流れに合わせて組織を組む原則 |
| サイロ（職能別の分断） | [Generative organizational culture（DORA）](https://dora.dev/capabilities/generative-organizational-culture/)（再掲） | 3 | Westrum の3類型（病理的・官僚的・創造的）にもとづき、情報が部門を越えて流れるかどうかが成果を左右すると示したDORAの解説 |
| 実践共同体 | [Communities of Practice: The Organizational Frontier（Wenger & Snyder, HBR）](https://hbr.org/2000/01/communities-of-practice-the-organizational-frontier) | 3 | 概念の提唱者 Etienne Wenger 本人による、組織における実践共同体の定義と、チームや部門との違い |
| プロジェクトからプロダクトへ | [Lean Portfolio Management（SAFe）](https://www.scaledagileframework.com/lean-portfolio-management/) | 2 | プロジェクト単位の資金配分から、価値の流れへの継続的な資金配分に移す考え方 |
| SAFe | [SAFe Framework（Scaled Agile）](https://framework.scaledagile.com/) | 3 | 7つのコアコンピテンシーを中心に据えた大規模フレームワークの公式サイト |
| LeSS | [Introduction to LeSS（The LeSS Company）](https://less.works/less/framework/introduction) | 3 | 役割と成果物を増やさずスクラムを拡張するという原則の公式解説 |
| Nexus / Scrum@Scale | [The Nexus Guide（Scrum.org）](https://www.scrum.org/resources/online-nexus-guide) | 3 | 3〜9チームのスクラムチームを統合する枠組みの公式ガイド |
| 〃 | [The Scrum@Scale Guide](https://www.scrumatscale.com/scrum-at-scale-guide/) | 3 | Jeff Sutherland によるスケールフリーな拡張モデルの公式ガイド |
| Spotifyモデル | [Scaling Agile @ Spotify（Henrik Kniberg & Anders Ivarsson）](https://blog.crisp.se/2012/11/14/henrikkniberg/scaling-agile-at-spotify) | 3 | 原典の解説記事。あくまで当時のスナップショットでありモデルではないと本人が後に注記している |
| スクラム・オブ・スクラムズ | [Scrum of Scrums（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/scrum-of-scrums/) | 3 | 複数チームの代表が集まり調整を行うスケーリングの技法の定義 |
| Beyond Budgeting | [Beyond Budgeting Institute](https://bbrt.org/) | 3 | 12原則（リーダーシップ6・マネジメントプロセス6）を策定した団体の公式サイト |
| リーンポートフォリオマネジメント | [Lean Portfolio Management（SAFe）](https://www.scaledagileframework.com/lean-portfolio-management/)（再掲） | 2 | 戦略と投資の資金配分、アジャイルなポートフォリオ運営、リーンガバナンスの3領域の解説 |
| 権限委譲 | [Delegation Poker（Management 3.0）](https://management30.com/practice/delegation-poker/) | 3 | 権限を7段階で表し、項目ごとに合意する実践の公式解説 |
| アジャイルな契約 | [情報システム・モデル取引・契約書（アジャイル開発版）｜IPA](https://www.ipa.go.jp/digital/model/agile20200331.html) | 3 | 2020年3月31日公開。アジャイル開発では請負ではなく準委任契約を基本とする、日本の実務向け公的モデル契約 |
| ステージゲートとの折り合い | [Process Goals（PMI Disciplined Agile）](https://www.pmi.org/disciplined-agile/process/introduction-to-dad/process-goals) | 3 | 資金確保やガバナンスを含む意思決定をプロセスゴールとして扱い、文脈に応じた選択肢を示す |
| 組織開発 | [What is Organization Development?（OD Network）](https://www.odnetwork.org/what-is-od) | 3 | 組織開発を専門とする国際的な実務者ネットワークによる領域の定義 |
| 〃 | [組織開発とは（慶應丸の内シティキャンパス）](https://www.keiomcc.com/organization-development/) | 2 | 日本語で組織開発の定義と人材開発との違いを整理した教育機関の解説 |
| レヴィンの3段階モデル | [Lewin's Change Management Model](https://www.mindtools.com/ajm9l1e/lewins-change-management-model) | 1 | クルト・レヴィンによる3段階モデルと力の場の分析の解説 |
| コッターの8段階 | [The 8 Steps for Leading Change（Kotter Inc.）](https://www.kotterinc.com/methodology/8-steps/) | 3 | John Kotter 本人の会社による8段階の公式解説 |
| ADKAR | [The Prosci ADKAR Model](https://www.prosci.com/methodology/adkar) | 3 | モデルを開発した Prosci による5要素の公式定義 |
| アプリシエイティブ・インクワイアリー | [About Appreciative Inquiry（Cooperrider Center, Champlain College）](https://appreciativeinquiry.champlain.edu/about-appreciative-inquiry/) | 3 | David Cooperrider の名を冠した唯一の学術センターによる手法の公式解説。4-Dサイクルを含む |
| 成功の循環モデル | [What is Your Organization's Core Theory of Success?（The Systems Thinker）](https://thesystemsthinker.com/what-is-your-organizations-core-theory-of-success/) | 3 | MIT組織学習センター共同創設者 Daniel Kim による、関係・思考・行動・結果が強化ループをなすモデルの解説 |
| 学習する組織 | [The Systems Thinker](https://thesystemsthinker.com/)（再掲） | 2 | Peter Senge らの系譜にあるシステム思考と学習する組織の論考を集めた媒体 |
| Westrumの組織文化類型 | [Generative organizational culture（DORA）](https://dora.dev/capabilities/generative-organizational-culture/)（再掲） | 3 | Westrum の3類型と、創造的（generative）な文化がデリバリー性能と組織成果に効くという調査結果。DORAでは現在この名称で扱われている |
| SECIモデル | [知識創造企業（新装版）野中郁次郎・竹内弘高（東洋経済新報社）](https://str.toyokeizai.net/books/9784492522325/)（再掲） | 3 | SECIモデルを提示し、日本企業のイノベーションの仕組みを知識創造として説明した原典の出版社ページ |
| 〃 | [知識創造企業（野中郁次郎 / Nonaka Institute of Knowledge）](http://nonaka-ik.org/nonaka/books/219.html)（再掲） | 3 | 著者本人の研究所による書籍紹介 |
| ミドル・アップダウン | [知識創造企業（新装版）野中郁次郎・竹内弘高（東洋経済新報社）](https://str.toyokeizai.net/books/9784492522325/)（再掲） | 3 | トップダウンでもボトムアップでもない第三のマネジメント様式としてミドル・アップダウンを提示した原典 |
| 失敗の本質 | [『失敗の本質 ― 日本軍の組織論的研究』特設サイト（中央公論新社）](https://www.chuko.co.jp/special/shippaino-honshitsu/) | 3 | 戸部良一・寺本義也・鎌田伸一・杉之尾孝生・村井友秀・野中郁次郎による共著。日本型組織の失敗の構造を6つの作戦から分析した研究書の出版社特設ページ |
| DORAの4つの指標 | [DORA's software delivery metrics: the four keys](https://dora.dev/guides/dora-metrics-four-keys/)（再掲） | 3 | 4指標の定義と使い方、性能の分布としての扱い方を示した公式ガイド |
| SPACEフレームワーク | [The SPACE of Developer Productivity（ACM Queue）](https://queue.acm.org/detail.cfm?id=3454124) | 3 | Forsgren らによる原論文。生産性を5次元で捉え単一指標を避けるべき理由を示す |
| エビデンスベースドマネジメント | [Evidence-Based Management（Scrum.org）](https://www.scrum.org/resources/evidence-based-management)（再掲） | 3 | Ken Schwaber と Scrum.org による4つの価値領域（KVA）の公式定義 |
| 成熟度モデルの罠 | [DORA Capabilities](https://dora.dev/capabilities/) | 3 | 成熟度の段階付けではなく、継続的に伸ばすケイパビリティの集合として整理している公式ページ |
| 統制と俊敏さの両立 | [Streamlining change approval（DORA）](https://dora.dev/capabilities/streamlining-change-approval/) | 3 | 外部承認プロセスがデリバリー性能を下げ、安定性も改善しないという調査結果と代替案 |
| ビジネスアジリティ | [Business Agility（Agile Alliance Glossary）](https://www.agilealliance.org/glossary/business-agility/) | 3 | 組織が市場の変化に素早く適応する能力としての定義 |
| 〃 | [The Domains of Business Agility（Business Agility Institute）](https://businessagility.institute/domains/overview) | 3 | 5つのドメインと18のケイパビリティからなるモデルの公式入口 |
| 計測の限界 | [Software Engineering: An Idea Whose Time Has Come and Gone?（Tom DeMarco, IEEE Software 2009）](https://www.computer.org/csdl/magazine/so/2009/04/mso2009040096/13rRUxYIN5T) | 3 | 自著の「測れないものは管理できない」を本人が撤回し、厳密な管理が効くのは価値の低いプロジェクトだけだと述べた論考 |

---

## 第2部 設計に使った参照

要素の出典ではなく、**大枠をどう切るかを決めるために読んだもの**です。

### 先行するプラクティスマップ（再発明を避けるために全件照合した）

- **[Subway Map to Agile Practices（Agile Alliance）](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/)**
  - 9本の路線（Scrum / XP / Lean / Testing / Product Management / DevOps / Teams & Culture / Design / Fundamentals）でアジャイルのプラクティスを路線図として並べた先行マップ。分類の軸は「出自」
  - 2026-09-15 時点で到達確認
- **[Agile Glossary（Agile Alliance）](https://www.agilealliance.org/agile101/agile-glossary/)**
  - Subway Map の各駅に対応する公式用語集。78語のスラッグを抽出し、本マップの出典と照合の原簿にした
  - 2026-09-15 にページ本文を取得
- **[アジャイルプラクティスマップ（Agile Studio / 永和システムマネジメント）](https://www.agile-studio.jp/agile-practice-map)**
  - 5路線49駅の日本語の路線図。スクラム／スクラム（補完）／XP／価値探索／チームビルディング。これから始める開発者向けであることを明示している
  - 2026-09-15 にブラウザで全駅を抽出

### 大枠の骨格を接続した既存タクソノミー

- **[Agile Delivery Learning Roadmap（ICAgile）](https://www.icagile.com/agile-delivery)**
  - Agile Coaching / Engineering / Testing / Delivery Management / DevOps / Product Ownership などの学習トラック。職能が独立領域として成立していることの裏取りに使った
  - 2026-09-15 時点で到達確認
- **[Process Goals（PMI Disciplined Agile）](https://www.pmi.org/disciplined-agile/toolkit/process-goals)**
  - Inception / Construction / Transition / Ongoing の4フェーズ24ゴール。資金確保やガバナンスなど開発の外側の意思決定を拾う参照にした
  - 2026-09-15 時点で到達確認
- **[The Domains of Business Agility（Business Agility Institute）](https://businessagility.institute/domains/overview)**
  - 5ドメイン18ケイパビリティ。顧客を中心に置き、リーダーシップ・個人・オペレーションの次元で組織能力を整理する。IV層とV層の受け皿の根拠
  - 2026-09-15 時点で到達確認
- **[SAFe Framework（Scaled Agile）](https://framework.scaledagile.com/)**
  - 7つのコアコンピテンシー（Lean-Agile Leadership / Team and Technical Agility / Agile Product Delivery / Enterprise Solution Delivery / Lean Portfolio Management / Organizational Agility / Continuous Learning Culture）。V層（組織）の裏取り
  - 2026-09-15 はbot対策で本文取得不可。構成は検索結果で確認
- **[Key Concepts（Team Topologies）](https://teamtopologies.com/key-concepts)**
  - 4チームタイプ×3インタラクションモードと認知負荷。既存体系のなかで唯一「人間の認知の限界」をチーム設計に接続しており、I層とII層の骨格の根拠になった
  - 2026-09-15 時点で到達確認
- **[DORA Capabilities](https://dora.dev/capabilities/)**
  - 成熟度の段階付けではなく継続的に伸ばす能力の集合として整理されたカタログ。本マップの計測系要素の出典元であり、ケイパビリティという考え方自体も参照した
  - 2026-09-15 時点で到達確認
- **[The SPACE of Developer Productivity（ACM Queue）](https://queue.acm.org/detail.cfm?id=3454124)**
  - 生産性を満足度・パフォーマンス・活動・協働・効率の5次元で捉える原論文。単一指標を避けるという立場が本マップのスコア設計の考え方に影響した
  - 2026-09-15 はbot対策で本文取得不可。定義は検索結果で確認

### 「認知の限界」を独立した層として立てるための参照

- **[Multitasking: Switching costs（American Psychological Association）](https://www.apa.org/topics/research/multitasking)**
  - Rubinstein・Meyer・Evans の実験にもとづく切替コストの解説。目標の切替とルールの再活性化という2段階
  - 2026-09-15 時点で到達確認
- **[The Financial Cost of Task Switching（Scrum.org）](https://www.scrum.org/resources/blog/financial-cost-task-switching)**
  - Weinberg の経験則（2案件並行で各40%、20%が切替で消える）と、それが実験結果ではなく工学的な見積りであるという但し書き
  - 2026-09-15 時点で到達確認
- **[When Teams Grow Too Large（Team Topologies）](https://teamtopologies.com/news-blogs-newsletters/when-teams-grow-too-large-solving-cognitive-load-issues)**
  - ダンバー数の層（5・15・50・150）とコミュニケーション経路の爆発（20人で190通り）を組織設計に接続した記事
  - 2026-09-15 時点で到達確認

### 日本語圏の参照

- **[組織開発とは（慶應丸の内シティキャンパス）](https://www.keiomcc.com/organization-development/)**
  - 組織開発を「制度ではなく人と人の関係の質に働きかける実践」として定義し、人材開発との違いを整理した日本語の解説
  - 2026-09-15 時点で到達確認
- **[ふりかえり実践会](https://hurikaeri.jp/)**
  - ふりかえりの手法とTIPSを日本語で体系的に公開しているコミュニティ。II-4のふりかえり関連の粒度を決める参考にした
  - 2026-09-15 時点で到達確認
- **[情報システム・モデル取引・契約書（アジャイル開発版）｜IPA](https://www.ipa.go.jp/digital/model/agile20200331.html)**
  - 日本の実務でアジャイル開発の契約を準委任で組むための公的モデル。V-3の契約要素の根拠
  - 2026-09-15 時点で到達確認
- **[アジャイルソフトウェア開発宣言（日本語公式）](https://agilemanifesto.org/iso/ja/manifesto.html)**
  - 4つの価値の日本語訳の原文。土台の帯の起点
  - 2026-09-15 時点で到達確認

---

## 到達性の確認について

到達確認は curl による HTTP ステータスと本文サイズの取得による。agilealliance.org / scaledagile.com / thesystemsthinker.com など一部のサイトは連続アクセスに対して 403 / 202 を返すが、これは bot 対策であって URL の無効を意味しない（単発・間隔をあけたアクセスでは 200 と実体が返ることを確認済み）。回避はしていない。

確認は `python3 scripts/check_urls.py` で全件まとめて実行できます（同一ドメインへの連続アクセスでレート制限に当たらないよう、ドメイン単位で直列化しています）。
