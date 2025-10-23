# Week 2 Assignment: Textured Maze with Animation
# 第2週課題：アニメーション付きテクスチャ迷路

**Due Date / 提出期限:** Before Week 3 lecture / 第3週講義前
**Points / 配点:** 15 points / 15点
**Developer / 開発者:** Yuri Tijerino

---

## Assignment Overview / 課題概要

### English
Build upon your Week 1 maze by adding materials, textures, and a simple animation. This assignment tests your understanding of Blender's material system, UV unwrapping, texturing workflow, and basic animation principles.

### 日本語
第1週の迷路にマテリアル、テクスチャ、シンプルなアニメーションを追加して構築します。この課題は、Blenderのマテリアルシステム、UV展開、テクスチャリングワークフロー、基本的なアニメーション原理の理解をテストします。

---

## Learning Objectives / 学習目標

### English
By completing this assignment, you will demonstrate your ability to:
1. Apply materials with different properties to 3D objects
2. Perform UV unwrapping on geometric objects
3. Apply image textures to models
4. Create and manage materials in Blender
5. Create simple path-based animations
6. Organize project files and textures
7. Use GitHub for version control with binary and image files

### 日本語
この課題を完了することで、以下の能力を示します：
1. 異なるプロパティを持つマテリアルを3Dオブジェクトに適用
2. 幾何学オブジェクトでUV展開を実行
3. モデルに画像テクスチャを適用
4. Blenderでマテリアルを作成して管理
5. シンプルなパスベースのアニメーションを作成
6. プロジェクトファイルとテクスチャを整理
7. バイナリと画像ファイルのバージョン管理にGitHubを使用

---

## Assignment Requirements / 課題要件

### Part 1: Materials (5 points / 5点)

#### English

Apply materials to your Week 1 maze with the following requirements:

**1. Floor Material (1 point / 1点)**
- Apply a material to the floor
- Color: Green, brown, or gray
- Adjust roughness appropriately (floor should be somewhat matte)
- Name material: "Mat_Floor"

**2. Wall Materials (2 points / 2点)**
- Apply materials to walls
- Color: Gray, brown, or white
- Can use same material for all walls OR
- Different materials for variety
- Name material(s): "Mat_Wall" or "Mat_Wall_01", "Mat_Wall_02", etc.

**3. Goal Material (1 point / 1点)**
- Apply distinct material to goal area
- Color: Bright red, gold, or glowing color
- Should stand out from other elements
- Optional: Add some metallic or emissive properties
- Name material: "Mat_Goal"

**4. Start Area Material (1 point / 1点)**
- Apply material to start area marker
- Color: Blue or contrasting color
- Should be clearly different from goal
- Name material: "Mat_Start"

#### 日本語

以下の要件で第1週の迷路にマテリアルを適用:

**1. 床マテリアル（1点）**
- 床にマテリアルを適用
- 色：緑、茶色、または灰色
- ラフネスを適切に調整（床はややマットにすべき）
- マテリアル名：「Mat_Floor」

**2. 壁マテリアル（2点）**
- 壁にマテリアルを適用
- 色：灰色、茶色、または白
- すべての壁に同じマテリアルを使用できるまたは
- バラエティのために異なるマテリアル
- マテリアル名：「Mat_Wall」または「Mat_Wall_01」、「Mat_Wall_02」など

**3. ゴールマテリアル（1点）**
- ゴールエリアに明確なマテリアルを適用
- 色：明るい赤、金色、または光る色
- 他の要素から目立つべき
- オプション：メタリックまたは発光プロパティを追加
- マテリアル名：「Mat_Goal」

**4. スタートエリアマテリアル（1点）**
- スタートエリアマーカーにマテリアルを適用
- 色：青または対照的な色
- ゴールとは明確に異なるべき
- マテリアル名：「Mat_Start」

---

### Part 2: Texture (5 points / 5点)

#### English

Apply at least ONE image texture to your maze:

**Option A: Wall Texture (Recommended for Beginners)**
- UV unwrap at least one wall section
- Apply brick, stone, or concrete texture
- Ensure texture is not stretched
- Texture should tile reasonably well

