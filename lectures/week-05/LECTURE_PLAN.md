# Week 5 Lecture Plan - Ball Maze Game: Maze & Player Controller (100 min)
# 第5週講義計画 - ボール迷路ゲーム：迷路とプレイヤーコントローラー（100分）

**Duration / 期間:** 100 minutes / 100分  
**Developer / 開発者:** Yuri Tijerino

---

## Goals / 目標

### English
- Organize Unity projects with proper folder structure and naming conventions
- Import and optimize Blender mazes for Unity game development
- Create an enhanced ball controller with refined physics and movement
- Implement a smooth camera follow system with damping and offset controls
- Build a goal detection system with particle effects and audio feedback
- Implement game state management for Playing, Won, and Lost states
- Create basic Unity UI with Canvas, Text, and Button components
- Add level restart functionality using SceneManager
- Implement a collectibles/pickups system for additional gameplay
- Playtest and iterate on game feel and balance

### 日本語
- 適切なフォルダ構造と命名規則でUnityプロジェクトを整理する
- Unityゲーム開発のためにBlender迷路をインポートして最適化する
- 洗練された物理とムーブメントを持つ強化されたボールコントローラーを作成する
- ダンピングとオフセットコントロールを備えたスムーズなカメラフォローシステムを実装する
- パーティクルエフェクトとオーディオフィードバックを備えたゴール検出システムを構築する
- Playing、Won、Lostの状態のためのゲーム状態管理を実装する
- Canvas、Text、Buttonコンポーネントを使用して基本的なUnity UIを作成する
- SceneManagerを使用してレベル再起動機能を追加する
- 追加のゲームプレイのために収集物/ピックアップシステムを実装する
- ゲームのフィールとバランスをプレイテストして反復する

---

## Timeline / タイムライン

### Segment 1: Phase 3 Introduction & Project Setup (10 min / 10分)

**English:**
- Welcome to Phase 3: Ball Maze Game (Weeks 5-7)
- Overview of complete ball maze game project
- Project organization best practices in Unity
- Creating proper folder structure: Assets/Scripts, Assets/Prefabs, Assets/Materials, Assets/Scenes
- Naming conventions for scripts, prefabs, and scenes
- Setting up the new Unity project

**日本語:**
- フェーズ3へようこそ：ボール迷路ゲーム（第5-7週）
- 完全なボール迷路ゲームプロジェクトの概要
- Unityでのプロジェクト整理のベストプラクティス
- 適切なフォルダ構造の作成：Assets/Scripts、Assets/Prefabs、Assets/Materials、Assets/Scenes
- スクリプト、プレハブ、シーンの命名規則
- 新しいUnityプロジェクトのセットアップ

---

### Segment 2: Importing and Setting Up the Maze (15 min / 15分)

**English:**
- Exporting maze from Blender as FBX (.fbx)
- Import settings in Unity for optimal performance
- Scaling considerations (Blender units vs Unity units)
- Adding colliders to maze walls (Box Colliders, Mesh Colliders)
- Creating Physics Materials for different surfaces
- Static vs Dynamic objects in Unity physics
- Optimizing maze for performance

**日本語:**
- BlenderからFBX（.fbx）として迷路をエクスポート
- 最適なパフォーマンスのためのUnityのインポート設定
- スケーリングの考慮事項（Blenderユニット vs Unityユニット）
- 迷路の壁にコライダーを追加（Box Colliders、Mesh Colliders）
- 異なる表面のための物理マテリアルの作成
- Unity物理におけるStaticとDynamicオブジェクト
- パフォーマンスのための迷路の最適化

---

### Segment 3: Enhanced Ball Controller (20 min / 20分)

**English:**
- Review of Week 4 basic ball controller
- Adding acceleration and deceleration for smoother movement
- Implementing maximum speed limits
- Adding jump functionality (optional)
- Implementing drag for more realistic physics
- Input smoothing and responsiveness tuning
- Preventing ball from getting stuck on walls
- Physics material setup for the ball

**日本語:**
- 第4週の基本的なボールコントローラーのレビュー
- よりスムーズな移動のための加速と減速の追加
- 最大速度制限の実装
- ジャンプ機能の追加（オプション）
- よりリアルな物理のためのドラッグの実装
- 入力スムージングと応答性のチューニング
- ボールが壁に引っかからないようにする
- ボールの物理マテリアル設定

---

### Segment 4: Advanced Camera Follow System (15 min / 15分)

