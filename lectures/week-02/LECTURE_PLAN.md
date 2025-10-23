# Week 2: Materials, Textures, and Simple Animations
# 第2週：マテリアル、テクスチャ、シンプルなアニメーション

**Duration / 期間:** 100 minutes / 100分
**Developer / 開発者:** Yuri Tijerino

---

## Lecture Objectives / 講義目標

### English
By the end of this lecture, students will be able to:
1. Understand materials and shaders in Blender
2. Apply colors and materials to 3D objects
3. Perform basic UV unwrapping
4. Apply image textures to models
5. Create simple path-based animations
6. Understand basic bone rigging concepts
7. Export textured models for use in Unity

### 日本語
この講義の終了までに、学生は以下ができるようになります：
1. Blenderのマテリアルとシェーダーを理解する
2. 3Dオブジェクトに色とマテリアルを適用する
3. 基本的なUV展開を実行する
4. モデルに画像テクスチャを適用する
5. シンプルなパスベースのアニメーションを作成する
6. 基本的なボーンリギングの概念を理解する
7. テクスチャ付きモデルをUnity用にエクスポートする

---

## Lecture Timeline / 講義タイムライン

### Segment 1: Review Week 1 and Q&A (10 minutes / 10分)
**English:**
- Quick review of navigation and modeling basics
- Showcase interesting student maze designs
- Address common issues from Week 1
- Collect Week 1 assignments

**日本語:**
- ナビゲーションとモデリングの基礎の簡単な復習
- 興味深い学生の迷路デザインを紹介
- 第1週の一般的な問題に対処
- 第1週の課題を収集

---

### Segment 2: Introduction to Materials (15 minutes / 15分)

#### English

**What are Materials?**
- Materials define how surfaces appear (color, shininess, transparency)
- In 3D graphics: Materials + Lighting = Final Appearance
- Blender uses a node-based shader system (Shader Editor)

**Material Properties:**
- Base Color
- Metallic vs Non-Metallic
- Roughness (shiny vs matte)
- Alpha (transparency)

**Shader Editor Overview:**
- Switching to Shading workspace
- Understanding nodes and connections
- Principled BSDF shader (industry standard)
- Material Output node

#### 日本語

**マテリアルとは何か？**
- マテリアルは表面の見え方を定義（色、光沢、透明度）
- 3Dグラフィックスでは：マテリアル + ライティング = 最終的な見た目
- Blenderはノードベースのシェーダーシステムを使用（Shader Editor）

**マテリアルプロパティ:**
- ベースカラー
- メタリックvs非メタリック
- ラフネス（光沢vsマット）
- アルファ（透明度）

**Shader Editor概要:**
- Shadingワークスペースへの切り替え
- ノードと接続の理解
- Principled BSDFシェーダー（業界標準）
- Material Outputノード

**Key Activities / 主な活動:**
- **Live Demo:** Add material to Week 1 maze
- **ライブデモ:** 第1週の迷路にマテリアルを追加
- Change floor color to green
- 床の色を緑に変更
- Change walls to gray
- 壁を灰色に変更
- Make goal area red
- ゴールエリアを赤に変更

---

### Segment 3: Applying Materials (20 minutes / 20分)

#### English

**Step-by-Step Process:**

1. **Select Object**
   - Click object in viewport or outliner

2. **Add Material**
   - Switch to Shading workspace (top menu)
   - Properties panel → Material Properties (sphere icon)
   - Click "+ New" to add material

3. **Adjust Properties**
   - Click on Base Color → Choose color
   - Adjust Metallic (0 = non-metal, 1 = metal)
   - Adjust Roughness (0 = mirror, 1 = matte)

4. **See Results**
   - Change viewport shading to Material Preview (3rd sphere icon top right)
   - Or Rendered view (4th sphere icon)

**Material Management:**
- Naming materials descriptively
- Reusing materials on multiple objects
- Material slots for multi-material objects

#### 日本語

**ステップバイステッププロセス:**

1. **オブジェクトを選択**
   - ビューポートまたはアウトライナーでオブジェクトをクリック

2. **マテリアルを追加**
   - Shadingワークスペースに切り替え（上部メニュー）
   - プロパティパネル → Material Properties（球体アイコン）
   - 「+ New」をクリックしてマテリアルを追加

