# Week 4 Lecture Plan - Unity Physics & Input Systems (100 min)
# 第4週講義計画 - Unity物理システムと入力システム（100分）

**Duration / 期間:** 100 minutes / 100分  
**Developer / 開発者:** Yuri Tijerino

---

## Goals / 目標

### English
- Understand Unity's physics system and how it simulates real-world physics
- Add and configure Rigidbody components for physics-based movement
- Work with different collider types (Box, Sphere, Capsule, Mesh)
- Understand the difference between collision and trigger events
- Implement player input using both legacy Input Manager and new Input System
- Create physics-based player movement scripts
- Implement a camera follow system
- Debug and test physics interactions
- Build a playable ball controller for the maze game

### 日本語
- Unityの物理システムと現実世界の物理シミュレーション方法を理解する
- 物理ベースの移動のためにRigidbodyコンポーネントを追加して設定する
- さまざまなコライダータイプ（Box、Sphere、Capsule、Mesh）を使用する
- 衝突イベントとトリガーイベントの違いを理解する
- レガシーInput Managerと新しいInput Systemの両方を使用してプレイヤー入力を実装する
- 物理ベースのプレイヤー移動スクリプトを作成する
- カメラフォローシステムを実装する
- 物理インタラクションをデバッグしてテストする
- 迷路ゲーム用のプレイ可能なボールコントローラーを構築する

---

## Timeline / タイムライン

### Segment 1: Introduction to Unity Physics System (10 min / 10分)

**English:**
- Review Week 3: Unity interface and GameObjects
- What is a physics engine?
- Unity's built-in physics system (NVIDIA PhysX)
- When to use physics vs kinematic movement
- Real-world examples: gravity, collisions, forces
- Physics timestep and FixedUpdate vs Update

**日本語:**
- 第3週の復習：Unityインターフェースとゲームオブジェクト
- 物理エンジンとは何か？
- Unityの組み込み物理システム（NVIDIA PhysX）
- 物理移動とキネマティック移動を使い分けるタイミング
- 実世界の例：重力、衝突、力
- 物理タイムステップとFixedUpdate vs Update

---

### Segment 2: Rigidbody Component Deep Dive (20 min / 20分)

**English:**
- Adding Rigidbody component
- Key properties:
  - Mass (kg)
  - Drag (air resistance)
  - Angular Drag (rotational resistance)
  - Use Gravity
  - Is Kinematic
  - Interpolate (smooth movement)
  - Collision Detection (Discrete, Continuous, Continuous Dynamic, Continuous Speculative)
- Constraints (Freeze Position/Rotation)
- Live demo: Add Rigidbody to sphere, test gravity

**日本語:**
- Rigidbodyコンポーネントの追加
- 主要プロパティ：
  - Mass（kg）
  - Drag（空気抵抗）
  - Angular Drag（回転抵抗）
  - Use Gravity
  - Is Kinematic
  - Interpolate（スムーズな移動）
  - Collision Detection（Discrete、Continuous、Continuous Dynamic、Continuous Speculative）
- Constraints（位置/回転の固定）
- ライブデモ：球体にRigidbodyを追加、重力をテスト

---

### Segment 3: Colliders and Collision Detection (15 min / 15分)

**English:**
- Collider types: Box, Sphere, Capsule, Mesh, Wheel, Terrain
- When to use each type
- Collider vs Mesh Collider (performance)
- Collider layers and layer collision matrix
- Compound colliders (multiple colliders on one GameObject)
- Live demo: Add colliders to maze walls and floor

**日本語:**
- コライダータイプ：Box、Sphere、Capsule、Mesh、Wheel、Terrain
- それぞれのタイプを使用するタイミング
- Collider vs Mesh Collider（パフォーマンス）
- コライダーレイヤーとレイヤー衝突マトリックス
- 複合コライダー（1つのGameObjectに複数のコライダー）
- ライブデモ：迷路の壁と床にコライダーを追加

---

### Segment 4: Collisions vs Triggers (15 min / 15分)

**English:**
- Physical collisions (Is Trigger = false)
  - OnCollisionEnter, OnCollisionStay, OnCollisionExit
  - Collision detection and physics interactions
- Triggers (Is Trigger = true)
  - OnTriggerEnter, OnTriggerStay, OnTriggerExit
  - Detection without physical interaction
- When to use each
- Demo: Goal detection trigger vs wall collision

**日本語:**
- 物理的衝突（Is Trigger = false）
  - OnCollisionEnter、OnCollisionStay、OnCollisionExit
  - 衝突検出と物理インタラクション
- トリガー（Is Trigger = true）
  - OnTriggerEnter、OnTriggerStay、OnTriggerExit
  - 物理的インタラクションなしの検出
- それぞれを使用するタイミング
- デモ：ゴール検出トリガー vs 壁の衝突

---

### Segment 5: Unity Input System (Old & New) (20 min / 20分)

**English:**
- Two Input Systems:
  1. Legacy Input Manager (Input class)
     - Input.GetKey, Input.GetKeyDown, Input.GetKeyUp
     - Input.GetAxis("Horizontal"), Input.GetAxis("Vertical")
  2. New Input System (Input System package)
     - More flexible, supports gamepads easily
     - Action Maps, Bindings
- Simple movement script using legacy Input
- Getting input in Update() vs FixedUpdate()

**日本語:**
- 2つの入力システム：
  1. レガシーInput Manager（Inputクラス）
     - Input.GetKey、Input.GetKeyDown、Input.GetKeyUp
     - Input.GetAxis("Horizontal")、Input.GetAxis("Vertical")
  2. 新しいInput System（Input Systemパッケージ）
     - より柔軟、ゲームパッドを簡単にサポート
     - Action Maps、Bindings
