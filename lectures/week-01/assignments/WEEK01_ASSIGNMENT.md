# Week 1 Assignment: Simple Maze Layout
# 第1週課題：シンプルな迷路レイアウト

**Due Date / 提出期限:** Before Week 2 lecture / 第2週講義前
**Points / 配点:** 10 points / 10点
**Developer / 開発者:** Yuri Tijerino

---

## Assignment Overview / 課題概要

### English
Create a simple 3D maze layout in Blender that will serve as the foundation for your game project. This assignment tests your understanding of Blender's interface, basic modeling tools, and file management with GitHub.

### 日本語
ゲームプロジェクトの基礎となるシンプルな3D迷路レイアウトをBlenderで作成します。この課題は、Blenderのインターフェース、基本的なモデリングツール、GitHubによるファイル管理の理解をテストします。

---

## Learning Objectives / 学習目標

### English
By completing this assignment, you will demonstrate your ability to:
1. Navigate Blender's 3D viewport
2. Create and manipulate basic 3D objects
3. Use transformation tools (move, rotate, scale)
4. Work in Edit Mode
5. Organize and save Blender project files
6. Use GitHub for version control

### 日本語
この課題を完了することで、以下の能力を示します：
1. Blenderの3Dビューポートをナビゲート
2. 基本的な3Dオブジェクトを作成し操作
3. トランスフォームツール（移動、回転、拡大縮小）を使用
4. 編集モードで作業
5. Blenderプロジェクトファイルを整理して保存
6. バージョン管理にGitHubを使用

---

## Assignment Requirements / 課題要件

### Part 1: Maze Design / パート1：迷路デザイン

#### English

Your maze must include the following elements:

**1. Floor (1 point / 1点)**
- Create a floor plane for the maze
- Minimum size: 10 x 10 Blender units
- Can be one large plane or multiple connected planes

**2. Walls (3 points / 3点)**
- Create walls using cubes or extruded edges
- Minimum of 15 wall segments
- Walls should create at least 3 distinct pathways
- Wall height: at least 2 Blender units
- Wall thickness: at least 0.2 Blender units

**3. Start Area (1 point / 1点)**
- Clearly designated starting area for the player
- Can be marked with a different object or color
- Should be an open space (no walls blocking it)

**4. Goal/Hole (2 points / 2点)**
- Create a goal area or hole where the ball will fall
- Can be:
  - A hole in the floor (using Edit Mode to delete faces)
  - A different colored area
  - A cylinder marking the target
- Should be clearly visible and accessible from the start

**5. Proper Organization (1 point / 1点)**
- All objects properly named in the Outliner:
  - "Floor"
  - "Wall_01", "Wall_02", etc.
  - "StartArea"
  - "Goal"
- Use Collections to organize maze elements

#### 日本語

迷路には以下の要素が含まれている必要があります：

**1. 床（1点）**
- 迷路用の床平面を作成
- 最小サイズ：10 x 10 Blenderユニット
- 1つの大きな平面または複数の接続された平面でも可

**2. 壁（3点）**
- 立方体または押し出されたエッジを使用して壁を作成
- 最小15の壁セグメント
- 壁は少なくとも3つの異なる経路を作成する必要があります
- 壁の高さ：少なくとも2 Blenderユニット
- 壁の厚さ：少なくとも0.2 Blenderユニット

**3. スタートエリア（1点）**
- プレイヤーの明確に指定された開始エリア
- 異なるオブジェクトまたは色でマークできます
- オープンスペースである必要があります（壁で塞がれていない）

**4. ゴール/穴（2点）**
- ボールが落ちるゴールエリアまたは穴を作成
- 以下が可能:
  - 床の穴（編集モードを使用して面を削除）
  - 異なる色のエリア
  - ターゲットをマークする円柱
- スタートから明確に見えてアクセス可能である必要があります

**5. 適切な整理（1点）**
- アウトライナーですべてのオブジェクトが適切に名前付けされている：
  - 「Floor」
  - 「Wall_01」、「Wall_02」など
  - 「StartArea」
  - 「Goal」