**Option B: Floor Texture (Alternative)**
- UV unwrap floor
- Apply grass, dirt, or tile texture
- Adjust UV scale appropriately

**Option C: Multiple Textures (Advanced, Optional)**
- Apply textures to multiple elements
- Floor AND walls textures
- Different textures for variety

**Texture Requirements:**
1. Use at least one image texture (not just solid colors)
2. Texture file must be in your project folder: `week-02/textures/`
3. UV unwrapping must be performed correctly (no extreme stretching)
4. Texture should be visible in Material Preview or Rendered viewport mode

**Texture File Requirements:**
- Format: PNG or JPG
- Resolution: At least 512x512 pixels
- Store in: `game-dev-2025-yourname/week-02/textures/`
- Name descriptively: `brick_texture.jpg`, `stone_wall.png`, etc.

#### 日本語

迷路に少なくとも1つの画像テクスチャを適用:

**オプションA：壁テクスチャ（初心者推奨）**
- 少なくとも1つの壁セクションをUV展開
- レンガ、石、またはコンクリートテクスチャを適用
- テクスチャが引き伸ばされていないことを確認
- テクスチャは合理的にタイリングすべき

**オプションB：床テクスチャ（代替）**
- 床をUV展開
- 草、土、またはタイルテクスチャを適用
- UVスケールを適切に調整

**オプションC：複数テクスチャ（上級、オプション）**
- 複数の要素にテクスチャを適用
- 床と壁のテクスチャ
- バラエティのために異なるテクスチャ

**テクスチャ要件:**
1. 少なくとも1つの画像テクスチャを使用（単色だけでなく）
2. テクスチャファイルはプロジェクトフォルダ内：`week-02/textures/`
3. UV展開は正しく実行される必要があります（極端な引き伸ばしなし）
4. テクスチャはMaterial PreviewまたはRenderedビューポートモードで表示されるべき

**テクスチャファイル要件:**
- フォーマット：PNGまたはJPG
- 解像度：少なくとも512x512ピクセル
- 保存場所：`game-dev-2025-yourname/week-02/textures/`
- 説明的に命名：`brick_texture.jpg`、`stone_wall.png`など

---

### Part 3: Animation (3 points / 3点)

#### English

Create ONE simple animation in your maze scene:

**Animation Options:**

**Option A: Moving Object (Recommended)**
- Add a decorative object (sphere, cube, custom shape)
- Create a path (Bezier curve)
- Animate object following the path
- Duration: 3-5 seconds (90-150 frames at 30fps)
- Example: A ball rolling through part of the maze

**Option B: Rotating Object**
- Add an object above the goal area
- Animate it rotating continuously
- Example: A rotating star or marker above the goal

**Option C: Floating Animation**
- Create object that moves up and down
- Use keyframes for position
- Example: Goal marker that bobs up and down

**Animation Requirements:**
1. Animation must be visible and smooth
2. Length: 90-150 frames (3-5 seconds)
3. Must loop naturally (start and end positions connect)
4. Object must have material applied

#### 日本語

迷路シーンで1つのシンプルなアニメーションを作成:

**アニメーションオプション:**

**オプションA：動くオブジェクト（推奨）**
- 装飾オブジェクト（球体、立方体、カスタム形状）を追加
- パス（ベジェ曲線）を作成
- パスに従うオブジェクトをアニメーション
- 期間：3〜5秒（30fpsで90〜150フレーム）
- 例：迷路の一部を転がるボール

**オプションB：回転オブジェクト**
- ゴールエリアの上にオブジェクトを追加
- 継続的に回転するようアニメーション
- 例：ゴールの上の回転する星またはマーカー

**オプションC：浮遊アニメーション**
- 上下に動くオブジェクトを作成
- 位置のキーフレームを使用
- 例：上下に揺れるゴールマーカー

**アニメーション要件:**
1. アニメーションは目に見えてスムーズである必要があります
2. 長さ：90〜150フレーム（3〜5秒）
3. 自然にループする必要があります（開始と終了位置が接続）
4. オブジェクトにはマテリアルが適用されている必要があります