3. **プロパティを調整**
   - Base Colorをクリック → 色を選択
   - Metallic調整（0 = 非金属、1 = 金属）
   - Roughness調整（0 = 鏡面、1 = マット）

4. **結果を確認**
   - ビューポートシェーディングをMaterial Previewに変更（右上3番目の球体アイコン）
   - またはRenderedビュー（4番目の球体アイコン）

**マテリアル管理:**
- マテリアルを説明的に命名
- 複数のオブジェクトでマテリアルを再利用
- マルチマテリアルオブジェクトのためのマテリアルスロット

**Key Activities / 主な活動:**
- **Practice Exercise:** Students apply materials to their mazes
- **練習問題:** 学生が迷路にマテリアルを適用
  - Floor: Green or brown (grass/dirt)
  - 床：緑または茶色（草/土）
  - Walls: Gray stone or brick-like
  - 壁：灰色の石またはレンガ風
  - Goal: Bright red or gold
  - ゴール：明るい赤または金色
  - Start area: Blue
  - スタートエリア：青

---

### Segment 4: Introduction to UV Unwrapping and Textures (20 minutes / 20分)

#### English

**What is UV Unwrapping?**
- UV = 2D coordinates (U and V axes, like X and Y)
- Unwrapping = "Unfolding" 3D model into 2D space
- Why? To apply 2D images (textures) onto 3D surfaces
- Like wrapping paper on a gift box

**UV Unwrapping Basics:**

1. **Enter Edit Mode** (Tab)
2. **Select Faces** to unwrap
3. **Mark Seams** (Ctrl+E → Mark Seam)
   - Where the "cuts" will be made to unfold
4. **Unwrap** (U → Unwrap)
5. **View UV Layout** in UV Editor

**Applying Image Textures:**

1. **Get Texture Image**
   - Free sources: textures.com, OpenGameArt.org
   - Or create simple texture in image editor

2. **Add Texture to Material**
   - In Shader Editor
   - Add → Texture → Image Texture
   - Connect to Base Color
   - Open/load image file

3. **Adjust UVs if needed**
   - Scale, rotate in UV Editor

#### 日本語

**UV展開とは何か？**
- UV = 2D座標（UとV軸、XとYのような）
- 展開 = 3Dモデルを2D空間に「展開」
- なぜ？2D画像（テクスチャ）を3D表面に適用するため
- ギフトボックスの包装紙のようなもの

**UV展開の基礎:**

1. **編集モードに入る**（Tab）
2. **展開する面を選択**
3. **シームをマーク**（Ctrl+E → Mark Seam）
   - 「カット」が展開のために行われる場所
4. **展開**（U → Unwrap）
5. **UV Editor でUVレイアウトを表示**

**画像テクスチャの適用:**

1. **テクスチャ画像を取得**
   - 無料ソース：textures.com、OpenGameArt.org
   - または画像エディタでシンプルなテクスチャを作成

2. **マテリアルにテクスチャを追加**
   - Shader Editorで
   - Add → Texture → Image Texture
   - Base Colorに接続
   - 画像ファイルを開く/読み込む

3. **必要に応じてUVを調整**
   - UV Editorでスケール、回転

**Key Activities / 主な活動:**
- **Live Demo:** Apply brick texture to one wall
- **ライブデモ:** 1つの壁にレンガテクスチャを適用
- Show seam marking and unwrapping
- シームマーキングと展開を表示
- **Simple Exercise:** Students apply one texture to their maze
- **シンプルな練習:** 学生が迷路に1つのテクスチャを適用

---

### Segment 5: Path-Based Animation (20 minutes / 20分)

#### English

**What is Animation?**
- Creating movement over time
- Path animation: Object follows a curve/path
- Frame-based: 24-30 frames per second typical

**Creating a Path Animation:**

1. **Create a Path**
   - Add → Curve → Bezier Curve
   - Edit Mode → Move control points to shape path
   - Can create circular, straight, or complex paths

2. **Create Object to Animate**
   - Add simple object (sphere, cube, etc.)

3. **Add Follow Path Constraint**
   - Select object
   - Constraints tab (chain icon)
   - Add → Relationship → Follow Path
   - Target: Select the path curve
   - Check "Follow Curve"

4. **Animate Along Path**
   - Select path curve
   - Object Data Properties → Path Animation
   - Set number of frames
   - Play animation (Spacebar)