- レガシーInputを使用したシンプルな移動スクリプト
- Update() vs FixedUpdate()での入力取得

---

### Segment 6: Physics-Based Movement Script (20 min / 20分)

**English:**
- Creating BallController script
- Using Rigidbody.AddForce() for movement
- Force modes: Force, Impulse, Acceleration, VelocityChange
- Reading input and applying forces
- Movement tuning: force magnitude, drag values
- Best practices:
  - Use FixedUpdate() for physics
  - Normalize input vectors
  - Clamp forces to prevent excessive speed

**日本語:**
- BallControllerスクリプトの作成
- 移動にRigidbody.AddForce()を使用
- フォースモード：Force、Impulse、Acceleration、VelocityChange
- 入力の読み取りとフォースの適用
- 移動の調整：フォースの大きさ、ドラッグ値
- ベストプラクティス：
  - 物理にはFixedUpdate()を使用
  - 入力ベクトルを正規化
  - 過度な速度を防ぐためにフォースをクランプ

---

### Segment 7: Camera Follow System (10 min / 10分)

**English:**
- Create CameraFollow script
- Smooth camera following using Vector3.Lerp() or Vector3.SmoothDamp()
- Offset from player position
- Lock camera rotation or allow rotation
- Test camera system with ball movement

**日本語:**
- CameraFollowスクリプトの作成
- Vector3.Lerp()またはVector3.SmoothDamp()を使用したスムーズなカメラフォロー
- プレイヤー位置からのオフセット
- カメラの回転を固定または許可
- ボール移動でカメラシステムをテスト

---

### Segment 8: Testing & Debugging (10 min / 10分)

**English:**
- Testing physics interactions
- Using Gizmos to visualize colliders
- Debug.Log() for collision/trigger events
- Common issues and solutions:
  - Ball falling through floor → Check colliders
  - Jittery movement → Adjust interpolation
  - Too fast/slow → Tune force values
- Assignment overview and Q&A

**日本語:**
- 物理インタラクションのテスト
- Gizmosを使用してコライダーを視覚化
- 衝突/トリガーイベントにDebug.Log()を使用
- 一般的な問題と解決策：
  - ボールが床を通過 → コライダーを確認
  - 不安定な動き → 補間を調整
  - 速すぎる/遅すぎる → フォース値を調整
- 課題概要とQ&A

---

## Materials Needed / 必要な教材

### Software / ソフトウェア
- Unity 2022 LTS installed / Unity 2022 LTSがインストールされている
- Week 3 Unity project / 第3週のUnityプロジェクト
- Visual Studio or VS Code / Visual StudioまたはVS Code

### Files Provided / 提供ファイル
- Sample BallController.cs script / サンプルBallController.csスクリプト
- Sample CameraFollow.cs script / サンプルCameraFollow.csスクリプト
- Physics settings reference / 物理設定リファレンス

---

## Common Pitfalls / よくある落とし穴

### English
1. **Using Update() instead of FixedUpdate() for physics**
   - Problem: Inconsistent physics behavior
   - Solution: Always use FixedUpdate() when modifying Rigidbody

2. **Ball falling through floor**
   - Problem: Missing colliders or colliders too small
   - Solution: Check all colliders, ensure proper sizing

3. **Movement too fast or too slow**
   - Problem: Force values not tuned
   - Solution: Adjust force magnitude and drag values incrementally

4. **Jittery or stuttering movement**
   - Problem: Interpolation not enabled
   - Solution: Enable Interpolate on Rigidbody

5. **Camera lagging behind player**
   - Problem: Lerp smoothing too slow
   - Solution: Increase lerp speed or use SmoothDamp

### 日本語
1. **物理にUpdate()の代わりにFixedUpdate()を使用しない**
   - 問題：一貫性のない物理動作
   - 解決策：Rigidbodyを変更する場合は常にFixedUpdate()を使用

2. **ボールが床を通過する**
   - 問題：コライダーが欠けている、またはコライダーが小さすぎる
   - 解決策：すべてのコライダーを確認し、適切なサイズを確保

3. **移動が速すぎる/遅すぎる**
   - 問題：フォース値が調整されていない
   - 解決策：フォースの大きさとドラッグ値を段階的に調整

4. **不安定またはカクつく動き**
   - 問題：補間が有効になっていない
   - 解決策：RigidbodyでInterpolateを有効にする

5. **カメラがプレイヤーより遅れる**
   - 問題：Lerpスムージングが遅すぎる
   - 解決策：lerp速度を上げるか、SmoothDampを使用

---

## Additional Resources / 追加リソース

### Video Tutorials / ビデオチュートリアル
- Unity Learn - "Physics in Unity"
- Brackeys - "Rigidbody Movement"
- Unity Manual - Physics System

### Documentation / ドキュメント
- Unity Manual - Rigidbody: https://docs.unity3d.com/Manual/class-Rigidbody.html
- Unity Manual - Colliders: https://docs.unity3d.com/Manual/CollidersOverview.html
- Unity Manual - Input System: https://docs.unity3d.com/Packages/com.unity.inputsystem@latest

---

## Preparation for Next Week / 次週の準備

### English
Students should:
1. Complete Week 4 assignment (playable ball maze)
2. Test their ball controller thoroughly
3. Review goal detection concepts
4. Come prepared with questions about physics and input

**Next Week Preview:** Maze setup, goal detection, player ball controller refinement

### 日本語
学生は以下を行うべきです：
1. 第4週の課題を完了（プレイ可能なボール迷路）
2. ボールコントローラーを徹底的にテスト
3. ゴール検出の概念を復習
4. 物理と入力についての質問を準備して来る

**来週のプレビュー:** 迷路のセットアップ、ゴール検出、プレイヤーボールコントローラーの改良

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**  
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます.**