---

### Part 4: File Organization and Submission (2 points / 2点)

#### English

**File Structure:**
```
game-dev-2025-yourname/
└── week-02/
    ├── textures/
    │   ├── [texture_file_1].jpg/png
    │   └── [texture_file_2].jpg/png (if using multiple)
    ├── week02_textured_maze_[yourname].blend
    ├── week02_materials_screenshot.png
    └── week02_animation_screenshot.png
```

**Required Files:**
1. **Blender File (1 point / 1点)**
   - Name: `week02_textured_maze_[yourname].blend`
   - Must open without errors
   - All textures must be found (use relative paths)

2. **Screenshots (0.5 points / 0.5点)**
   - `week02_materials_screenshot.png` - Shows materials applied (Material Preview mode)
   - `week02_animation_screenshot.png` - Shows animated object at interesting frame

3. **Texture Files (0.5 points / 0.5点)**
   - All texture images in `textures/` folder
   - Files properly named
   - Reasonable file sizes (not huge)

**GitHub Submission:**
- Commit all files with message: "Complete Week 2 textured maze assignment"
- Push to GitHub
- Verify all files visible on GitHub.com

#### 日本語

**ファイル構造:**
```
game-dev-2025-yourname/
└── week-02/
    ├── textures/
    │   ├── [texture_file_1].jpg/png
    │   └── [texture_file_2].jpg/png（複数使用する場合）
    ├── week02_textured_maze_[yourname].blend
    ├── week02_materials_screenshot.png
    └── week02_animation_screenshot.png
```

**必要なファイル:**
1. **Blenderファイル（1点）**
   - 名前：`week02_textured_maze_[yourname].blend`
   - エラーなく開く必要があります
   - すべてのテクスチャが見つかる必要があります（相対パスを使用）

2. **スクリーンショット（0.5点）**
   - `week02_materials_screenshot.png` - 適用されたマテリアルを表示（Material Previewモード）
   - `week02_animation_screenshot.png` - 興味深いフレームでアニメーションオブジェクトを表示

3. **テクスチャファイル（0.5点）**
   - `textures/`フォルダ内のすべてのテクスチャ画像
   - ファイルが適切に命名されている
   - 適切なファイルサイズ（巨大でない）

**GitHub提出:**
- メッセージですべてのファイルをコミット：「Complete Week 2 textured maze assignment」
- GitHubにプッシュ
- GitHub.comですべてのファイルが表示されることを確認

---

## Grading Rubric / 採点基準

### English

| Criteria / 基準 | Points / 点数 | Description / 説明 |
|------------------|---------------|-------------------|
| Floor Material | 1 | Appropriate material applied to floor<br/>床に適切なマテリアルが適用されている |
| Wall Materials | 2 | Materials applied to walls with proper settings<br/>適切な設定で壁にマテリアルが適用されている |
| Goal Material | 1 | Distinctive, visible goal material<br/>特徴的で見える ゴールマテリアル |
| Start Material | 1 | Clear start area material<br/>明確なスタートエリアマテリアル |
| Image Texture | 3 | At least one texture correctly applied with UV unwrapping<br/>UV展開で少なくとも1つのテクスチャが正しく適用されている |
| Texture Quality | 2 | Texture not stretched, appropriate resolution, tiles well<br/>テクスチャが引き伸ばされていない、適切な解像度、よくタイリング |
| Animation | 3 | Smooth animation, appropriate length, loops properly<br/>スムーズなアニメーション、適切な長さ、適切にループ |
| File Organization | 1 | Correct folder structure and file naming<br/>正しいフォルダ構造とファイル命名 |
| GitHub Submission | 1 | All files committed and pushed successfully<br/>すべてのファイルが正常にコミットおよびプッシュされた |
| **Total** | **15** | |

### Grading Scale / 採点スケール
- **14-15 points:** Excellent - All requirements exceeded
  - **14-15点:** 優秀 - すべての要件を超える
- **12-13 points:** Good - All requirements met
  - **12-13点:** 良い - すべての要件を満たす
