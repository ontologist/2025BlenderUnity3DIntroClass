# Week 6 Assignment: AI Enemy Implementation
# 第6週課題：AI敵ボールの実装

**Due Date / 提出期限:** Before Week 7 lecture / 第7週講義前  
**Points / 配点:** 15 points / 15点  
**Developer / 開発者:** Yuri Tijerino

---

## Assignment Overview / 課題概要

### English
Implement AI enemy balls that chase the player in your ball maze game. You'll use Unity's NavMesh system to create intelligent enemies that navigate around obstacles and pursue the player.

### 日本語
ボール迷路ゲームでプレイヤーを追跡するAI敵ボールを実装します。UnityのNavMeshシステムを使用して、障害物を回避し、プレイヤーを追跡する知的な敵を作成します。

---

## Learning Objectives / 学習目標

### English
By completing this assignment, you will demonstrate your ability to:
1. Set up and bake NavMesh in Unity
2. Configure NavMeshAgent components
3. Create AI chase behavior scripts
4. Implement player detection logic
5. Handle enemy-player collisions
6. Balance game difficulty

### 日本語
この課題を完了することで、以下の能力を示します：
1. UnityでNavMeshをセットアップしてベイクする
2. NavMeshAgentコンポーネントを設定する
3. AI追跡動作スクリプトを作成する
4. プレイヤー検出ロジックを実装する
5. 敵-プレイヤーの衝突を処理する
6. ゲーム難易度をバランスさせる

---

## Assignment Requirements / 課題要件

### Part 1: NavMesh Setup (3 points / 3点)

#### English

**1. NavMesh Baking (2 points)**
- Mark all walkable surfaces in your maze as Navigation Static
- Bake NavMesh for your scene
- NavMesh should cover the entire maze floor
- Walls and obstacles should be excluded from NavMesh
- Verify NavMesh appears blue in Scene view

**2. NavMesh Configuration (1 point)**
- Set appropriate agent radius (0.5-1.0 units)
- Set appropriate agent height (1-2 units)
- Configure maximum slope (45-60 degrees)

#### 日本語

**1. NavMeshのベイク（2点）**
- 迷路内のすべての歩行可能な表面をNavigation Staticとしてマーク
- シーンのNavMeshをベイク
- NavMeshは迷路の床全体をカバーする必要がある
- 壁と障害物はNavMeshから除外する必要がある
- SceneビューでNavMeshが青色で表示されることを確認

**2. NavMesh設定（1点）**
- 適切なエージェント半径（0.5-1.0ユニット）を設定
- 適切なエージェント高さ（1-2ユニット）を設定
- 最大傾斜（45-60度）を設定

---

### Part 2: Enemy Ball GameObject (3 points / 3点)

#### English

**1. Enemy Ball Prefab (2 points)**
- Create an enemy ball GameObject (Sphere primitive)
- Apply contrasting material (red or different color from player)
- Add Rigidbody component
- Add NavMeshAgent component
- Configure NavMeshAgent:
  - Speed: 3-5 units/second
  - Angular Speed: 120-180 degrees/second
  - Acceleration: 8 units/second²
  - Stopping Distance: 0.5 units

**2. Enemy Tag and Layer (1 point)**
- Tag enemy as "Enemy" (or create custom tag)
- Set up appropriate layer for collision detection
- Ensure enemy doesn't collide with other enemies (optional)

#### 日本語

**1. 敵ボールプレハブ（2点）**
- 敵ボールGameObject（Sphereプリミティブ）を作成
- 対照的なマテリアル（赤またはプレイヤーとは異なる色）を適用
- Rigidbodyコンポーネントを追加
- NavMeshAgentコンポーネントを追加
- NavMeshAgentを設定：
  - 速度：3-5ユニット/秒
  - 角速度：120-180度/秒
  - 加速度：8ユニット/秒²
  - 停止距離：0.5ユニット