- Collectionsを使用して迷路要素を整理

---

### Part 2: Technical Requirements / パート2：技術要件

#### English

**File Management (2 points / 2点)**
1. Save your Blender file as `week01_maze_[yourname].blend`
   - Example: `week01_maze_yuri.blend`
2. Save in your GitHub repository folder: `game-dev-2025-yourname/week-01/`
3. Include a screenshot of your maze (top view)
   - File name: `week01_maze_screenshot.png`

**GitHub Submission (1 point / 1点)**
1. Commit your files with a descriptive message
2. Push to your GitHub repository
3. Verify files are visible on GitHub.com

#### 日本語

**ファイル管理（2点）**
1. Blenderファイルを`week01_maze_[yourname].blend`として保存
   - 例：`week01_maze_yuri.blend`
2. GitHubリポジトリフォルダに保存：`game-dev-2025-yourname/week-01/`
3. 迷路のスクリーンショット（上面図）を含める
   - ファイル名：`week01_maze_screenshot.png`

**GitHub提出（1点）**
1. 説明的なメッセージでファイルをコミット
2. GitHubリポジトリにプッシュ
3. GitHub.comでファイルが表示されることを確認

---

## Design Constraints / デザイン制約

### English

**What you CAN do:**
- ✅ Make the maze as complex as you want (minimum requirements above)
- ✅ Add additional decorative objects
- ✅ Experiment with different wall heights
- ✅ Create multiple paths and dead ends
- ✅ Add ramps or stairs (advanced, optional)

**What you should NOT do yet:**
- ❌ Don't add materials or textures (Week 2 topic)
- ❌ Don't add lights or cameras (not needed yet)
- ❌ Don't add animations (Week 2 topic)
- ❌ Keep it simple - this is just the layout

### 日本語

**できること:**
- ✅ 迷路を好きなだけ複雑にする（上記の最小要件）
- ✅ 追加の装飾オブジェクトを追加
- ✅ 異なる壁の高さを試す
- ✅ 複数のパスと行き止まりを作成
- ✅ スロープや階段を追加（上級、オプション）

**まだすべきでないこと:**
- ❌ マテリアルやテクスチャを追加しない（第2週のトピック）
- ❌ ライトやカメラを追加しない（まだ不要）
- ❌ アニメーションを追加しない（第2週のトピック）
- ❌ シンプルに保つ - これは単なるレイアウトです

---

## Step-by-Step Guide / ステップバイステップガイド

### English

**Step 1: Set Up Your Workspace**
1. Open Blender
2. Delete the default cube (X → Delete)
3. Save immediately: File → Save As → Navigate to your GitHub repo week-01 folder

**Step 2: Create the Floor**
1. Add a plane: Shift+A → Mesh → Plane
2. Scale it up: S → 10 → Enter
3. Rename in Outliner: Double-click "Plane" → type "Floor"

**Step 3: Create Walls**
1. **Method A (Individual Cubes):**
   - Add cube: Shift+A → Mesh → Cube
   - Scale: S → X → 0.1 (thin), S → Z → 2 (tall)
   - Move into position: G → X/Y
   - Duplicate: Shift+D
   - Repeat to create maze layout

2. **Method B (Extrude from edges - Advanced):**
   - Select floor, Tab (Edit Mode)
   - Select edge (Alt+Click)
   - Extrude up: E → Z → 2
   - Create wall thickness: I (Inset) or scale

**Step 4: Create Start and Goal**
1. Start area: Add a small cube or cylinder, scale and position
2. Goal:
   - Option A: Add cylinder, scale flat
   - Option B: Select floor face in Edit Mode, X → Delete Faces

**Step 5: Organize**
1. Rename all objects in Outliner
2. Optional: Create Collection (M → New Collection → "Maze")
3. Add all maze objects to collection

**Step 6: Take Screenshot**
1. Change to top view: NumPad 7
2. Frame all: Home key
3. Render → Viewport Render Image
4. Image → Save As → `week01_maze_screenshot.png`
5. Save to week-01 folder