- **10-11 points:** Satisfactory - Most requirements met
  - **10-11点:** 満足 - ほとんどの要件を満たす
- **7-9 points:** Needs Improvement - Some requirements missing
  - **7-9点:** 改善が必要 - いくつかの要件が欠けている
- **0-6 points:** Incomplete - Major requirements not met
  - **0-6点:** 不完全 - 主要な要件が満たされていない

---

## Step-by-Step Guide / ステップバイステップガイド

### English

**Step 1: Open Your Week 1 Maze**
1. Open Blender
2. File → Open → Navigate to `week-01/week01_maze_[yourname].blend`
3. Immediately Save As → `week-02/week02_textured_maze_[yourname].blend`

**Step 2: Apply Materials**
1. Select floor object
2. Switch to Shading workspace
3. Click "+ New" material
4. Rename material to "Mat_Floor"
5. Choose base color (green/brown/gray)
6. Adjust Roughness to ~0.8
7. Repeat for walls, goal, start area

**Step 3: Add Texture to One Element**
1. Create `textures/` folder in week-02 directory
2. Find/download a texture image (brick, stone, etc.)
3. Save texture to `textures/` folder
4. Select wall object
5. Tab → Edit Mode
6. Select all faces (A key)
7. Mark seams at corners: Select edges, Ctrl+E → Mark Seam
8. U → Unwrap
9. Switch to Shading workspace
10. In Shader Editor: Add → Texture → Image Texture
11. Click folder icon → navigate to texture file
12. Connect Image Texture → Base Color input of Principled BSDF
13. Switch viewport to Material Preview mode

**Step 4: Create Animation**
1. Add object to animate (Shift+A → Mesh → UV Sphere)
2. Position near start of maze
3. Add path: Shift+A → Curve → Bezier Curve
4. Tab (Edit Mode) → Move/shape curve through maze
5. Select animated object
6. Constraints tab → Add → Follow Path
7. Target: Select your curve
8. Check "Follow Curve"
9. Select curve → Object Data Properties
10. Set Frames: 150
11. Test: Press Spacebar to play

**Step 5: Take Screenshots**
1. Switch to Material Preview mode (3rd sphere icon)
2. Frame your scene nicely (NumPad 7 for top view)
3. Image → View Render → Save Image → `week02_materials_screenshot.png`
4. Scrub timeline to interesting animation frame
5. Take second screenshot → `week02_animation_screenshot.png`

**Step 6: Save and Submit**
1. Save Blender file: Ctrl+S / Cmd+S
2. Check file structure:
   - Blender file in week-02/
   - Textures in week-02/textures/
   - Screenshots in week-02/
3. Open GitHub Desktop
4. Commit with message: "Complete Week 2 textured maze assignment"
5. Push to GitHub
6. Verify on GitHub.com

### 日本語

**ステップ1：第1週の迷路を開く**
1. Blenderを開く
2. File → Open → `week-01/week01_maze_[yourname].blend`に移動
3. すぐにSave As → `week-02/week02_textured_maze_[yourname].blend`

**ステップ2：マテリアルを適用**
1. 床オブジェクトを選択
2. Shadingワークスペースに切り替え
3. 「+ New」マテリアルをクリック
4. マテリアルを「Mat_Floor」に名前変更
5. ベースカラーを選択（緑/茶色/灰色）
6. Roughnessを約0.8に調整
7. 壁、ゴール、スタートエリアに繰り返し

**ステップ3：1つの要素にテクスチャを追加**
1. week-02ディレクトリに`textures/`フォルダを作成
2. テクスチャ画像を検索/ダウンロード（レンガ、石など）
3. テクスチャを`textures/`フォルダに保存
4. 壁オブジェクトを選択
5. Tab → 編集モード
6. すべての面を選択（Aキー）
7. 角にシームをマーク：エッジを選択、Ctrl+E → Mark Seam
8. U → Unwrap
9. Shadingワークスペースに切り替え
10. Shader Editorで：Add → Texture → Image Texture
11. フォルダアイコンをクリック → テクスチャファイルに移動
12. Image Textureを接続 → Principled BSDFのBase Color入力
13. ビューポートをMaterial Previewモードに切り替え