**English:**
- Review of basic camera following from Week 4
- Implementing smooth camera damping with Lerp
- Setting up camera offset and rotation
- Multiple camera modes: Top-Down, Isometric, Third-Person
- Camera zoom controls (optional)
- Preventing camera from going through walls

**日本語:**
- 第4週の基本的なカメラフォローのレビュー
- Lerpを使用したスムーズなカメラダンピングの実装
- カメラオフセットと回転の設定
- 複数のカメラモード：トップダウン、アイソメトリック、サードパーソン
- カメラズームコントロール（オプション）
- カメラが壁を通過しないようにする

---

### Segment 5: Goal Detection & Win Condition (15 min / 15分)

**English:**
- Creating goal zone with trigger collider
- Implementing OnTriggerEnter for win detection
- Game state management: Playing, Won, Lost
- Creating GameManager script
- Displaying win message
- Scene restart functionality using SceneManager

**日本語:**
- トリガーコライダー付きゴールゾーンの作成
- 勝利検出のためのOnTriggerEnterの実装
- ゲーム状態管理：Playing、Won、Lost
- GameManagerスクリプトの作成
- 勝利メッセージの表示
- SceneManagerを使用したシーン再起動機能

---

### Segment 6: Basic UI System (10 min / 10分)

**English:**
- Unity UI system overview (Canvas, Text, Button)
- Creating UI Canvas
- Adding Text elements (score, win message)
- Creating Restart button
- Implementing button onClick events
- UI layout and positioning

**日本語:**
- Unity UIシステム概要（Canvas、Text、Button）
- UI Canvasの作成
- Text要素の追加（スコア、勝利メッセージ）
- リスタートボタンの作成
- ボタンonClickイベントの実装
- UIレイアウトと配置

---

### Segment 7: Collectibles/Pickups System (10 min / 10分)

**English:**
- Creating collectible prefabs
- Implementing pickup detection with triggers
- Adding score tracking
- Visual feedback for pickups
- Optional: Particle effects

**日本語:**
- 収集可能なプレハブの作成
- トリガーを使用したピックアップ検出の実装
- スコア追跡の追加
- ピックアップの視覚的フィードバック
- オプション：パーティクルエフェクト

---

### Segment 8: Testing & Polish (5 min / 5分)

**English:**
- Playtesting best practices
- Game feel and balance tuning
- Common issues and solutions
- Assignment overview and Q&A

**日本語:**
- プレイテストのベストプラクティス
- ゲームのフィールとバランスの調整
- 一般的な問題と解決策
- 課題概要とQ&A

---

## Materials Needed / 必要な教材

### Software / ソフトウェア
- Unity 2022 LTS
- Week 1 Blender maze project
- Visual Studio or VS Code

### Files Provided / 提供ファイル
- Sample GameManager.cs
- Sample EnhancedBallController.cs
- UI setup guide

---

## Common Pitfalls / よくある落とし穴

### English
1. **Camera following too fast/slow** - Adjust smoothSpeed value
2. **Ball gets stuck on walls** - Check collider sizes and physics materials
3. **Goal trigger not working** - Verify Is Trigger is checked and player has tag
4. **UI not showing** - Check Canvas Render Mode and Camera settings
5. **Game doesn't restart** - Ensure SceneManager.LoadScene includes correct scene name

### 日本語
1. **カメラの追従が速すぎる/遅すぎる** - smoothSpeed値を調整
2. **ボールが壁に引っかかる** - コライダーサイズと物理マテリアルを確認
3. **ゴールトリガーが機能しない** - Is Triggerがチェックされていることとプレイヤーにタグがあることを確認
4. **UIが表示されない** - Canvas Render ModeとCamera設定を確認
5. **ゲームが再起動しない** - SceneManager.LoadSceneに正しいシーン名が含まれていることを確認

---

## Preparation for Next Week / 次週の準備

### English
Students should:
1. Complete Week 5 assignment (playable maze with win condition)
2. Test game thoroughly
3. Review trigger and collision concepts
4. Come prepared with questions

**Next Week Preview:** AI Enemy implementation with NavMesh

### 日本語
学生は以下を行うべきです：
1. 第5週の課題を完了（勝利条件付きのプレイ可能な迷路）
2. ゲームを徹底的にテスト
3. トリガーと衝突の概念を復習
4. 質問を準備して来る

**来週のプレビュー:** NavMeshを使用したAI敵の実装

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**  
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます.**

