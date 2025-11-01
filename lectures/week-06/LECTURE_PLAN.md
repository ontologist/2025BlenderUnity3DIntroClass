# Week 6 Lecture Plan - AI Enemy Implementation (100 min)
# 第6週講義計画 - AI敵ボールの実装（100分）

**Duration / 期間:** 100 minutes / 100分  
**Developer / 開発者:** Yuri Tijerino

---

## Goals / 目標

### English
- Understand AI navigation concepts and NavMesh in Unity
- Set up NavMesh for enemy pathfinding
- Create enemy ball GameObjects with AI behavior
- Implement basic chase behavior using NavMeshAgent
- Add player detection and pursuit logic
- Implement collision detection for game over conditions
- Create enemy spawner system
- Test and balance enemy difficulty

### 日本語
- AIナビゲーションの概念とUnityのNavMeshを理解する
- 敵の経路探索のためにNavMeshをセットアップする
- AI動作を持つ敵ボールGameObjectを作成する
- NavMeshAgentを使用して基本的な追跡動作を実装する
- プレイヤーの検出と追跡ロジックを追加する
- ゲームオーバー条件のための衝突検出を実装する
- 敵スポナーシステムを作成する
- 敵の難易度をテストしてバランスを取る

---

## Timeline / タイムライン

### Segment 1: Introduction to AI Navigation (15 min / 15分)

**English:**
- What is AI in games?
- Understanding NavMesh (Navigation Mesh)
- When to use NavMesh vs other AI methods
- Setting up NavMesh in Unity
- NavMesh baking process
- Visualizing NavMesh in Scene view

**日本語:**
- ゲームにおけるAIとは何か？
- NavMesh（ナビゲーションメッシュ）の理解
- NavMeshとその他のAI手法を使い分ける
- UnityでNavMeshをセットアップする
- NavMeshのベイク処理
- SceneビューでNavMeshを視覚化する

**Key Concepts / 主要概念:**
- Static vs Dynamic obstacles
- NavMesh Agents
- Navigation Areas

---

### Segment 2: Setting Up NavMesh for the Maze (15 min / 15分)

**English:**
- Marking walkable surfaces (Navigation Static)
- Excluding walls and obstacles
- Baking the NavMesh
- Adjusting NavMesh agent radius and height
- Setting up NavMesh areas (Walkable, Jump, Not Walkable)
- Testing NavMesh with manual agent placement

**日本語:**
- 歩行可能な表面をマーク（Navigation Static）
- 壁と障害物を除外
- NavMeshのベイク
- NavMeshエージェントの半径と高さの調整
- NavMeshエリアの設定（Walkable、Jump、Not Walkable）
- 手動エージェント配置でNavMeshをテストする

**Hands-On Activity / 実践活動:**
- Students bake NavMesh for their maze
- Verify walkable areas are correctly identified

---

### Segment 3: Creating Enemy Ball GameObject (15 min / 15分)

**English:**
- Creating enemy ball prefab
- Setting up Rigidbody component
- Adding NavMeshAgent component
- Configuring NavMeshAgent parameters:
  - Speed, Angular Speed, Acceleration
  - Stopping Distance
  - Obstacle Avoidance
  - Agent Size (Radius, Height)
- Creating enemy material (red or contrasting color)
- Setting up enemy layer for collision detection

**日本語:**
- 敵ボールプレハブの作成
- Rigidbodyコンポーネントのセットアップ
- NavMeshAgentコンポーネントの追加
- NavMeshAgentパラメータの設定：
  - 速度、角速度、加速度
  - 停止距離
  - 障害物回避
  - エージェントサイズ（半径、高さ）
- 敵のマテリアルの作成（赤または対照的な色）
- 衝突検出のための敵レイヤーの設定

**Hands-On Activity / 実践活動:**
- Students create their first enemy ball
- Test basic NavMeshAgent movement

---

### Segment 4: Basic Chase Behavior Script (25 min / 25分)

**English:**
- Creating EnemyController script
- Understanding NavMeshAgent.SetDestination()
- Finding the player GameObject
- Setting destination to player position
- Updating destination every frame (FixedUpdate)
- Handling player position updates
- Adding visual debug lines (optional)

**日本語:**
- EnemyControllerスクリプトの作成
- NavMeshAgent.SetDestination()の理解
- プレイヤーGameObjectの検索
- プレイヤーの位置を目的地に設定
- 毎フレーム目的地を更新（FixedUpdate）
- プレイヤー位置の更新を処理
- ビジュアルデバッグラインの追加（オプション）

**Code Example / コード例:**
```csharp
public class EnemyController : MonoBehaviour
{
    private NavMeshAgent agent;
    private Transform player;
    
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }
    
    void FixedUpdate()
    {
        if (player != null)
        {
            agent.SetDestination(player.position);
        }
    }
}
```

---

### Segment 5: Player Detection and Pursuit Logic (15 min / 15分)

**English:**
- Adding detection range (sphere cast or distance check)
- Only chasing when player is in range
- Implementing pursuit behavior
- Adding escape behavior when player moves away
- Smoothing enemy movement
- Handling edge cases (player destroyed, enemy stuck)

**日本語:**
- 検出範囲の追加（スフィアキャストまたは距離チェック）
- プレイヤーが範囲内の時のみ追跡
- 追跡動作の実装
- プレイヤーが離れたときの逃走動作を追加
- 敵の動きをスムーズにする
- エッジケースの処理（プレイヤー破壊、敵の詰まり）

