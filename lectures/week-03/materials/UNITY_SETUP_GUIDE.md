# Unity3D Installation & Setup Guide / Unity3Dインストール＆セットアップガイド
**Developer / 開発者:** Yuri Tijerino

---

## Introduction / 紹介

### English
Unity3D is a powerful cross-platform game engine used to create 2D and 3D games. In this course, you'll use Unity3D to:
- Import Blender models into game scenes
- Add physics and interactivity to game objects
- Create player controls and game mechanics
- Build complete playable game projects
- Export games for multiple platforms

This guide will walk you through installing and setting up Unity3D for this course in about 15-20 minutes.

**What You'll Learn:**
- How to install Unity Hub and Unity Editor
- How to create and manage Unity projects
- Basic Unity interface navigation
- Essential settings for game development
- How to connect Unity with your code editor (Cursor)

### 日本語
Unity3Dは、2Dおよび3Dゲームを作成するために使用される強力なクロスプラットフォームゲームエンジンです。このコースでは、Unity3Dを以下のために使用します：
- Blenderモデルをゲームシーンにインポート
- ゲームオブジェクトに物理とインタラクティビティを追加
- プレイヤーコントロールとゲームメカニクスを作成
- 完全なプレイ可能なゲームプロジェクトを構築
- 複数のプラットフォーム用にゲームをエクスポート

このガイドでは、約15〜20分でこのコース用のUnity3Dのインストールとセットアップを説明します。

**学ぶこと:**
- Unity HubとUnity Editorのインストール方法
- Unityプロジェクトの作成と管理方法
- 基本的なUnityインターフェースナビゲーション
- ゲーム開発のための必須設定
- UnityをコードエディタUnity（Cursor）と接続する方法

---

## System Requirements / システム要件

### English

**Minimum Requirements:**
- **OS:** Windows 10 (64-bit), macOS 10.15+, or Ubuntu 20.04+
- **CPU:** X64 architecture with SSE2 instruction set support
- **RAM:** 8 GB
- **Graphics:** DX10 (shader model 4.0) capable GPU
- **Storage:**
  - Unity Hub: ~100 MB
  - Unity Editor: 4-6 GB per version
  - Projects: 1-5 GB per project (varies)
  - **Total Recommended:** 20 GB free space
- **Internet:** Required for installation and asset downloads

**Recommended Requirements:**
- **OS:** Windows 11 (64-bit) or macOS 12+
- **CPU:** Quad-core processor or better
- **RAM:** 16 GB or more
- **Graphics:**
  - Dedicated GPU with 4 GB VRAM
  - NVIDIA GeForce GTX 1060 or AMD Radeon RX 580 (or better)
- **Storage:** SSD with 40 GB+ free space
- **Display:** 1920x1080 or higher resolution

**Note for Apple Silicon (M1/M2/M3) Macs:**
- Unity runs natively on Apple Silicon
- Performance is excellent with Unity 2022 LTS and newer
- Some older Unity versions require Rosetta 2

### 日本語

**最小要件:**
- **OS:** Windows 10（64ビット）、macOS 10.15+、またはUbuntu 20.04+
- **CPU:** SSE2命令セットをサポートするX64アーキテクチャ
- **RAM:** 8 GB
- **グラフィックス:** DX10（シェーダーモデル4.0）対応GPU
- **ストレージ:**
  - Unity Hub：約100 MB
  - Unity Editor：バージョンごとに4〜6 GB
  - プロジェクト：プロジェクトごとに1〜5 GB（変動）
  - **合計推奨:** 20 GB以上の空き容量
- **インターネット:** インストールとアセットのダウンロードに必要

**推奨要件:**
- **OS:** Windows 11（64ビット）またはmacOS 12+
- **CPU:** クアッドコアプロセッサ以上
- **RAM:** 16 GB以上
- **グラフィックス:**
  - 4 GB VRAMの専用GPU
  - NVIDIA GeForce GTX 1060またはAMD Radeon RX 580（またはそれ以上）
- **ストレージ:** 40 GB以上の空き容量のあるSSD
- **ディスプレイ:** 1920x1080以上の解像度

**Apple Silicon（M1/M2/M3）Mac向けの注意:**
- UnityはApple Siliconでネイティブに動作
- Unity 2022 LTS以降では優れたパフォーマンス
- 一部の古いUnityバージョンではRosetta 2が必要

---

## Step 1: Create Unity Account / ステップ1：Unityアカウントを作成

### English

Before installing Unity, create a free Unity account:

1. **Visit Unity ID website:**
   - Go to https://id.unity.com/

2. **Click "Create a Unity ID"**

3. **Enter your information:**
   - Email address (use your school email if possible)
   - Username
   - Password (strong password recommended)
   - Full name

4. **Verify your email:**
   - Check your email inbox
   - Click the verification link
   - This activates your Unity account