**2. 敵のタグとレイヤー（1点）**
- 敵に"Enemy"タグを付ける（またはカスタムタグを作成）
- 衝突検出のための適切なレイヤーを設定
- 敵が他の敵と衝突しないようにする（オプション）

---

### Part 3: Enemy Controller Script (5 points / 5点)

#### English

**1. Basic Chase Behavior (3 points)**
- Create EnemyController script
- Find player GameObject by tag ("Player")
- Set NavMeshAgent destination to player position
- Update destination every frame in FixedUpdate()
- Enemy should continuously chase player when active

**2. Detection Range Logic (2 points)**
- Add detection range parameter (10-15 units)
- Only chase player when within detection range
- Stop chasing when player moves outside chase range (optional)
- Enemy should not move when player not detected

#### 日本語

**1. 基本的な追跡動作（3点）**
- EnemyControllerスクリプトを作成
- タグ（"Player"）でプレイヤーGameObjectを検索
- NavMeshAgentの目的地をプレイヤーの位置に設定
- FixedUpdate()で毎フレーム目的地を更新
- 敵はアクティブなときにプレイヤーを継続的に追跡する必要がある

**2. 検出範囲ロジック（2点）**
- 検出範囲パラメータ（10-15ユニット）を追加
- 検出範囲内にいるときのみプレイヤーを追跡
- プレイヤーが追跡範囲外に移動したら追跡を停止（オプション）
- プレイヤーが検出されていないときは敵が動かないようにする

**Code Template / コードテンプレート:**
```csharp
public class EnemyController : MonoBehaviour
{
    private NavMeshAgent agent;
    private Transform player;
    public float detectionRange = 10f;
    
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }
    
    void FixedUpdate()
    {
        if (player != null)
        {
            float distance = Vector3.Distance(transform.position, player.position);
            if (distance <= detectionRange)
            {
                agent.SetDestination(player.position);
            }
            else
            {
                agent.ResetPath();
            }
        }
    }
}
```

---

### Part 4: Collision Detection (2 points / 2点)

#### English

**1. Game Over Detection (2 points)**
- Detect when enemy collides with player
- Use OnTriggerEnter or OnCollisionEnter
- Call GameManager.GameOver() when collision occurs
- Add visual/audio feedback (optional but recommended)
- Ensure player ball has "Player" tag

#### 日本語

**1. ゲームオーバー検出（2点）**
- 敵がプレイヤーと衝突したときを検出
- OnTriggerEnterまたはOnCollisionEnterを使用
- 衝突時にGameManager.GameOver()を呼び出す
- ビジュアル/オーディオフィードバックを追加（オプションだが推奨）
- プレイヤーボールに"Player"タグが付いていることを確認

---

### Part 5: Testing and Balancing (2 points / 2点)

#### English

**1. Gameplay Testing (1 point)**
- Test enemy chases player correctly
- Verify enemy navigates around obstacles
- Ensure enemy doesn't get stuck
- Test collision detection works properly

**2. Difficulty Balancing (1 point)**
- Adjust enemy speed to feel challenging but fair
- Adjust detection range for good gameplay feel
- Enemy should be a threat but not impossible to avoid
- Document your chosen values in comments

#### 日本語

**1. ゲームプレイテスト（1点）**
- 敵がプレイヤーを正しく追跡することをテスト
- 敵が障害物を回避することを確認
- 敵が詰まらないことを確認
- 衝突検出が正しく機能することをテスト

**2. 難易度バランス（1点）**
- 敵の速度を調整して挑戦的だが公平に感じるようにする
- 良いゲームプレイのフィールのために検出範囲を調整
- 敵は脅威であるが、回避不可能ではない必要がある
- 選択した値をコメントで文書化

---

## Submission Requirements / 提出要件

### English

**1. Project Files (Required)**
- Unity project with all scripts and prefabs
- EnemyController script with comments
- At least one enemy prefab
- NavMesh baked and visible in Scene view