**ステップ4：アニメーションを作成**
1. アニメーションするオブジェクトを追加（Shift+A → Mesh → UV Sphere）
2. 迷路の開始近くに配置
3. パスを追加：Shift+A → Curve → Bezier Curve
4. Tab（編集モード） → 迷路を通じて曲線を移動/形成
5. アニメーションオブジェクトを選択
6. Constraintsタブ → Add → Follow Path
7. ターゲット：曲線を選択
8. 「Follow Curve」にチェック
9. 曲線を選択 → Object Data Properties
10. フレームを設定：150
11. テスト：スペースバーを押して再生

**ステップ5：スクリーンショットを撮る**
1. Material Previewモードに切り替え（3番目の球体アイコン）
2. シーンをきれいにフレーム（NumPad 7で上面図）
3. Image → View Render → Save Image → `week02_materials_screenshot.png`
4. 興味深いアニメーションフレームにタイムラインをスクラブ
5. 2番目のスクリーンショットを撮る → `week02_animation_screenshot.png`

**ステップ6：保存して提出**
1. Blenderファイルを保存：Ctrl+S / Cmd+S
2. ファイル構造を確認：
   - Blenderファイルがweek-02/内
   - テクスチャがweek-02/textures/内
   - スクリーンショットがweek-02/内
3. GitHub Desktopを開く
4. メッセージでコミット：「Complete Week 2 textured maze assignment」
5. GitHubにプッシュ
6. GitHub.comで確認

---

## Common Mistakes to Avoid / 避けるべきよくある間違い

### English

1. **Texture File Not Found**
   - ❌ Putting texture files in random locations
   - ✅ Always use `week-02/textures/` folder and relative paths

2. **Stretched Textures**
   - ❌ Forgetting to UV unwrap or marking seams poorly
   - ✅ Properly mark seams and unwrap before applying texture

3. **Animation Doesn't Loop**
   - ❌ Start and end positions are different
   - ✅ Make path curve close to form a loop

4. **Materials Look Black**
   - ❌ Viewing in Solid mode instead of Material Preview
   - ✅ Switch to Material Preview (3rd sphere icon) or Rendered view

5. **File Size Too Large**
   - ❌ Using 4K textures or uncompressed images
   - ✅ Use 1024x1024 or smaller, JPG format for photos

6. **Forgetting to Save Blender File in Week-02 Folder**
   - ❌ Saving in Week-01 or Desktop
   - ✅ Use "Save As" and ensure it's in week-02/

### 日本語

1. **テクスチャファイルが見つからない**
   - ❌ テクスチャファイルをランダムな場所に置く
   - ✅ 常に`week-02/textures/`フォルダと相対パスを使用

2. **引き伸ばされたテクスチャ**
   - ❌ UV展開を忘れる、またはシームを適切にマークしない
   - ✅ テクスチャを適用する前にシームを適切にマークして展開

3. **アニメーションがループしない**
   - ❌ 開始と終了位置が異なる
   - ✅ パス曲線を閉じてループを形成

4. **マテリアルが黒く見える**
   - ❌ Material Previewの代わりにSolidモードで表示
   - ✅ Material Preview（3番目の球体アイコン）またはRenderedビューに切り替え

5. **ファイルサイズが大きすぎる**
   - ❌ 4Kテクスチャまたは非圧縮画像を使用
   - ✅ 1024x1024以下、写真用JPGフォーマットを使用

6. **Week-02フォルダにBlenderファイルを保存するのを忘れる**
   - ❌ Week-01またはデスクトップに保存
   - ✅ 「Save As」を使用してweek-02/内にあることを確認

---

## Free Texture Resources / 無料テクスチャリソース

### English