**Step 7: Save and Submit**
1. Save Blender file: Ctrl+S / Cmd+S
2. Open GitHub Desktop or Terminal
3. Commit with message: "Complete Week 1 maze assignment"
4. Push to GitHub
5. Verify on GitHub.com

### 日本語

**ステップ1：ワークスペースをセットアップ**
1. Blenderを開く
2. デフォルトキューブを削除（X → Delete）
3. すぐに保存：File → Save As → GitHubリポジトリのweek-01フォルダに移動

**ステップ2：床を作成**
1. 平面を追加：Shift+A → Mesh → Plane
2. 拡大：S → 10 → Enter
3. アウトライナーで名前変更：「Plane」をダブルクリック → 「Floor」と入力

**ステップ3：壁を作成**
1. **方法A（個別のキューブ）:**
   - キューブを追加：Shift+A → Mesh → Cube
   - スケール：S → X → 0.1（薄く）、S → Z → 2（高く）
   - 位置に移動：G → X/Y
   - 複製：Shift+D
   - 繰り返して迷路レイアウトを作成

2. **方法B（エッジから押し出し - 上級）:**
   - 床を選択、Tab（編集モード）
   - エッジを選択（Alt+クリック）
   - 上に押し出し：E → Z → 2
   - 壁の厚さを作成：I（インセット）またはスケール

**ステップ4：スタートとゴールを作成**
1. スタートエリア：小さなキューブまたは円柱を追加、スケールと位置を調整
2. ゴール：
   - オプションA：円柱を追加、平らにスケール
   - オプションB：編集モードで床の面を選択、X → Delete Faces

**ステップ5：整理**
1. アウトライナーですべてのオブジェクトの名前を変更
2. オプション：Collectionを作成（M → New Collection → 「Maze」）
3. すべての迷路オブジェクトをコレクションに追加

**ステップ6：スクリーンショットを撮る**
1. 上面図に変更：NumPad 7
2. すべてをフレーム：Homeキー
3. Render → Viewport Render Image
4. Image → Save As → `week01_maze_screenshot.png`
5. week-01フォルダに保存

**ステップ7：保存して提出**
1. Blenderファイルを保存：Ctrl+S / Cmd+S
2. GitHub DesktopまたはTerminalを開く
3. メッセージでコミット：「Complete Week 1 maze assignment」
4. GitHubにプッシュ
5. GitHub.comで確認

---

## Grading Rubric / 採点基準

### English

| Criteria / 基準 | Points / 点数 | Description / 説明 |
|------------------|---------------|-------------------|
| Floor | 1 | Floor plane present and appropriately sized<br/>床平面が存在し、適切なサイズ |
| Walls | 3 | At least 15 wall segments creating 3+ pathways<br/>少なくとも15の壁セグメントが3つ以上の経路を作成 |
| Start Area | 1 | Clearly marked starting location<br/>明確にマークされた開始位置 |
| Goal | 2 | Visible and accessible goal area<br/>見えてアクセス可能なゴールエリア |
| Organization | 1 | Objects properly named and organized<br/>オブジェクトが適切に名前付けされ整理されている |
| File Management | 2 | Correct file naming and screenshot included<br/>正しいファイル名とスクリーンショット含まれる |
| GitHub Submission | 1 | Files successfully pushed to GitHub<br/>GitHubにファイルが正常にプッシュされた |
| **Total** | **10** | |

### Grading Scale / 採点スケール
- **9-10 points:** Excellent - All requirements met or exceeded
  - **9-10点:** 優秀 - すべての要件を満たすまたは超える
- **7-8 points:** Good - Most requirements met with minor issues
  - **7-8点:** 良い - ほとんどの要件を満たすが軽微な問題がある
- **5-6 points:** Satisfactory - Basic requirements met but missing some elements
  - **5-6点:** 満足 - 基本要件を満たすがいくつかの要素が欠けている
- **3-4 points:** Needs Improvement - Significant requirements missing
  - **3-4点:** 改善が必要 - 重要な要件が欠けている