**Timeline and Keyframes:**
- Timeline at bottom of screen
- Scrubbing: Drag playhead to see animation
- Setting frame range (start/end)
- Playback controls

#### 日本語

**アニメーションとは何か？**
- 時間の経過とともに動きを作成
- パスアニメーション：オブジェクトが曲線/パスに従う
- フレームベース：通常24-30フレーム/秒

**パスアニメーションの作成:**

1. **パスを作成**
   - Add → Curve → Bezier Curve
   - 編集モード → コントロールポイントを移動してパスを形成
   - 円形、直線、または複雑なパスを作成可能

2. **アニメーションするオブジェクトを作成**
   - シンプルなオブジェクトを追加（球体、立方体など）

3. **Follow Path制約を追加**
   - オブジェクトを選択
   - Constraintsタブ（チェーンアイコン）
   - Add → Relationship → Follow Path
   - ターゲット：パス曲線を選択
   - 「Follow Curve」にチェック

4. **パスに沿ってアニメーション**
   - パス曲線を選択
   - Object Data Properties → Path Animation
   - フレーム数を設定
   - アニメーションを再生（スペースバー）

**タイムラインとキーフレーム:**
- 画面下部のタイムライン
- スクラビング：プレイヘッドをドラッグしてアニメーションを確認
- フレーム範囲の設定（開始/終了）
- 再生コントロール

**Key Activities / 主な活動:**
- **Live Demo:** Create animated sphere moving through maze
- **ライブデモ:** 迷路を通過するアニメーション球体を作成
- Students create one simple path animation
- 学生が1つのシンプルなパスアニメーションを作成

---

### Segment 6: Introduction to Bone Rigging (10 minutes / 10分)

#### English

**What is Rigging?**
- Skeleton system for animating characters/objects
- Bones (armature) control mesh deformation
- Essential for character animation

**Basic Armature:**

1. **Add Armature**
   - Add → Armature → Single Bone
   - Appears as simple bone

2. **Edit Armature in Edit Mode**
   - Tab → Edit Mode
   - Can move head and tail of bone
   - Extrude (E) to add connected bones

3. **Parent Mesh to Armature (Skinning)**
   - Select mesh, then select armature (Shift+Click)
   - Ctrl+P → With Automatic Weights
   - Now bones control mesh

4. **Pose Mode**
   - Select armature
   - Change to Pose Mode (Ctrl+Tab or mode menu)
   - Rotate/move bones to pose character
   - Mesh deforms with bones

**Note:** This is just an introduction. We'll use pre-rigged characters later.

#### 日本語

**リギングとは何か？**
- キャラクター/オブジェクトをアニメーションするための骨格システム
- ボーン（アーマチュア）がメッシュの変形を制御
- キャラクターアニメーションに不可欠

**基本的なアーマチュア:**

1. **アーマチュアを追加**
   - Add → Armature → Single Bone
   - シンプルなボーンとして表示

2. **編集モードでアーマチュアを編集**
   - Tab → 編集モード
   - ボーンのヘッドとテールを移動可能
   - 押し出し（E）で接続されたボーンを追加

3. **メッシュをアーマチュアに親子付け（スキニング）**
   - メッシュを選択、次にアーマチュアを選択（Shift+クリック）
   - Ctrl+P → With Automatic Weights
   - これでボーンがメッシュを制御

4. **ポーズモード**
   - アーマチュアを選択
   - ポーズモードに変更（Ctrl+Tabまたはモードメニュー）
   - ボーンを回転/移動してキャラクターをポーズ
   - メッシュがボーンとともに変形

**注意:** これは単なる入門です。後でリグ済みキャラクターを使用します。

**Key Activities / 主な活動:**
- **Live Demo:** Simple 2-bone armature controlling a cylinder
- **ライブデモ:** シリンダーを制御する2ボーンのシンプルなアーマチュア
- Students observe only (rigging is complex for beginners)
- 学生は観察のみ（リギングは初心者には複雑）

---

### Segment 7: Exporting for Unity (5 minutes / 5分)

#### English

**Export Settings:**
- File → Export → FBX (.fbx)
- FBX is Unity's preferred format
- Check "Selected Objects" if exporting specific items
- Apply modifiers
- Include textures (embed or place in same folder)

**Export Checklist:**
- Materials applied
- Textures saved in project folder
- Objects properly named
- Scale: Unity uses 1 unit = 1 meter