5. **Choose License Type (you'll be asked during installation):**
   - **Unity Personal (Free)** - Choose this for the course
   - Requirements: Revenue/funding less than $100K/year
   - Perfect for students and learning

**Why create account first?**
- Faster installation process
- Immediate access to Unity services
- Asset Store access
- Cloud builds and collaboration features

### 日本語

Unityをインストールする前に、無料のUnityアカウントを作成します：

1. **Unity IDウェブサイトにアクセス:**
   - https://id.unity.com/ にアクセス

2. **「Create a Unity ID」をクリック**

3. **情報を入力:**
   - メールアドレス（可能であれば学校のメールを使用）
   - ユーザー名
   - パスワード（強力なパスワードを推奨）
   - フルネーム

4. **メールを確認:**
   - メール受信トレイを確認
   - 確認リンクをクリック
   - これによりUnityアカウントがアクティベートされます

5. **ライセンスタイプを選択（インストール中に尋ねられます）:**
   - **Unity Personal（無料）** - このコース用にこれを選択
   - 要件：年間収益/資金が$100K未満
   - 学生と学習に最適

**なぜアカウントを最初に作成？**
- より速いインストールプロセス
- Unityサービスへの即座のアクセス
- アセットストアへのアクセス
- クラウドビルドとコラボレーション機能

---

## Step 2: Download Unity Hub / ステップ2：Unity Hubをダウンロード

### English

Unity Hub is a management tool for Unity installations and projects.

1. **Visit Unity Download page:**
   - Go to https://unity.com/download

2. **Download Unity Hub:**
   - Click **"Download Unity Hub"**
   - The website detects your operating system automatically
   - File size: approximately 100 MB

3. **Choose your platform:**
   - **Windows:** `UnityHubSetup.exe`
   - **Mac:** `UnityHubSetup.dmg`
   - **Linux:** `UnityHub.AppImage`

4. **Wait for download to complete**

**What is Unity Hub?**
- Central application to manage Unity versions
- Project manager and launcher
- License management
- Easy version switching for different projects

### 日本語

Unity Hubは、Unityのインストールとプロジェクトを管理するためのツールです。

1. **Unityダウンロードページにアクセス:**
   - https://unity.com/download にアクセス

2. **Unity Hubをダウンロード:**
   - **「Download Unity Hub」**をクリック
   - ウェブサイトが自動的にオペレーティングシステムを検出します
   - ファイルサイズ：約100 MB

3. **プラットフォームを選択:**
   - **Windows:** `UnityHubSetup.exe`
   - **Mac:** `UnityHubSetup.dmg`
   - **Linux:** `UnityHub.AppImage`

4. **ダウンロードが完了するまで待つ**

**Unity Hubとは？**
- Unityバージョンを管理するための中央アプリケーション
- プロジェクトマネージャーとランチャー
- ライセンス管理
- 異なるプロジェクト用の簡単なバージョン切り替え

---

## Step 3: Install Unity Hub / ステップ3：Unity Hubをインストール

### For Windows / Windows用

#### English
1. Locate the downloaded file: `UnityHubSetup.exe`
2. Double-click to run the installer
3. If Windows SmartScreen appears, click "More info" → "Run anyway"
4. Accept the Unity Hub License Agreement
5. Choose installation location (default is fine: `C:\Program Files\Unity Hub`)
6. Click "Install"
7. Wait for installation (1-2 minutes)
8. Launch Unity Hub when installation completes

#### 日本語
1. ダウンロードしたファイルを見つける：`UnityHubSetup.exe`
2. ダブルクリックしてインストーラーを実行
3. Windows SmartScreenが表示された場合、「詳細情報」→「実行」をクリック
4. Unity Hubライセンス契約に同意
5. インストール場所を選択（デフォルトで問題なし：`C:\Program Files\Unity Hub`）
6. 「Install」をクリック
7. インストールを待つ（1〜2分）
8. インストール完了時にUnity Hubを起動

---

### For Mac / Mac用

#### English
1. Locate the downloaded file: `UnityHubSetup.dmg`
2. Double-click to open the disk image
3. Drag Unity Hub to the Applications folder
4. Eject the disk image
5. Open Applications folder
6. **First launch:**
   - Right-click Unity Hub → "Open"
   - Click "Open" to confirm (macOS security)
   - This only needs to be done once
7. Unity Hub will launch

#### 日本語
1. ダウンロードしたファイルを見つける：`UnityHubSetup.dmg`
2. ダブルクリックしてディスクイメージを開く
3. Unity HubをApplicationsフォルダにドラッグ
4. ディスクイメージを取り出す
5. Applicationsフォルダを開く
6. **初回起動:**
   - Unity Hubを右クリック →「開く」
   - 「開く」をクリックして確認（macOSセキュリティ）
   - これは一度だけ行う必要があります
7. Unity Hubが起動します

---

### For Linux / Linux用

#### English
1. Locate the downloaded file: `UnityHub.AppImage`
2. Make it executable:
```bash
chmod +x UnityHub.AppImage
```
3. Run Unity Hub:
```bash
./UnityHub.AppImage
```
4. **(Optional) Move to /opt for system-wide access:**
```bash
sudo mv UnityHub.AppImage /opt/UnityHub.AppImage
sudo ln -s /opt/UnityHub.AppImage /usr/local/bin/unityhub
```
5. Now you can launch with: `unityhub`

#### 日本語
1. ダウンロードしたファイルを見つける：`UnityHub.AppImage`
2. 実行可能にする:
```bash
chmod +x UnityHub.AppImage
```
3. Unity Hubを実行:
```bash
./UnityHub.AppImage
```
4. **（オプション）システム全体でのアクセスのために/optに移動:**
```bash
sudo mv UnityHub.AppImage /opt/UnityHub.AppImage
sudo ln -s /opt/UnityHub.AppImage /usr/local/bin/unityhub
```
5. これで`unityhub`で起動できます

---

## Step 4: Sign in to Unity Hub / ステップ4：Unity Hubにサインイン

### English

1. **Launch Unity Hub** (if not already open)

2. **Sign in with your Unity ID:**
   - Click **"Sign in"** button (top right)
   - Enter your Unity ID email and password
   - Click "Sign in"

3. **Choose your license:**
   - Unity Hub will ask you to activate a license
   - Click **"Add"** or **"Get Unity Personal"**
   - Select **"Unity Personal"**
   - Check the boxes:
     - ✅ "I don't use Unity in a professional capacity"
     - ✅ Accept terms
   - Click **"Done"** or **"Activate"**

4. **Verify license activation:**
   - Look for a green checkmark next to "Unity Personal"
   - You're now ready to install Unity Editor

### 日本語

1. **Unity Hubを起動**（まだ開いていない場合）

2. **Unity IDでサインイン:**
   - **「Sign in」**ボタンをクリック（右上）
   - Unity IDメールとパスワードを入力
   - 「Sign in」をクリック

3. **ライセンスを選択:**
   - Unity Hubがライセンスをアクティベートするように求めます
   - **「Add」**または**「Get Unity Personal」**をクリック
   - **「Unity Personal」**を選択
   - チェックボックスにチェック:
     - ✅ 「I don't use Unity in a professional capacity」
     - ✅ 規約に同意
   - **「Done」**または**「Activate」**をクリック

4. **ライセンスアクティベーションを確認:**
   - 「Unity Personal」の横に緑のチェックマークを探す
   - これでUnity Editorをインストールする準備が整いました

---

## Step 5: Install Unity Editor / ステップ5：Unity Editorをインストール

### English

1. **In Unity Hub, click the "Installs" tab** (left sidebar)

2. **Click "Install Editor" or "Add" button**

3. **Choose Unity Version:**
   - **Recommended for this course:** Unity **2022 LTS (Long Term Support)**
   - Look for **"2022.3.x LTS"** (where x is the latest patch number)
   - LTS versions are stable and receive long-term support
   - Click **"Install"**

4. **Add Modules (Important!):**
   You'll be asked which modules to install. Select:

   **Essential Modules:**
   - ✅ **Microsoft Visual Studio Community** (Windows only - code editor, optional if using Cursor)
   - ✅ **Documentation** (offline Unity manual)
   - ✅ **Language Pack** (optional - add Japanese if desired)

   **Build Support (choose your target platforms):**
   - ✅ **Windows Build Support (IL2CPP)** (if on Mac/Linux and want to build for Windows)
   - ✅ **Mac Build Support (Mono)** (if on Windows and want to build for Mac)
   - ✅ **Linux Build Support (Mono)** (for Linux builds)
   - ✅ **WebGL Build Support** (to build browser games)
   - ⚠️ **Android Build Support** (optional - if interested in mobile development)
   - ⚠️ **iOS Build Support** (optional - Mac only, requires Xcode)

5. **Accept license agreements**

6. **Click "Continue" then "Install"**

7. **Wait for installation:**
   - Download size: 4-6 GB depending on modules
   - Installation time: 15-30 minutes depending on internet speed
   - You can continue with other tasks while installing

8. **Verify installation:**
   - When complete, you'll see Unity 2022.3.x LTS listed in "Installs" tab
   - There will be a green "Open" button next to it

### 日本語

1. **Unity Hubで「Installs」タブをクリック**（左サイドバー）

2. **「Install Editor」または「Add」ボタンをクリック**

3. **Unityバージョンを選択:**
   - **このコースに推奨:** Unity **2022 LTS（長期サポート）**
   - **「2022.3.x LTS」**を探す（xは最新のパッチ番号）
   - LTSバージョンは安定しており、長期サポートを受けます
   - **「Install」**をクリック

4. **モジュールを追加（重要！）:**
   どのモジュールをインストールするか尋ねられます。以下を選択:

   **必須モジュール:**
   - ✅ **Microsoft Visual Studio Community**（Windowsのみ - コードエディタ、Cursorを使用する場合はオプション）
   - ✅ **Documentation**（オフラインUnityマニュアル）
   - ✅ **Language Pack**（オプション - 必要に応じて日本語を追加）

   **ビルドサポート（ターゲットプラットフォームを選択）:**
   - ✅ **Windows Build Support (IL2CPP)**（Mac/LinuxでWindows用にビルドする場合）
   - ✅ **Mac Build Support (Mono)**（WindowsでMac用にビルドする場合）
   - ✅ **Linux Build Support (Mono)**（Linuxビルド用）
   - ✅ **WebGL Build Support**（ブラウザゲームをビルドする場合）
   - ⚠️ **Android Build Support**（オプション - モバイル開発に興味がある場合）
   - ⚠️ **iOS Build Support**（オプション - Macのみ、Xcodeが必要）

5. **ライセンス契約に同意**

6. **「Continue」をクリックしてから「Install」**

7. **インストールを待つ:**
   - ダウンロードサイズ：モジュールに応じて4〜6 GB
   - インストール時間：インターネット速度に応じて15〜30分
   - インストール中に他のタスクを続行できます

8. **インストールを確認:**
   - 完了すると、「Installs」タブにUnity 2022.3.x LTSがリストされます
   - その横に緑色の「Open」ボタンがあります

---

## Step 6: Create Your First Unity Project / ステップ6：最初のUnityプロジェクトを作成

### English

1. **In Unity Hub, click the "Projects" tab**

2. **Click "New project" button**

3. **Configure project settings:**

   **Editor Version:**
   - Select **Unity 2022.3.x LTS** (the version you just installed)

   **Template:**
   - Choose **"3D (Built-in Render Pipeline)"**
   - This is the standard template for 3D games
   - Perfect for importing Blender models

   **Project Name:**
   - Enter: `TestProject` or `Unity-Learning-Project`

   **Location:**
   - Click **"..."** to browse
   - Navigate to your course repository: `game-dev-2025-yourname/week-03/`
   - Or create a dedicated Unity projects folder: `Documents/UnityProjects/`

   **Organization:** (optional)
   - Leave as "Personal" or enter your name

4. **Click "Create project"**

5. **Wait for project creation:**
   - Unity Editor will open (may take 2-3 minutes first time)
   - Unity is importing default assets and setting up the project
   - You'll see a loading screen with Unity logo

6. **First launch complete!**
   - You should now see the Unity Editor interface
   - Default scene with Main Camera and Directional Light
   - Various windows: Scene, Game, Hierarchy, Project, Inspector

### 日本語

1. **Unity Hubで「Projects」タブをクリック**

2. **「New project」ボタンをクリック**

3. **プロジェクト設定を構成:**

   **Editor Version:**
   - **Unity 2022.3.x LTS**を選択（インストールしたばかりのバージョン）

   **Template:**
   - **「3D (Built-in Render Pipeline)」**を選択
   - これは3Dゲームの標準テンプレート
   - Blenderモデルのインポートに最適

   **Project Name:**
   - 入力：`TestProject`または`Unity-Learning-Project`

   **Location:**
   - **「...」**をクリックしてブラウズ
   - コースリポジトリに移動：`game-dev-2025-yourname/week-03/`
   - または専用のUnityプロジェクトフォルダを作成：`Documents/UnityProjects/`

   **Organization:**（オプション）
   - 「Personal」のままにするか、名前を入力

4. **「Create project」をクリック**

5. **プロジェクト作成を待つ:**
   - Unity Editorが開きます（初回は2〜3分かかる場合があります）
   - Unityがデフォルトアセットをインポートし、プロジェクトをセットアップしています
   - Unityロゴの読み込み画面が表示されます

6. **初回起動完了！**
   - Unity Editorインターフェースが表示されるはずです
   - Main CameraとDirectional Lightを含むデフォルトシーン
   - さまざまなウィンドウ：Scene、Game、Hierarchy、Project、Inspector

---

## Step 7: Unity Interface Overview / ステップ7：Unityインターフェースの概要

### English

Understanding Unity's interface is crucial. Here are the main windows:

**1. Scene View (Center-Top):**
- Where you build and navigate your game world
- Move, rotate, and place objects
- Use W/E/R/T keys to switch tools
- Navigate with middle mouse button or Alt+Left Click

**2. Game View (Center-Top, Tab next to Scene):**
- Shows what the player will see
- Click "Play" button to test your game
- Only visible when scene contains a camera

**3. Hierarchy (Left Side):**
- Lists all objects in current scene
- Shows parent-child relationships
- Click to select objects
- Right-click to create new objects

**4. Project Window (Bottom):**
- Your project's file system
- All assets: scripts, models, textures, sounds
- Organized in folders
- Drag assets from here into the scene

**5. Inspector (Right Side):**
- Shows properties of selected object
- Add/remove components
- Adjust values and settings
- Transform (position, rotation, scale)

**6. Console (Bottom, Tab next to Project):**
- Shows errors, warnings, and messages
- Essential for debugging code
- Click to see detailed error information

**7. Toolbar (Top):**
- Play/Pause/Step buttons (center)
- Transform tools (left): Move, Rotate, Scale, Rect, Transform
- Hand tool for navigation
- Center object button

### Navigation Controls:
- **Right Mouse Button + WASD:** Fly through scene (like FPS game)
- **Middle Mouse Button (drag):** Pan view
- **Scroll Wheel:** Zoom in/out
- **Alt + Left Mouse Button:** Orbit around selection
- **F:** Focus on selected object
- **Double-click object in Hierarchy:** Focus on that object

### 日本語

Unityのインターフェースを理解することは非常に重要です。主なウィンドウは以下です：

**1. シーンビュー（中央上部）:**
- ゲーム世界を構築してナビゲートする場所
- オブジェクトを移動、回転、配置
- W/E/R/Tキーを使用してツールを切り替え
- マウス中ボタンまたはAlt+左クリックでナビゲート

**2. ゲームビュー（中央上部、シーンの横のタブ）:**
- プレイヤーが見るものを表示
- 「Play」ボタンをクリックしてゲームをテスト
- シーンにカメラが含まれている場合のみ表示

**3. ヒエラルキー（左側）:**
- 現在のシーンのすべてのオブジェクトをリスト
- 親子関係を表示
- クリックしてオブジェクトを選択
- 右クリックして新しいオブジェクトを作成

**4. プロジェクトウィンドウ（下部）:**
- プロジェクトのファイルシステム
- すべてのアセット：スクリプト、モデル、テクスチャ、サウンド
- フォルダで整理
- ここからシーンにアセットをドラッグ

**5. インスペクター（右側）:**
- 選択したオブジェクトのプロパティを表示
- コンポーネントを追加/削除
- 値と設定を調整
- トランスフォーム（位置、回転、スケール）

**6. コンソール（下部、プロジェクトの横のタブ）:**
- エラー、警告、メッセージを表示
- コードのデバッグに不可欠
- クリックして詳細なエラー情報を表示

**7. ツールバー（上部）:**
- Play/Pause/Stepボタン（中央）
- トランスフォームツール（左）：移動、回転、スケール、Rect、トランスフォーム
- ナビゲーション用のハンドツール
- オブジェクトを中央に配置するボタン

### ナビゲーションコントロール:
- **右マウスボタン + WASD:** シーンを飛行（FPSゲームのように）
- **マウス中ボタン（ドラッグ）:** ビューをパン
- **スクロールホイール:** ズームイン/アウト
- **Alt +左マウスボタン:** 選択の周りを周回
- **F:** 選択したオブジェクトにフォーカス
- **ヒエラルキーのオブジェクトをダブルクリック:** そのオブジェクトにフォーカス

---

## Step 8: Essential Unity Settings / ステップ8：必須のUnity設定

### English

Let's configure Unity for optimal game development:

**1. Set External Script Editor (Connect Cursor):**
- Go to **Edit → Preferences** (Windows/Linux) or **Unity → Settings** (Mac)
- Click **"External Tools"** in the left sidebar
- Under **"External Script Editor"**, click the dropdown
- Select **"Browse..."**
- Navigate to Cursor application:
  - **Windows:** `C:\Users\YourName\AppData\Local\Programs\cursor\Cursor.exe`
  - **Mac:** `/Applications/Cursor.app`
  - **Linux:** `/usr/local/bin/cursor` or wherever you installed it
- Click **"Open"**
- Now double-clicking C# scripts in Unity will open them in Cursor

**2. Enable Auto-Refresh:**
- In **Edit → Preferences → General**
- Ensure **"Auto Refresh"** is enabled
- This automatically updates Unity when you save scripts

**3. Maximize On Play:**
- In **Edit → Preferences → General**
- Optionally enable **"Maximize On Play"**
- Makes Game view fullscreen when testing

**4. Set Project to use .gitignore:**
- In **Edit → Project Settings → Editor**
- Under **"Version Control"**:
  - Set **"Mode"** to **"Visible Meta Files"**
  - Set **"Asset Serialization"** to **"Force Text"**
- These settings make Unity projects Git-friendly

**5. Configure Colors (Optional):**
- In **Edit → Preferences → Colors**
- Adjust Playmode tint if desired
- Helps distinguish Play Mode from Edit Mode

**6. Physics Settings:**
- In **Edit → Project Settings → Physics**
- Default gravity is **-9.81** (realistic)
- Keep default for this course

### 日本語

ゲーム開発を最適化するためにUnityを設定しましょう：

**1. 外部スクリプトエディタを設定（Cursorを接続）:**
- **編集 → プリファレンス**（Windows/Linux）または**Unity → Settings**（Mac）に移動
- 左サイドバーの**「External Tools」**をクリック
- **「External Script Editor」**の下で、ドロップダウンをクリック
- **「Browse...」**を選択
- Cursorアプリケーションに移動:
  - **Windows:** `C:\Users\YourName\AppData\Local\Programs\cursor\Cursor.exe`
  - **Mac:** `/Applications/Cursor.app`
  - **Linux:** `/usr/local/bin/cursor`またはインストールした場所
- **「Open」**をクリック
- これでUnityのC#スクリプトをダブルクリックするとCursorで開きます

**2. 自動更新を有効化:**
- **編集 → プリファレンス → 一般**で
- **「Auto Refresh」**が有効になっていることを確認
- これによりスクリプトを保存するとUnityが自動的に更新されます

**3. 再生時に最大化:**
- **編集 → プリファレンス → 一般**で
- オプションで**「Maximize On Play」**を有効化
- テスト時にゲームビューがフルスクリーンになります

**4. プロジェクトが.gitignoreを使用するように設定:**
- **編集 → プロジェクト設定 → エディタ**で
- **「Version Control」**の下:
  - **「Mode」**を**「Visible Meta Files」**に設定
  - **「Asset Serialization」**を**「Force Text」**に設定
- これらの設定によりUnityプロジェクトがGitフレンドリーになります

**5. 色を設定（オプション）:**
- **編集 → プリファレンス → Colors**で
- 必要に応じてPlaymode tintを調整
- プレイモードと編集モードを区別するのに役立ちます

**6. 物理設定:**
- **編集 → プロジェクト設定 → Physics**で
- デフォルトの重力は**-9.81**（現実的）
- このコースではデフォルトを維持

---

## Step 9: Test Unity Installation / ステップ9：Unityインストールをテスト

### English

Let's create a simple test to verify everything works:

**1. Create a 3D Object:**
- In Hierarchy, right-click → **3D Object → Cube**
- A cube appears at position (0, 0, 0)

**2. Position the Camera:**
- Select "Main Camera" in Hierarchy
- In Inspector, set Transform Position:
  - X: 0, Y: 1, Z: -5
- This positions camera to see the cube

**3. Add Color to Cube:**
- Select the Cube in Hierarchy
- In Inspector, scroll down to "Mesh Renderer" component
- Expand "Materials"
- Click the circle next to "Default-Material"
- Asset selector appears - click "New" to create new material
- Name it "TestMaterial"
- In Inspector, find "Albedo" color
- Click the color box and choose a color (e.g., blue, red, green)

**4. Test Play Mode:**
- Click the **Play** button (▶) at the top center
- Game view shows your colored cube
- **Success!** Unity is working correctly
- Click **Play** again to stop

**5. Add Physics (Optional test):**
- Select the Cube
- Click **"Add Component"** in Inspector
- Search for **"Rigidbody"**
- Click to add it
- Press **Play**
- The cube falls due to gravity!
- This confirms physics is working

**6. Save the Scene:**
- **File → Save As...**
- Save in `Assets/Scenes/` folder
- Name it: `TestScene`
- Click **Save**

**Congratulations!** Unity is installed and working correctly.

### 日本語

すべてが機能することを確認するための簡単なテストを作成しましょう：

**1. 3Dオブジェクトを作成:**
- ヒエラルキーで右クリック → **3D Object → Cube**
- 位置(0, 0, 0)にキューブが表示されます

**2. カメラを配置:**
- ヒエラルキーで「Main Camera」を選択
- インスペクターで、トランスフォーム位置を設定:
  - X: 0、Y: 1、Z: -5
- これによりカメラがキューブを見る位置に配置されます

**3. キューブに色を追加:**
- ヒエラルキーでキューブを選択
- インスペクターで、「Mesh Renderer」コンポーネントまでスクロール
- 「Materials」を展開
- 「Default-Material」の横の円をクリック
- アセットセレクターが表示されます -「New」をクリックして新しいマテリアルを作成
- 「TestMaterial」と名前を付ける
- インスペクターで「Albedo」カラーを見つける
- カラーボックスをクリックして色を選択（例：青、赤、緑）

**4. プレイモードをテスト:**
- 上部中央の**Play**ボタン（▶）をクリック
- ゲームビューに色付きのキューブが表示されます
- **成功！** Unityが正しく動作しています
- もう一度**Play**をクリックして停止

**5. 物理を追加（オプションのテスト）:**
- キューブを選択
- インスペクターで**「Add Component」**をクリック
- **「Rigidbody」**を検索
- クリックして追加
- **Play**を押す
- キューブが重力で落下します！
- これにより物理が機能していることを確認

**6. シーンを保存:**
- **ファイル → 名前を付けて保存...**
- `Assets/Scenes/`フォルダに保存
- 名前を付ける：`TestScene`
- **Save**をクリック

**おめでとうございます！** Unityがインストールされ、正しく動作しています。

---

## Step 10: Unity .gitignore Setup / ステップ10：Unity .gitignoreのセットアップ

### English

Unity creates many temporary files that shouldn't be committed to Git.

**1. Update your .gitignore file:**

If you set up your repository with the Unity .gitignore template in Week 1, you're all set!

If not, add these lines to your `.gitignore` file at the root of your repository:

```gitignore
# Unity generated files
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/

# Unity3D generated meta files
*.pidb.meta
*.pdb.meta
*.mdb.meta

# Unity3D generated file on crash reports
sysinfo.txt

# Builds
*.apk
*.aab
*.unitypackage
*.app

# Crashlytics generated file
crashlytics-build.properties

# Autogenerated VS/MD/Consulo solution and project files
ExportedObj/
.consulo/
*.csproj
*.unityproj
*.sln
*.suo
*.tmp
*.user
*.userprefs
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db

# Unity3D Auto generated folder
[Aa]ssets/AssetStoreTools*

# Visual Studio cache directory
.vs/

# Gradle cache directory (Android)
.gradle/

# macOS
.DS_Store

# Windows
Thumbs.db
Desktop.ini
```

**2. Save the .gitignore file**

**3. Commit the changes:**
```bash
git add .gitignore
git commit -m "Update .gitignore for Unity projects"
git push
```

**What these rules do:**
- Excludes Library folder (Unity's cache - can be regenerated)
- Excludes Temp folder (temporary files)
- Excludes build files
- Keeps your repository clean and small
- Only commits source files that matter

### 日本語

Unityは多くの一時ファイルを作成し、Gitにコミットすべきではありません。

**1. .gitignoreファイルを更新:**

Week 1でUnity .gitignoreテンプレートを使用してリポジトリをセットアップした場合は、準備完了です！

そうでない場合は、リポジトリのルートにある`.gitignore`ファイルに以下の行を追加します：

```gitignore
# Unity generated files
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/

# Unity3D generated meta files
*.pidb.meta
*.pdb.meta
*.mdb.meta

# Unity3D generated file on crash reports
sysinfo.txt

# Builds
*.apk
*.aab
*.unitypackage
*.app

# Crashlytics generated file
crashlytics-build.properties

# Autogenerated VS/MD/Consulo solution and project files
ExportedObj/
.consulo/
*.csproj
*.unityproj
*.sln
*.suo
*.tmp
*.user
*.userprefs
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db

# Unity3D Auto generated folder
[Aa]ssets/AssetStoreTools*

# Visual Studio cache directory
.vs/

# Gradle cache directory (Android)
.gradle/

# macOS
.DS_Store

# Windows
Thumbs.db
Desktop.ini
```

**2. .gitignoreファイルを保存**

**3. 変更をコミット:**
```bash
git add .gitignore
git commit -m "Unity プロジェクト用に.gitignoreを更新"
git push
```

**これらのルールが行うこと:**
- Libraryフォルダを除外（Unityのキャッシュ - 再生成可能）
- Tempフォルダを除外（一時ファイル）
- ビルドファイルを除外
- リポジトリをクリーンで小さく保つ
- 重要なソースファイルのみコミット

---

## Essential Unity Shortcuts / 必須のUnityショートカット

### English

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Play/Pause** | Ctrl/Cmd + P | Start/stop game playback |
| **Step Frame** | Ctrl/Cmd + Shift + P | Advance one frame in play mode |
| **New Object** | Ctrl/Cmd + Shift + N | Create new empty GameObject |
| **Duplicate** | Ctrl/Cmd + D | Duplicate selected object |
| **Frame Selected** | F | Focus camera on selected object |
| **Pan View** | Q + Drag or Middle Mouse | Pan scene view |
| **Move Tool** | W | Activate move tool |
| **Rotate Tool** | E | Activate rotate tool |
| **Scale Tool** | R | Activate scale tool |
| **Rect Transform** | T | Activate rect transform tool (UI) |
| **Hand Tool** | Q | Navigate without selecting objects |
| **Save** | Ctrl/Cmd + S | Save current scene |
| **Undo** | Ctrl/Cmd + Z | Undo last action |
| **Redo** | Ctrl/Cmd + Y | Redo last undone action |
| **Find** | Ctrl/Cmd + F | Search in scene |

**Pro Tips:**
- Hold **V** while moving objects to enable vertex snapping
- Hold **Ctrl/Cmd** while moving to snap to grid
- **Alt + Left Click + Drag:** Orbit around object
- **Right Click + WASD:** Fly through scene like FPS

### 日本語

| アクション | ショートカット | 説明 |
|--------|----------|-------------|
| **Play/Pause** | Ctrl/Cmd + P | ゲームの再生を開始/停止 |
| **Step Frame** | Ctrl/Cmd + Shift + P | プレイモードで1フレーム進む |
| **New Object** | Ctrl/Cmd + Shift + N | 新しい空のGameObjectを作成 |
| **Duplicate** | Ctrl/Cmd + D | 選択したオブジェクトを複製 |
| **Frame Selected** | F | 選択したオブジェクトにカメラをフォーカス |
| **Pan View** | Q + Drag またはマウス中ボタン | シーンビューをパン |
| **Move Tool** | W | 移動ツールを有効化 |
| **Rotate Tool** | E | 回転ツールを有効化 |
| **Scale Tool** | R | スケールツールを有効化 |
| **Rect Transform** | T | Rectトランスフォームツールを有効化（UI） |
| **Hand Tool** | Q | オブジェクトを選択せずにナビゲート |
| **Save** | Ctrl/Cmd + S | 現在のシーンを保存 |
| **Undo** | Ctrl/Cmd + Z | 最後のアクションを元に戻す |
| **Redo** | Ctrl/Cmd + Y | 最後に元に戻したアクションをやり直す |
| **Find** | Ctrl/Cmd + F | シーンで検索 |

**プロのヒント:**
- オブジェクトを移動中に**V**を押したままにして頂点スナップを有効化
- 移動中に**Ctrl/Cmd**を押したままにしてグリッドにスナップ
- **Alt +左クリック+ドラッグ:** オブジェクトの周りを周回
- **右クリック + WASD:** FPSのようにシーンを飛行

---

## Troubleshooting / トラブルシューティング

### Problem: Unity Hub won't launch / 問題：Unity Hubが起動しない

**English:**
- **Solution 1:** Restart computer
- **Solution 2:** Reinstall Unity Hub
- **Solution 3:** Check antivirus isn't blocking Unity Hub
- **Solution 4:** Run as administrator (Windows)

**日本語:**
- **解決策1:** コンピュータを再起動
- **解決策2:** Unity Hubを再インストール
- **解決策3:** アンチウイルスがUnity Hubをブロックしていないか確認
- **解決策4:** 管理者として実行（Windows）

---

### Problem: Can't activate Unity Personal license / 問題：Unity Personalライセンスをアクティベートできない

**English:**
- **Solution 1:** Ensure you're signed in with Unity ID
- **Solution 2:** Check internet connection
- **Solution 3:** Try signing out and signing in again
- **Solution 4:** Visit Unity website and verify account status

**日本語:**
- **解決策1:** Unity IDでサインインしていることを確認
- **解決策2:** インターネット接続を確認
- **解決策3:** サインアウトして再度サインイン
- **解決策4:** Unityウェブサイトにアクセスしてアカウントステータスを確認

---

### Problem: Unity Editor extremely slow / 問題：Unity Editorが非常に遅い

**English:**
- **Solution 1:** Close unnecessary applications
- **Solution 2:** Reduce quality in Edit → Project Settings → Quality
- **Solution 3:** Disable real-time Global Illumination
- **Solution 4:** Check GPU drivers are up to date
- **Solution 5:** Ensure project is on local drive (not network drive)

**日本語:**
- **解決策1:** 不要なアプリケーションを閉じる
- **解決策2:** 編集 → プロジェクト設定 → Qualityで品質を下げる
- **解決策3:** リアルタイムグローバルイルミネーションを無効化
- **解決策4:** GPUドライバが最新であることを確認
- **解決策5:** プロジェクトがローカルドライブにあることを確認（ネットワークドライブではない）

---

### Problem: Scripts don't open in Cursor / 問題：スクリプトがCursorで開かない

**English:**
- **Solution 1:** Set external editor again: Edit → Preferences → External Tools
- **Solution 2:** Restart Unity Editor
- **Solution 3:** Manually open Cursor and then open the script file
- **Solution 4:** Right-click script in Unity → Open C# Project

**日本語:**
- **解決策1:** 外部エディタを再度設定：編集 → プリファレンス → External Tools
- **解決策2:** Unity Editorを再起動
- **解決策3:** 手動でCursorを開いてからスクリプトファイルを開く
- **解決策4:** Unityでスクリプトを右クリック → Open C# Project

---

### Problem: "Failed to resolve packages" error / 問題：「Failed to resolve packages」エラー

**English:**
- **Solution 1:** Delete the `Library` folder in your project and reopen
- **Solution 2:** Window → Package Manager → Click refresh icon
- **Solution 3:** Check internet connection
- **Solution 4:** Clear package cache: Help → Reset Packages to defaults

**日本語:**
- **解決策1:** プロジェクトの`Library`フォルダを削除して再度開く
- **解決策2:** ウィンドウ → パッケージマネージャー → 更新アイコンをクリック
- **解決策3:** インターネット接続を確認
- **解決策4:** パッケージキャッシュをクリア：ヘルプ → パッケージをデフォルトにリセット

---

### Problem: Play button is grayed out / 問題：プレイボタンがグレーアウトしている

**English:**
- **Solution:** Save your scene first (Ctrl/Cmd + S)
- Unity requires scenes to be saved before entering play mode

**日本語:**
- **解決策:** 最初にシーンを保存（Ctrl/Cmd + S）
- Unityはプレイモードに入る前にシーンを保存する必要があります

---

## Next Steps / 次のステップ

### English
Now that Unity is installed and configured:
1. ✅ Familiarize yourself with the Unity interface
2. ✅ Practice navigating the Scene view
3. ✅ Experiment with creating and manipulating 3D objects
4. ✅ Test Play mode and understand Edit vs Play mode
5. ✅ Try the Unity tutorials: Help → Unity Manual
6. ✅ Save your test project to your course repository
7. ✅ Commit and push to GitHub
8. ✅ Ready to start **importing Blender models into Unity!**

**Recommended Practice:**
- Complete Unity Essentials tutorial: https://learn.unity.com/pathway/unity-essentials
- Watch "Unity for Beginners" videos on YouTube
- Practice basic C# scripting in Week 3 lectures

### 日本語
Unityがインストールされ、設定されたので:
1. ✅ Unityインターフェースに慣れる
2. ✅ シーンビューのナビゲーションを練習
3. ✅ 3Dオブジェクトの作成と操作を実験
4. ✅ プレイモードをテストし、編集モードとプレイモードの違いを理解
5. ✅ Unityチュートリアルを試す：ヘルプ → Unity Manual
6. ✅ テストプロジェクトをコースリポジトリに保存
7. ✅ GitHubにコミットしてプッシュ
8. ✅ **BlenderモデルをUnityにインポートする準備完了！**

**推奨される練習:**
- Unity Essentialsチュートリアルを完了：https://learn.unity.com/pathway/unity-essentials
- YouTubeで「Unity for Beginners」ビデオを見る
- Week 3講義で基本的なC#スクリプティングを練習

---

## Additional Resources / 追加リソース

### English
- **Unity Manual:** https://docs.unity3d.com/Manual/
- **Unity Learn Platform:** https://learn.unity.com/
- **Unity Scripting API:** https://docs.unity3d.com/ScriptReference/
- **Brackeys YouTube Tutorials:** https://www.youtube.com/@Brackeys (beginner-friendly)
- **Unity Forum:** https://forum.unity.com/
- **r/Unity3D Community:** https://www.reddit.com/r/Unity3D/

### 日本語
- **Unityマニュアル（日本語）:** https://docs.unity3d.com/ja/current/Manual/
- **Unity Learn Platform:** https://learn.unity.com/ （英語）
- **Unityスクリプティング API:** https://docs.unity3d.com/ja/current/ScriptReference/
- **Brackeys YouTubeチュートリアル:** https://www.youtube.com/@Brackeys （初心者向け、英語）
- **Unityフォーラム:** https://forum.unity.com/ （英語）
- **r/Unity3Dコミュニティ:** https://www.reddit.com/r/Unity3D/ （英語）

---

## Help and Support / ヘルプとサポート

### English
If you encounter any issues with Unity setup:
1. Check the Troubleshooting section above
2. Ask classmates (collaboration is encouraged!)
3. Post in the course discussion forum
4. Contact the instructor
5. Unity Answers: https://answers.unity.com/
6. Unity Learn Support: https://support.unity.com/

**Remember:** Unity has a learning curve, but millions of developers use it successfully. Be patient, practice, and don't hesitate to ask for help!

### 日本語
Unityのセットアップで問題が発生した場合:
1. 上記のトラブルシューティングセクションを確認
2. クラスメートに聞く（協力が推奨されます！）
3. コースディスカッションフォーラムに投稿
4. インストラクターに連絡
5. Unity Answers: https://answers.unity.com/
6. Unity Learnサポート: https://support.unity.com/

**覚えておいてください:** Unityには学習曲線がありますが、何百万人もの開発者が成功裏に使用しています。忍耐強く、練習し、助けを求めることをためらわないでください！

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