**2. GitHub Submission (Required)**
- Commit all changes with descriptive message
- Push to your GitHub repository
- Include screenshot showing NavMesh and enemies in Scene view
- File: `week06_navmesh_screenshot.png`

**3. Testing Documentation (Optional but Recommended)**
- Document enemy speed and detection range values chosen
- Note any issues encountered and how you solved them
- Brief gameplay testing notes

#### 日本語

**1. プロジェクトファイル（必須）**
- すべてのスクリプトとプレハブを含むUnityプロジェクト
- コメント付きのEnemyControllerスクリプト
- 少なくとも1つの敵プレハブ
- NavMeshがベイクされ、Sceneビューで表示される

**2. GitHub提出（必須）**
- 説明的なメッセージですべての変更をコミット
- GitHubリポジトリにプッシュ
- SceneビューでNavMeshと敵を示すスクリーンショットを含める
- ファイル：`week06_navmesh_screenshot.png`

**3. テストドキュメント（オプションだが推奨）**
- 選択した敵の速度と検出範囲の値を文書化
- 遭遇した問題とその解決方法を記録
- 簡単なゲームプレイテストノート

---

## Bonus Points / ボーナス点 (+3 points max)

### English

**1. Multiple Enemy Types (1 point)**
- Create 2 different enemy types with different speeds
- Fast enemy: 6-8 units/second
- Slow enemy: 2-3 units/second
- Different colored materials to distinguish

**2. Enemy Spawner (1 point)**
- Create EnemySpawner script
- Spawn enemies at specific locations
- Spawn enemies every X seconds
- Limit maximum enemy count

**3. Advanced AI Behavior (1 point)**
- Implement patrol behavior when player not detected
- Add enemy health system
- Create enemy spawn points as GameObjects
- Add visual indicators for detection range (Gizmos)

#### 日本語

**1. 複数の敵タイプ（1点）**
- 異なる速度の2つの異なる敵タイプを作成
- 速い敵：6-8ユニット/秒
- 遅い敵：2-3ユニット/秒
- 区別するために異なる色のマテリアル

**2. 敵スポナー（1点）**
- EnemySpawnerスクリプトを作成
- 特定の位置で敵をスポーン
- X秒ごとに敵をスポーン
- 最大敵数を制限

**3. 高度なAI動作（1点）**
- プレイヤーが検出されていないときにパトロール動作を実装
- 敵の体力システムを追加
- 敵のスポーンポイントをGameObjectとして作成
- 検出範囲の視覚的インジケーター（Gizmos）を追加

---

## Common Mistakes to Avoid / 避けるべき一般的な間違い

### English
- ❌ Forgetting to bake NavMesh (enemy won't move)
- ❌ Not updating destination every frame
- ❌ Wrong NavMeshAgent size (gets stuck)
- ❌ Not setting Player tag on player ball
- ❌ Using wrong collision detection method
- ❌ Enemy speed too fast or too slow
- ❌ Detection range too large (unfair) or too small (too easy)

### 日本語
- ❌ NavMeshのベイクを忘れる（敵が動かない）
- ❌ 毎フレーム目的地を更新しない
- ❌ NavMeshAgentのサイズが間違っている（詰まる）
- ❌ プレイヤーボールにPlayerタグを設定しない
- ❌ 間違った衝突検出方法を使用
- ❌ 敵の速度が速すぎるまたは遅すぎる
- ❌ 検出範囲が大きすぎる（不公平）または小さすぎる（簡単すぎる）

---

## Resources / リソース

- Unity NavMesh Documentation: https://docs.unity3d.com/Manual/nav-BuildingNavMesh.html
- NavMeshAgent API Reference: https://docs.unity3d.com/ScriptReference/AI.NavMeshAgent.html
- Unity AI Tutorial: https://learn.unity.com/tutorial/introduction-to-navmesh

---

**Good luck with your assignment! / 課題頑張ってください！**