**Note:** We'll actually use exports next week in Unity.

#### 日本語

**エクスポート設定:**
- File → Export → FBX（.fbx）
- FBXはUnityの推奨フォーマット
- 特定のアイテムをエクスポートする場合は「Selected Objects」にチェック
- モディファイアを適用
- テクスチャを含める（埋め込みまたは同じフォルダに配置）

**エクスポートチェックリスト:**
- マテリアルが適用されている
- テクスチャがプロジェクトフォルダに保存されている
- オブジェクトが適切に名前付けされている
- スケール：Unityは1ユニット = 1メートルを使用

**注意:** 実際のエクスポートは来週Unityで使用します。

---

## Expected Outcomes / 期待される成果

### English
Students should be able to:
1. Add and configure materials in Blender
2. Apply colors to 3D objects
3. Understand the difference between materials and textures
4. Perform basic UV unwrapping
5. Apply at least one image texture to a model
6. Create a simple path animation
7. Understand basic concepts of bone rigging
8. Know how to export models for Unity

### 日本語
学生は以下ができるようになります：
1. Blenderでマテリアルを追加して設定
2. 3Dオブジェクトに色を適用
3. マテリアルとテクスチャの違いを理解
4. 基本的なUV展開を実行
5. モデルに少なくとも1つの画像テクスチャを適用
6. シンプルなパスアニメーションを作成
7. ボーンリギングの基本概念を理解
8. Unity用にモデルをエクスポートする方法を知る

---

## Materials Needed / 必要な教材

### Software / ソフトウェア
- Blender 4.0+ / Blender 4.0以降
- Week 1 maze project / 第1週の迷路プロジェクト
- Image editing software (optional): GIMP, Photoshop, Paint.NET
  - 画像編集ソフトウェア（オプション）：GIMP、Photoshop、Paint.NET

### Files Provided / 提供ファイル
- Sample texture images (brick, stone, grass) / サンプルテクスチャ画像（レンガ、石、草）
- Material presets file / マテリアルプリセットファイル
- Example animated scene (.blend) / アニメーションシーンの例（.blend）
- UV unwrapping reference guide / UV展開リファレンスガイド

---

## Common Pitfalls / よくある落とし穴

### English

1. **Materials Not Showing**
   - **Problem:** Material is black or not visible
   - **Solution:** Check viewport shading mode (use Material Preview or Rendered view)

2. **Texture Appears Stretched or Wrong**
   - **Problem:** UV mapping not done correctly
   - **Solution:** Re-unwrap with proper seams

3. **Too Many Seams**
   - **Problem:** UV layout is fragmented
   - **Solution:** Use fewer seams, only where necessary (sharp corners, breaks)

4. **Texture File Not Found**
   - **Problem:** Red/pink missing texture
   - **Solution:** Keep texture images in project folder, use relative paths

5. **Animation Not Playing**
   - **Problem:** Timeline doesn't show movement
   - **Solution:** Check frame range, ensure constraint is properly set

6. **Bones Don't Affect Mesh**
   - **Problem:** Mesh doesn't move with bones
   - **Solution:** Check parenting (Ctrl+P → With Automatic Weights)

### 日本語

1. **マテリアルが表示されない**
   - **問題:** マテリアルが黒または見えない
   - **解決策:** ビューポートシェーディングモードを確認（Material PreviewまたはRenderedビューを使用）

2. **テクスチャが引き伸ばされるまたは間違っている**
   - **問題:** UVマッピングが正しく行われていない
   - **解決策:** 適切なシームで再展開

3. **シームが多すぎる**
   - **問題:** UVレイアウトが断片化されている
   - **解決策:** 必要な場所（鋭い角、切れ目）でのみ少ないシームを使用

4. **テクスチャファイルが見つからない**
   - **問題:** 赤/ピンクの欠けテクスチャ
   - **解決策:** テクスチャ画像をプロジェクトフォルダに保存、相対パスを使用

5. **アニメーションが再生されない**
   - **問題:** タイムラインが動きを表示しない
   - **解決策:** フレーム範囲を確認、制約が適切に設定されているか確認

6. **ボーンがメッシュに影響しない**
   - **問題:** メッシュがボーンと一緒に動かない
   - **解決策:** 親子付けを確認（Ctrl+P → With Automatic Weights）