**Enhanced Code / 強化されたコード:**
```csharp
public float detectionRange = 10f;
public float chaseRange = 15f;

void FixedUpdate()
{
    float distanceToPlayer = Vector3.Distance(transform.position, player.position);
    
    if (distanceToPlayer <= detectionRange)
    {
        agent.SetDestination(player.position);
    }
    else if (distanceToPlayer > chaseRange)
    {
        agent.ResetPath(); // Stop chasing
    }
}
```

---

### Segment 6: Collision Detection for Game Over (10 min / 10分)

**English:**
- Using OnTriggerEnter for collision detection
- Tagging player ball with "Player" tag
- Detecting when enemy touches player
- Implementing game over logic
- Adding visual feedback (particle effect, screen flash)
- Integration with GameManager from Week 5

**日本語:**
- 衝突検出にOnTriggerEnterを使用
- プレイヤーボールに"Player"タグを付ける
- 敵がプレイヤーに触れたときを検出
- ゲームオーバーロジックの実装
- ビジュアルフィードバックの追加（パーティクルエフェクト、画面フラッシュ）
- 第5週のGameManagerとの統合

**Code Example / コード例:**
```csharp
void OnTriggerEnter(Collider other)
{
    if (other.CompareTag("Player"))
    {
        // Game Over!
        GameManager.Instance.GameOver();
    }
}
```

---

### Segment 7: Enemy Spawner System (5 min / 5分)

**English:**
- Creating EnemySpawner script
- Spawning enemies at specific locations
- Spawning enemies over time
- Limiting maximum enemy count
- Spawning enemies at random locations

**日本語:**
- EnemySpawnerスクリプトの作成
- 特定の位置で敵をスポーン
- 時間をかけて敵をスポーン
- 最大敵数の制限
- ランダムな位置で敵をスポーン

---

## Materials Needed / 必要な教材

### Software / ソフトウェア
- Unity 2022 LTS with Navigation package
- Project from Week 5 (maze with player ball)

### Resources / リソース
- Unity Navigation Documentation: https://docs.unity3d.com/Manual/nav-BuildingNavMesh.html
- NavMeshAgent API: https://docs.unity3d.com/ScriptReference/AI.NavMeshAgent.html

---

## Common Pitfalls / よくある落とし穴

### English
1. **Forgetting to bake NavMesh:** Enemy won't move if NavMesh isn't baked
2. **Wrong agent size:** Enemy might get stuck if radius/height too large
3. **Not updating destination:** Enemy stops chasing if destination isn't updated
4. **Collision detection issues:** Use triggers, not regular colliders
5. **Performance:** Too many enemies updating every frame can cause lag

### 日本語
1. **NavMeshのベイクを忘れる:** NavMeshがベイクされていないと敵が動かない
2. **間違ったエージェントサイズ:** 半径/高さが大きすぎると敵が詰まる
3. **目的地を更新しない:** 目的地が更新されないと敵が追跡をやめる
4. **衝突検出の問題:** 通常のコライダーではなく、トリガーを使用する
5. **パフォーマンス:** 毎フレーム更新する敵が多すぎると遅延の原因になる

---

## FAQs / よくある質問

### English

**Q: Why isn't my enemy moving?**
A: Check that NavMesh is baked, enemy has NavMeshAgent component, and agent is on NavMesh surface.

**Q: Enemy is getting stuck on walls?**
A: Reduce NavMeshAgent radius or increase obstacle avoidance quality.

**Q: How do I make enemies spawn randomly?**
A: Use Random.insideUnitSphere or place spawn points and pick randomly.

**Q: Can I use multiple NavMeshes?**
A: Yes, use NavMeshComponents package for multiple surfaces.

### 日本語

**Q: 敵が動かないのはなぜですか？**
A: NavMeshがベイクされているか、敵にNavMeshAgentコンポーネントがあるか、エージェントがNavMesh表面上にあるかを確認してください。

**Q: 敵が壁に詰まっています。**
A: NavMeshAgentの半径を減らすか、障害物回避の品質を上げてください。

**Q: 敵をランダムにスポーンさせるにはどうすればよいですか？**
A: Random.insideUnitSphereを使用するか、スポーンポイントを配置してランダムに選択します。

**Q: 複数のNavMeshを使用できますか？**
A: はい、NavMeshComponentsパッケージを使用して複数の表面に対応できます。

---

## Expected Outcomes / 期待される成果

### English
By the end of this lecture, students should have:
- A working NavMesh system in their maze
- At least one enemy ball that chases the player
- Enemy-player collision detection working
- Basic understanding of AI navigation concepts
- A game that feels challenging but fair

### 日本語
この講義の終了までに、学生は以下を達成する必要があります：
- 迷路で動作するNavMeshシステム
- プレイヤーを追跡する少なくとも1つの敵ボール
- 敵-プレイヤーの衝突検出が機能している
- AIナビゲーション概念の基本的な理解
- 挑戦的だが公平なゲーム

---

## Assignment Preview / 課題プレビュー

### English
Next assignment will focus on:
- Adding multiple enemies
- Balancing enemy speed and detection range
- Creating different enemy types (optional)
- Adding spawn points
- Testing game difficulty

### 日本語
次の課題では以下に焦点を当てます：
- 複数の敵の追加
- 敵の速度と検出範囲のバランス
- 異なる敵タイプの作成（オプション）
- スポーンポイントの追加
- ゲーム難易度のテスト

