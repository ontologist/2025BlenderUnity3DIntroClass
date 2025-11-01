# Week 4 Assignment: Playable Ball Maze Game
# 第4週課題：プレイ可能なボール迷路ゲーム

**Due Date / 提出期限:** Before Week 5 lecture / 第5週講義前  
**Points / 点数:** 15 points / 15点  
**Estimated Time / 推定時間:** 3-4 hours / 3-4時間  
**Submission / 提出:** Via GitHub repository / GitHubリポジトリ経由

---

## Assignment Description / 課題概要

**English:** Build a fully playable ball maze game in Unity using physics-based movement. You will import your Week 1 Blender maze, add physics components, implement player controls, create a camera system, and add goal detection. This assignment combines 3D modeling skills from Blender with Unity's physics and scripting systems.

**日本語:** 物理ベースの移動を使用して、Unityで完全にプレイ可能なボール迷路ゲームを構築します。第1週のBlender迷路をインポートし、物理コンポーネントを追加し、プレイヤーコントロールを実装し、カメラシステムを作成し、ゴール検出を追加します。この課題は、Blenderからの3DモデリングスキルとUnityの物理およびスクリプトシステムを組み合わせます。

---

## Requirements / 要件

### 1. Ball Player with Rigidbody (2 points / 2点)

**English:**
- Create or import a sphere object as the player ball
- Add Rigidbody component with appropriate settings:
  - Mass: 0.5 - 1 kg
  - Drag: 0.5 - 2
  - Use Gravity: Enabled
  - Interpolate: Enabled
  - Collision Detection: Continuous or Continuous Dynamic
- Sphere Collider already attached to sphere primitive
- Tag the ball as "Player"

**日本語:**
- プレイヤーボールとして球体オブジェクトを作成またはインポート
- 適切な設定でRigidbodyコンポーネントを追加：
  - Mass：0.5 - 1 kg
  - Drag：0.5 - 2
  - Use Gravity：有効
  - Interpolate：有効
  - Collision Detection：ContinuousまたはContinuous Dynamic
- Sphere Colliderは球体プリミティブに既に付属
- ボールに「Player」タグを付ける

---

### 2. Maze with Proper Colliders (3 points / 3点)

**English:**
- Import your Week 1 Blender maze as FBX
- Add Box Colliders to all walls (at least 10 wall segments)
- Add Box Collider to floor/ground
- All colliders should have "Is Trigger" unchecked (physical collisions)
- Properly organize maze objects in Hierarchy (use empty GameObjects as groups)
- Optional: Add Physics Material to floor for friction control

**日本語:**
- 第1週のBlender迷路をFBXとしてインポート
- すべての壁にBox Colliderを追加（少なくとも10の壁セグメント）
- 床/地面にBox Colliderを追加
- すべてのコライダーで「Is Trigger」のチェックを外す（物理的衝突）
- Hierarchyで迷路オブジェクトを適切に整理（グループとして空のGameObjectを使用）
- オプション：摩擦制御のためにPhysics Materialを床に追加

---

### 3. Player Movement Script (4 points / 4点)

**English:**
- Create a C# script named `BallController.cs`
- Implement physics-based movement using `AddForce()` in `FixedUpdate()`
- Use `Input.GetAxis()` for smooth input
- Include public variables for moveForce (adjustable in Inspector)
- Movement should respond to WASD or Arrow keys
- Code must be well-commented

**日本語:**
- `BallController.cs`という名前のC#スクリプトを作成
- `FixedUpdate()`で`AddForce()`を使用した物理ベースの移動を実装
- 滑らかな入力のために`Input.GetAxis()`を使用
- moveForce用のpublic変数を含める（Inspectorで調整可能）
- 移動はWASDまたは矢印キーに応答する必要があります
- コードは十分にコメントされ整理されている必要があります

---

### 4. Camera Follow System (3 points / 3点)

**English:**
- Create a C# script named `CameraFollow.cs`
- Attach script to Main Camera
- Implement smooth camera follow using `Vector3.Lerp()` in `LateUpdate()`
- Include public variables for target, offset, and smoothSpeed
- Camera should keep player in view at all times

**日本語:**
- `CameraFollow.cs`という名前のC#スクリプトを作成
- Main Cameraにスクリプトをアタッチ
- `LateUpdate()`で`Vector3.Lerp()`を使用して滑らかなカメラフォローを実装
- target、offset、smoothSpeed用のpublic変数を含める
- カメラは常にプレイヤーを視界に保つ必要があります

---

### 5. Goal Detection with Trigger (2 points / 2点)

**English:**
- Create a goal zone object (Cylinder, Cube, or custom mesh)
- Position at the end of the maze
- Add Collider component with "Is Trigger" checked
- Create a C# script named `GoalTrigger.cs`
- Implement `OnTriggerEnter()` to detect when player reaches goal
- Log success message to Console when goal is reached

**日本語:**
- ゴールゾーンオブジェクトを作成（Cylinder、Cube、またはカスタムメッシュ）
- 迷路の終わりに配置
- 「Is Trigger」をチェックしてColliderコンポーネントを追加
- `GoalTrigger.cs`という名前のC#スクリプトを作成
- プレイヤーがゴールに到達したときを検出するために`OnTriggerEnter()`を実装
- ゴールに到達したときにConsoleに成功メッセージをログ

---

### 6. File Organization (1 point / 1点)

**English:**
- Create Unity project in `week-04/` folder
- Organize scripts in `Assets/Scripts/` folder
- Save main scene as `MazeGame.unity`
- Take a screenshot of gameplay

**日本語:**
- `week-04/`フォルダにUnityプロジェクトを作成
- `Assets/Scripts/`フォルダにスクリプトを整理
- メインシーンを`MazeGame.unity`として保存
- ゲームプレイのスクリーンショットを撮る

---

## Submission Checklist / 提出チェックリスト

- ✅ Ball with Rigidbody properly configured
- ✅ Maze imported with colliders on walls and floor
- ✅ BallController.cs script working
- ✅ CameraFollow.cs script working
- ✅ GoalTrigger.cs script working
- ✅ Scene saved and organized
- ✅ Screenshot taken
- ✅ Project committed and pushed to GitHub

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**  
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます.**