---

## Frequently Asked Questions / よくある質問

### English

**Q1: Do I need to texture everything in my maze?**
A1: No, the assignment requires texturing at least one element. You can use solid colors (materials) for most objects and add one texture for practice.

**Q2: Where can I find free textures?**
A2: Good free sources include:
- textures.com (some free)
- OpenGameArt.org
- Poly Haven (polyhaven.com)
- Create your own in image editor

**Q3: My texture looks blurry. What's wrong?**
A3: The image resolution might be too low. Try using at least 512x512 pixel images, preferably 1024x1024 or higher.

**Q4: Can I use photos as textures?**
A4: Yes! Photos of walls, floors, etc. can work. Best if:
- Taken straight-on (not at angle)
- Good lighting
- Seamless if possible (edges match)

**Q5: Do I need to animate my maze?**
A5: The Week 2 assignment requires one simple animation. It can be a decorative object moving, not the maze itself.

**Q6: How long should my animation be?**
A6: 3-5 seconds (90-150 frames at 30fps) is sufficient.

### 日本語

**Q1: 迷路のすべてにテクスチャを付ける必要がありますか？**
A1: いいえ、課題では少なくとも1つの要素にテクスチャを付けることを要求しています。ほとんどのオブジェクトには単色（マテリアル）を使用し、練習のために1つのテクスチャを追加できます。

**Q2: 無料のテクスチャはどこで見つけられますか？**
A2: 良い無料ソースには以下があります：
- textures.com（一部無料）
- OpenGameArt.org
- Poly Haven（polyhaven.com）
- 画像エディタで自作

**Q3: テクスチャがぼやけて見えます。何が問題ですか？**
A3: 画像解像度が低すぎる可能性があります。少なくとも512x512ピクセルの画像、できれば1024x1024以上を使用してみてください。

**Q4: 写真をテクスチャとして使用できますか？**
A4: はい！壁、床などの写真は機能します。以下の場合が最適：
- まっすぐ撮影（角度なし）
- 良い照明
- 可能であればシームレス（エッジが一致）

**Q5: 迷路をアニメーションする必要がありますか？**
A5: 第2週の課題では1つのシンプルなアニメーションが必要です。迷路自体ではなく、装飾オブジェクトが動くことができます。

**Q6: アニメーションの長さはどれくらいにすべきですか？**
A6: 3〜5秒（30fpsで90〜150フレーム）で十分です。

---

## Additional Resources / 追加リソース

### Video Tutorials / ビデオチュートリアル

**English Resources:**
- Blender Guru - "Understanding Materials and Shading"
- Grant Abbitt - "Beginner UV Unwrapping Guide"
- CG Cookie - "Introduction to Texturing"
- Blender Official - "Animation Fundamentals"

**Japanese Resources / 日本語リソース:**
- Blender Japan - マテリアル入門
- CGrad - UV展開チュートリアル
- 3D人 - テクスチャリング基礎

### Free Texture Resources / 無料テクスチャリソース
- Poly Haven: https://polyhaven.com/textures
- OpenGameArt.org: https://opengameart.org/
- Textures.com (limited free): https://www.textures.com/
- CC0 Textures: https://cc0textures.com/

### Documentation / ドキュメント
- Blender Manual - Materials: https://docs.blender.org/manual/en/latest/render/materials/
- Blender Manual - UV Mapping: https://docs.blender.org/manual/en/latest/modeling/meshes/uv/
- Blender Manual - Animation: https://docs.blender.org/manual/en/latest/animation/

---

## Preparation for Next Week / 次週の準備

### English
Students should:
1. Complete Week 2 assignment (textured maze with animation)
2. Install Unity Hub and Unity 2022 LTS
3. Watch introductory Unity videos (links provided)
4. Ensure GitHub repository is up to date
5. Bring questions about Blender basics

**Next Week Preview:** Unity3D introduction, importing assets, basic scene setup

### 日本語
学生は以下を行うべきです：
1. 第2週の課題を完了（アニメーション付きテクスチャ迷路）
2. Unity HubとUnity 2022 LTSをインストール
3. 入門Unityビデオを視聴（リンク提供）
4. GitHubリポジトリが最新であることを確認
5. Blender基礎についての質問を準備

**来週のプレビュー:** Unity3D入門、アセットのインポート、基本シーンセットアップ

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます.**