- **0-2 points:** Incomplete - Major requirements not met
  - **0-2点:** 不完全 - 主要な要件が満たされていない

---

## Submission Checklist / 提出チェックリスト

### English

Before submitting, verify:
- ✅ Blender file saved with correct naming: `week01_maze_[yourname].blend`
- ✅ Screenshot saved: `week01_maze_screenshot.png`
- ✅ Both files in correct folder: `game-dev-2025-yourname/week-01/`
- ✅ All maze elements present: floor, walls, start, goal
- ✅ Objects properly named in Outliner
- ✅ Files committed to Git with descriptive message
- ✅ Files pushed to GitHub
- ✅ Verified files visible on GitHub.com

### 日本語

提出前に確認:
- ✅ Blenderファイルが正しい命名で保存：`week01_maze_[yourname].blend`
- ✅ スクリーンショット保存：`week01_maze_screenshot.png`
- ✅ 両方のファイルが正しいフォルダ内：`game-dev-2025-yourname/week-01/`
- ✅ すべての迷路要素が存在：床、壁、スタート、ゴール
- ✅ アウトライナーでオブジェクトが適切に名前付けされている
- ✅ ファイルが説明的なメッセージでGitにコミットされた
- ✅ ファイルがGitHubにプッシュされた
- ✅ GitHub.comでファイルが表示されることを確認

---

## Common Mistakes to Avoid / 避けるべきよくある間違い

### English

1. **Wrong File Location**
   - ❌ Saving to Desktop or Documents instead of GitHub repo
   - ✅ Always save directly in your repository folder

2. **Forgetting to Push to GitHub**
   - ❌ Only committing locally without pushing
   - ✅ Always push and verify on GitHub.com

3. **Unnamed Objects**
   - ❌ Leaving default names like "Cube.001", "Cube.002"
   - ✅ Rename everything descriptively

4. **Too Complex Too Soon**
   - ❌ Trying to add textures, lights, animations
   - ✅ Keep it simple - just geometry for now

5. **No Screenshot**
   - ❌ Forgetting to include the screenshot
   - ✅ Screenshot is required for quick verification

### 日本語

1. **間違ったファイルの場所**
   - ❌ GitHubリポジトリの代わりにデスクトップやドキュメントに保存
   - ✅ 常にリポジトリフォルダに直接保存

2. **GitHubへのプッシュを忘れる**
   - ❌ プッシュせずにローカルでのみコミット
   - ✅ 常にプッシュしてGitHub.comで確認

3. **名前のないオブジェクト**
   - ❌ 「Cube.001」、「Cube.002」のようなデフォルト名のまま
   - ✅ すべてを説明的に名前変更

4. **早すぎる複雑化**
   - ❌ テクスチャ、ライト、アニメーションを追加しようとする
   - ✅ シンプルに保つ - 今はジオメトリだけ

5. **スクリーンショットなし**
   - ❌ スクリーンショットを含めるのを忘れる
   - ✅ スクリーンショットは迅速な確認に必要

---

## Tips for Success / 成功のためのヒント

### English

1. **Start Simple, Iterate**
   - Create basic layout first
   - Add complexity after requirements are met

2. **Save Often**
   - Press Ctrl+S / Cmd+S frequently
   - Blender can crash, don't lose work!

3. **Test Navigation**
   - Mentally "walk through" your maze
   - Make sure there's a clear path from start to goal

4. **Use Reference Views**
   - Switch between Top (NumPad 7), Front (NumPad 1), and Side (NumPad 3) views
   - Helps ensure walls are aligned properly

5. **Experiment!**
   - Try different layouts
   - Undo (Ctrl+Z) is your friend
   - Learning happens through experimentation

### 日本語

1. **シンプルに始めて反復**
   - まず基本レイアウトを作成
   - 要件を満たした後に複雑さを追加

2. **頻繁に保存**
   - Ctrl+S / Cmd+Sを頻繁に押す
   - Blenderはクラッシュする可能性があり、作業を失わないように！

3. **ナビゲーションをテスト**
   - 迷路を頭の中で「歩く」
   - スタートからゴールまでの明確なパスがあることを確認