**Recommended Sites:**
1. **Poly Haven** (https://polyhaven.com/textures)
   - High-quality, CC0 license
   - Variety of materials
   - Includes normal maps and other maps

2. **OpenGameArt.org** (https://opengameart.org/)
   - Game-focused textures
   - Various licenses (check each)
   - Good for beginners

3. **Textures.com** (https://www.textures.com/)
   - Free tier: 15 credits per day
   - High quality
   - Requires account

4. **CC0 Textures** (https://cc0textures.com/)
   - All CC0 (public domain)
   - PBR textures
   - Professional quality

### 日本語

**推奨サイト:**
1. **Poly Haven** (https://polyhaven.com/textures)
   - 高品質、CC0ライセンス
   - さまざまなマテリアル
   - ノーマルマップやその他のマップが含まれる

2. **OpenGameArt.org** (https://opengameart.org/)
   - ゲーム向けテクスチャ
   - 各種ライセンス（それぞれ確認）
   - 初心者に適している

3. **Textures.com** (https://www.textures.com/)
   - 無料ティア：1日15クレジット
   - 高品質
   - アカウントが必要

4. **CC0 Textures** (https://cc0textures.com/)
   - すべてCC0（パブリックドメイン）
   - PBRテクスチャ
   - プロフェッショナルな品質

---

## Bonus Challenges (Optional) / ボーナスチャレンジ（オプション）

### English

For students who want extra practice:
1. **Apply textures to multiple elements** (floor, walls, goal)
2. **Create normal maps** for added detail
3. **Add multiple animated objects**
4. **Create more complex animation path** with loops and turns
5. **Experiment with emissive materials** (glowing goal area)
6. **Add simple lighting** to enhance materials

Remember: Focus on meeting basic requirements first!

### 日本語

追加の練習を望む学生向け:
1. **複数の要素にテクスチャを適用**（床、壁、ゴール）
2. **ノーマルマップを作成** 詳細を追加
3. **複数のアニメーションオブジェクトを追加**
4. **ループとターンのあるより複雑なアニメーションパスを作成**
5. **発光マテリアルを実験**（光るゴールエリア）
6. **シンプルなライティングを追加** マテリアルを強化

覚えておいてください：まず基本要件を満たすことに焦点を当ててください！

---

## Getting Help / ヘルプを得る

### English

If you're stuck:
1. Review Week 2 lecture notes and materials
2. Watch recommended tutorial videos on materials and texturing
3. Check the Common Pitfalls section above
4. Visit free texture sites for inspiration
5. Ask in course discussion forum
6. Attend office hours
7. Compare with classmates (concepts, not copying files)
8. Email instructor with:
   - GitHub repository link
   - Screenshots of issue
   - Description of what you've tried

### 日本語

困った場合:
1. 第2週の講義ノートと教材を復習
2. マテリアルとテクスチャリングに関する推奨チュートリアルビデオを視聴
3. 上記の「よくある落とし穴」セクションを確認
4. インスピレーションのために無料テクスチャサイトを訪問
5. コースディスカッションフォーラムで質問
6. オフィスアワーに出席
7. クラスメートと比較（概念、ファイルのコピーではない）
8. 以下を含めてインストラクターにメール:
   - GitHubリポジトリリンク
   - 問題のスクリーンショット
   - 試したことの説明

---

## What's Next: Week 3 Preview / 次は何：第3週プレビュー

### English

In Week 3, you will:
- Install and set up Unity3D
- Learn Unity's interface and workflow
- Import your Blender maze into Unity
- Set up basic scene with lighting and camera
- Understand GameObjects and Components
- Prepare for adding physics and interactivity

**Important:** Install Unity Hub and Unity 2022 LTS BEFORE Week 3 class. Installation can take time!

### 日本語

第3週では、以下を行います:
- Unity3Dをインストールしてセットアップ
- Unityのインターフェースとワークフローを学ぶ
- Blender迷路をUnityにインポート
- ライティングとカメラで基本シーンをセットアップ
- GameObjectsとComponentsを理解
- 物理演算とインタラクティビティの追加に備える

**重要:** 第3週のクラス前にUnity HubとUnity 2022 LTSをインストールしてください。インストールには時間がかかることがあります！

---

**Good luck with your textured maze!**
**テクスチャ迷路がんばってください！**

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