4. **参照ビューを使用**
   - 上面（NumPad 7）、正面（NumPad 1）、側面（NumPad 3）ビューを切り替え
   - 壁が適切に整列していることを確認するのに役立ちます

5. **実験してください！**
   - 異なるレイアウトを試す
   - 元に戻す（Ctrl+Z）は友達
   - 学習は実験を通じて起こる

---

## Example Maze Ideas / 迷路アイデアの例

### English

**Simple Maze (Meets Requirements):**
```
Start → Straight path → Turn left → Turn right → Goal
With a few dead ends and alternate paths
```

**Medium Maze:**
```
Start → Multiple branching paths →
Some dead ends → Hidden shortcuts → Goal
```

**Advanced Maze (Optional):**
```
Start → Multi-level sections →
Complex branching → Many dead ends →
Multiple routes to goal → Different wall heights
```

### 日本語

**シンプルな迷路（要件を満たす）:**
```
スタート → 直線パス → 左折 → 右折 → ゴール
いくつかの行き止まりと代替パスあり
```

**中級迷路:**
```
スタート → 複数の分岐パス →
いくつかの行き止まり → 隠しショートカット → ゴール
```

**上級迷路（オプション）:**
```
スタート → マルチレベルセクション →
複雑な分岐 → 多くの行き止まり →
ゴールへの複数のルート → 異なる壁の高さ
```

---

## Getting Help / ヘルプを得る

### English

If you're stuck:
1. Review the Week 1 lecture notes and materials
2. Watch the recommended Blender tutorial videos
3. Check the Common Pitfalls section in the lecture plan
4. Ask questions in the course discussion forum
5. Attend office hours
6. Ask a classmate (collaboration on concepts is encouraged!)
7. Email the instructor with:
   - Your GitHub repository link
   - Screenshot of your problem
   - Description of what you've tried

### 日本語

困った場合:
1. 第1週の講義ノートと教材を復習
2. 推奨されるBlenderチュートリアルビデオを視聴
3. 講義計画の「よくある落とし穴」セクションを確認
4. コースディスカッションフォーラムで質問
5. オフィスアワーに出席
6. クラスメートに聞く（概念についてのコラボレーションは推奨されます！）
7. 以下を含めてインストラクターにメール:
   - GitHubリポジトリのリンク
   - 問題のスクリーンショット
   - 試したことの説明

---

## Bonus Challenges (Optional, No Extra Credit) / ボーナスチャレンジ（オプション、追加クレジットなし）

### English

For students who want extra practice:
1. **Create a second, more complex maze**
2. **Add ramps or stairs connecting different levels**
3. **Create a circular or radial maze pattern**
4. **Design a themed maze (castle, dungeon, garden)**
5. **Add decorative elements (pillars, arches, towers)**

These are purely for learning and fun - focus on meeting the basic requirements first!

### 日本語

追加の練習を望む学生向け:
1. **2つ目のより複雑な迷路を作成**
2. **異なるレベルを接続するスロープや階段を追加**
3. **円形または放射状の迷路パターンを作成**
4. **テーマのある迷路をデザイン（城、ダンジョン、庭園）**
5. **装飾要素を追加（柱、アーチ、塔）**

これらは純粋に学習と楽しみのためです - まず基本要件を満たすことに焦点を当ててください！

---

## What's Next: Week 2 Preview / 次は何：第2週プレビュー

### English

In Week 2, you will:
- Learn about materials and textures
- Apply colors and textures to your maze
- Create simple path-based animations
- Introduction to bone rigging basics

Make sure your maze is complete and submitted before Week 2, as we'll be building on this work!

### 日本語

第2週では、以下を行います:
- マテリアルとテクスチャについて学ぶ
- 迷路に色とテクスチャを適用
- シンプルなパスベースのアニメーションを作成
- ボーンリギングの基礎入門

第2週の前に迷路が完成して提出されていることを確認してください。この作業をベースに構築していきます！

---

**Good luck! Have fun creating your maze!**
**がんばってください！迷路作成を楽しんでください！**

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
