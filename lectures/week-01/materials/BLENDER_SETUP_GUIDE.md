# Blender Installation & Setup Guide / Blenderインストール＆セットアップガイド
**Developer / 開発者:** Yuri Tijerino

---

## Introduction / 紹介

### English
Blender is a free, open-source 3D creation suite that supports 3D modeling, animation, rendering, and more. In this course, you'll use Blender to:
- Create 3D models for game environments
- Design game objects and characters
- Build complete game levels
- Export models to Unity3D

This guide will walk you through installing and setting up Blender 4.0+ for this course in about 10-15 minutes.

**What You'll Learn:**
- How to download and install Blender
- Initial configuration for game development
- Basic interface navigation
- Essential shortcuts and settings

### 日本語
Blenderは、3Dモデリング、アニメーション、レンダリングなどをサポートする無料のオープンソース3D作成スイートです。このコースでは、Blenderを以下のために使用します：
- ゲーム環境用の3Dモデルを作成
- ゲームオブジェクトとキャラクターをデザイン
- 完全なゲームレベルを構築
- モデルをUnity3Dにエクスポート

このガイドでは、約10〜15分でこのコース用のBlender 4.0+のインストールとセットアップを説明します。

**学ぶこと:**
- Blenderのダウンロードとインストール方法
- ゲーム開発のための初期設定
- 基本的なインターフェースナビゲーション
- 必須のショートカットと設定

---

## System Requirements / システム要件

### English

**Minimum Requirements:**
- **OS:** Windows 10/11, macOS 10.13+, or Linux
- **CPU:** 64-bit quad core CPU
- **RAM:** 8 GB
- **Graphics:** 2 GB VRAM, OpenGL 4.3 compatible
- **Display:** 1920x1080 resolution
- **Storage:** 500 MB for installation

**Recommended Requirements:**
- **CPU:** 64-bit eight core CPU
- **RAM:** 16 GB or more
- **Graphics:** 4 GB VRAM or more, NVIDIA or AMD GPU
- **Display:** 2560x1440 or higher
- **Mouse:** 3-button mouse or trackpad with gesture support

### 日本語

**最小要件:**
- **OS:** Windows 10/11、macOS 10.13+、またはLinux
- **CPU:** 64ビットクアッドコアCPU
- **RAM:** 8 GB
- **グラフィックス:** 2 GB VRAM、OpenGL 4.3互換
- **ディスプレイ:** 1920x1080解像度
- **ストレージ:** インストールに500 MB

**推奨要件:**
- **CPU:** 64ビットオクタコアCPU
- **RAM:** 16 GB以上
- **グラフィックス:** 4 GB VRAM以上、NVIDIAまたはAMD GPU
- **ディスプレイ:** 2560x1440以上
- **マウス:** 3ボタンマウスまたはジェスチャーサポート付きトラックパッド

---

## Step 1: Download Blender / ステップ1：Blenderをダウンロード

### English

1. **Visit the official Blender website:**
   - Go to https://www.blender.org/download/

2. **Choose your operating system:**
   - The website automatically detects your OS
   - Click the large **"Download Blender 4.3"** button (or latest version)
   - **Windows:** Downloads a `.msi` installer or `.zip` portable version
   - **Mac:** Downloads a `.dmg` disk image
   - **Linux:** Choose your distribution (Snap, Flatpak, or direct download)

3. **Alternative: Download LTS (Long Term Support) Version:**
   - Scroll down to find "Long Term Support" section
   - Blender 4.2 LTS is recommended for stability
   - Click the appropriate download button for your OS

4. **Wait for download to complete:**
   - File size: approximately 200-300 MB
   - Save to your Downloads folder

**Note:** For this course, Blender 4.0 or higher is required. Version 4.2 LTS or 4.3+ are recommended.

### 日本語

1. **公式Blenderウェブサイトにアクセス:**
   - https://www.blender.org/download/ にアクセス

2. **オペレーティングシステムを選択:**
   - ウェブサイトが自動的にOSを検出します
   - 大きな **「Download Blender 4.3」** ボタン（または最新バージョン）をクリック
   - **Windows:** `.msi`インストーラーまたは`.zip`ポータブルバージョンをダウンロード
   - **Mac:** `.dmg`ディスクイメージをダウンロード
   - **Linux:** ディストリビューションを選択（Snap、Flatpak、または直接ダウンロード）

3. **代替：LTS（長期サポート）バージョンをダウンロード:**
   - 下にスクロールして「Long Term Support」セクションを見つける
   - 安定性のためにBlender 4.2 LTSを推奨
   - OS用の適切なダウンロードボタンをクリック

4. **ダウンロードが完了するまで待つ:**
   - ファイルサイズ：約200〜300 MB
   - Downloadsフォルダに保存

**注意:** このコースでは、Blender 4.0以上が必要です。バージョン4.2 LTSまたは4.3+を推奨します。

---

## Step 2: Install Blender / ステップ2：Blenderをインストール

### For Windows / Windows用

#### English
1. **Locate the downloaded file:** `blender-4.x.x-windows-x64.msi`
2. **Double-click to run the installer**
3. **Windows SmartScreen may appear:**
   - Click "More info" → "Run anyway"
4. **Follow the installation wizard:**
   - Click "Next" on the welcome screen
   - Accept the End User License Agreement
   - Choose installation location:
     - Default: `C:\Program Files\Blender Foundation\Blender 4.x`
     - Or choose custom location with enough space (1 GB recommended)
   - Select components to install (keep defaults)
   - Choose whether to create desktop shortcut (recommended)
5. **Click "Install"**
6. **Wait for installation to complete (2-3 minutes)**
7. **Click "Finish"**
   - Check "Launch Blender" to start immediately

#### 日本語
1. **ダウンロードしたファイルを見つける:** `blender-4.x.x-windows-x64.msi`
2. **ダブルクリックしてインストーラーを実行**
3. **Windows SmartScreenが表示される場合:**
   - 「詳細情報」→「実行」をクリック
4. **インストールウィザードに従う:**
   - ウェルカム画面で「次へ」をクリック
   - エンドユーザーライセンス契約に同意
   - インストール場所を選択:
     - デフォルト: `C:\Program Files\Blender Foundation\Blender 4.x`
     - または十分なスペースのあるカスタム場所（1 GB推奨）
   - インストールするコンポーネントを選択（デフォルトのまま）
   - デスクトップショートカットを作成するかどうかを選択（推奨）
5. **「インストール」をクリック**
6. **インストールが完了するまで待つ（2〜3分）**
7. **「完了」をクリック**
   - すぐに起動するには「Launch Blender」にチェック

---

### For Mac / Mac用

#### English
1. **Locate the downloaded file:** `blender-4.x.x-macos-arm64.dmg` (Apple Silicon) or `blender-4.x.x-macos-x64.dmg` (Intel)
2. **Double-click the `.dmg` file to open it**
3. **Drag the Blender icon to the Applications folder**
   - This installs Blender on your Mac
4. **Eject the Blender disk image**
   - Right-click the disk image on desktop → "Eject"
   - Or drag it to the Trash
5. **Open Applications folder**
6. **First launch security:**
   - Find Blender in Applications
   - **Right-click** (or Control+click) on Blender → Select "Open"
   - macOS will warn: "Blender is an app downloaded from the internet"
   - Click "Open" to confirm
   - This only needs to be done the first time
7. **Blender will launch**

**Note for Apple Silicon (M1/M2/M3) Macs:**
- Download the ARM64 version for best performance
- The Intel version will work but runs slower through Rosetta 2

#### 日本語
1. **ダウンロードしたファイルを見つける:** `blender-4.x.x-macos-arm64.dmg`（Apple Silicon）または`blender-4.x.x-macos-x64.dmg`（Intel）
2. **`.dmg`ファイルをダブルクリックして開く**
3. **BlenderアイコンをApplicationsフォルダにドラッグ**
   - これによりBlenderがMacにインストールされます
4. **Blenderディスクイメージを取り出す**
   - デスクトップのディスクイメージを右クリック →「取り出す」
   - またはゴミ箱にドラッグ
5. **Applicationsフォルダを開く**
6. **初回起動時のセキュリティ:**
   - ApplicationsでBlenderを見つける
   - Blenderを**右クリック**（またはControl+クリック）→「開く」を選択
   - macOSが警告：「Blenderはインターネットからダウンロードされたアプリです」
   - 「開く」をクリックして確認
   - これは初回のみ行う必要があります
7. **Blenderが起動します**

**Apple Silicon（M1/M2/M3）Mac向けの注意:**
- 最高のパフォーマンスのためにARM64バージョンをダウンロード
- Intelバージョンも動作しますが、Rosetta 2を通じて遅くなります

---

### For Linux / Linux用

#### English

**Option A: Using Snap (Recommended for Ubuntu/Debian):**
```bash
sudo snap install blender --classic
```

**Option B: Using Flatpak:**
```bash
flatpak install flathub org.blender.Blender
```

**Option C: Direct Download (.tar.xz):**
1. Download the `.tar.xz` file from blender.org
2. Extract the archive:
```bash
cd ~/Downloads
tar -xf blender-4.x.x-linux-x64.tar.xz
```
3. Move to `/opt/` or your preferred location:
```bash
sudo mv blender-4.x.x-linux-x64 /opt/blender
```
4. Create a symbolic link (optional):
```bash
sudo ln -s /opt/blender/blender /usr/local/bin/blender
```
5. Launch from terminal:
```bash
blender
```

**Option D: Distribution Package Manager:**
- **Arch Linux:** `sudo pacman -S blender`
- **Fedora:** `sudo dnf install blender`
- **Debian/Ubuntu:** `sudo apt install blender`
  - Note: Repo versions may be older

#### 日本語

**オプションA：Snapを使用（Ubuntu/Debian推奨）:**
```bash
sudo snap install blender --classic
```

**オプションB：Flatpakを使用:**
```bash
flatpak install flathub org.blender.Blender
```

**オプションC：直接ダウンロード（.tar.xz）:**
1. blender.orgから`.tar.xz`ファイルをダウンロード
2. アーカイブを展開:
```bash
cd ~/Downloads
tar -xf blender-4.x.x-linux-x64.tar.xz
```
3. `/opt/`または好みの場所に移動:
```bash
sudo mv blender-4.x.x-linux-x64 /opt/blender
```
4. シンボリックリンクを作成（オプション）:
```bash
sudo ln -s /opt/blender/blender /usr/local/bin/blender
```
5. ターミナルから起動:
```bash
blender
```

**オプションD：ディストリビューションパッケージマネージャー:**
- **Arch Linux:** `sudo pacman -S blender`
- **Fedora:** `sudo dnf install blender`
- **Debian/Ubuntu:** `sudo apt install blender`
  - 注意：リポジトリのバージョンは古い場合があります

---

## Step 3: First Launch & Initial Setup / ステップ3：初回起動と初期セットアップ

### English

When you launch Blender for the first time:

1. **Splash Screen Appears:**
   - Shows the Blender version and news
   - **Click anywhere to dismiss** or wait a few seconds

2. **Quick Setup Dialog:**
   If this appears, configure the following:

   **Language / 言語:**
   - Select "English" (or "日本語" if you prefer Japanese interface)

   **Shortcuts:**
   - Select **"Blender"** (recommended for this course)
   - Alternative: "Industry Compatible" (similar to Maya/3ds Max)

   **Theme:**
   - Select **"Blender Dark"** (recommended - easier on eyes)
   - Alternative: "Blender Light"

   **Select With:**
   - Keep as **"Left Click"** (default and recommended)

   **Spacebar Action:**
   - Set to **"Play"** (recommended for this course)
   - This makes Spacebar start/stop animations

3. **Click "Next"** and then **"Save Preferences"**

4. **You'll see the default Blender workspace with:**
   - Default cube in the center
   - Camera
   - Light source
   - 3D viewport

### 日本語

Blenderを初めて起動すると：

1. **スプラッシュ画面が表示されます:**
   - Blenderバージョンとニュースが表示されます
   - **どこかをクリックして閉じる**か、数秒待つ

2. **クイックセットアップダイアログ:**
   これが表示された場合、以下を設定:

   **Language / 言語:**
   - 「English」を選択（または日本語インターフェースが好みなら「日本語」）

   **Shortcuts:**
   - **「Blender」**を選択（このコースに推奨）
   - 代替：「Industry Compatible」（MayaとMAX/3ds Maxに類似）

   **Theme:**
   - **「Blender Dark」**を選択（推奨 - 目に優しい）
   - 代替：「Blender Light」

   **Select With:**
   - **「Left Click」**のままにする（デフォルトで推奨）

   **Spacebar Action:**
   - **「Play」**に設定（このコースに推奨）
   - これによりスペースバーでアニメーションが開始/停止します

3. **「Next」をクリックしてから「Save Preferences」をクリック**

4. **デフォルトのBlenderワークスペースが表示されます:**
   - 中央にデフォルトキューブ
   - カメラ
   - ライトソース
   - 3Dビューポート

---

## Step 4: Interface Overview / ステップ4：インターフェースの概要

### English

Understanding Blender's interface is crucial. Here are the main areas:

**1. 3D Viewport (Center):**
- Main working area where you create 3D models
- Contains grid floor, camera, lights, and objects
- This is where you'll spend most of your time

**2. Outliner (Top Right):**
- Shows hierarchy of all objects in your scene
- Click to select objects
- Click the eye icon to hide/show objects

**3. Properties Panel (Bottom Right):**
- Shows properties of selected object
- Tabs for different settings (Object, Modifier, Material, etc.)
- Used to configure object details

**4. Timeline (Bottom):**
- For animations (we'll use this later in the course)
- Shows frame numbers and keyframes

**5. Top Menu Bar:**
- File, Edit, Render, Window, Help
- Access to all major functions

**6. Tool Shelf (Left Side):**
- Contains tools for modeling
- Select, Move, Rotate, Scale, and more

**Navigation Tips:**
- **Middle Mouse Button (MMB):** Rotate view by dragging
- **Shift + MMB:** Pan view (move sideways)
- **Scroll Wheel:** Zoom in/out
- **Trackpad Users:** Two-finger drag to rotate, pinch to zoom

### 日本語

Blenderのインターフェースを理解することは非常に重要です。主なエリアは以下です：

**1. 3Dビューポート（中央）:**
- 3Dモデルを作成するメインの作業エリア
- グリッド床、カメラ、ライト、オブジェクトが含まれます
- ここでほとんどの時間を過ごします

**2. アウトライナー（右上）:**
- シーン内のすべてのオブジェクトの階層を表示
- クリックしてオブジェクトを選択
- 目のアイコンをクリックしてオブジェクトを非表示/表示

**3. プロパティパネル（右下）:**
- 選択されたオブジェクトのプロパティを表示
- 異なる設定のタブ（オブジェクト、モディファイア、マテリアルなど）
- オブジェクトの詳細を設定するために使用

**4. タイムライン（下部）:**
- アニメーション用（コースの後半で使用します）
- フレーム番号とキーフレームを表示

**5. トップメニューバー:**
- ファイル、編集、レンダリング、ウィンドウ、ヘルプ
- すべての主要機能へのアクセス

**6. ツールシェルフ（左側）:**
- モデリング用のツールを含む
- 選択、移動、回転、スケールなど

**ナビゲーションのヒント:**
- **マウス中ボタン（MMB）:** ドラッグでビューを回転
- **Shift + MMB:** ビューをパン（横に移動）
- **スクロールホイール:** ズームイン/アウト
- **トラックパッドユーザー:** 2本指ドラッグで回転、ピンチでズーム

---

## Step 5: Essential Settings for Game Development / ステップ5：ゲーム開発のための必須設定

### English

Let's configure Blender for game development:

**1. Enable Auto Save:**
- Go to **Edit → Preferences** (or **Blender → Preferences** on Mac)
- Click **"Save & Load"** on the left
- Enable **"Auto Save"**
- Set **"Auto Save Time"** to **2 minutes**
- Click the **☰** menu → **"Save Preferences"**

**2. Set Units to Metric:**
- In the **Properties Panel** (bottom right), find the **Scene Properties** tab (looks like a scene icon)
- Expand **"Units"** section
- Set **"Unit System"** to **"Metric"**
- Set **"Length"** to **"Meters"**
- This matches Unity's default unit system

**3. Enable Screencast Keys (Optional but Helpful):**
- Go to **Edit → Preferences → Add-ons**
- Search for **"Screencast Keys"**
- Check the box to enable it
- This shows which keys you're pressing (helpful for learning)

**4. Enable Node Wrangler (Helpful for Materials):**
- In **Edit → Preferences → Add-ons**
- Search for **"Node Wrangler"**
- Check the box to enable it
- Provides shortcuts for working with materials

**5. Increase Undo Steps:**
- In **Edit → Preferences → System**
- Find **"Undo Steps"**
- Increase to **64** (default is 32)
- Allows more undo history

**6. Save Preferences:**
- Click the **☰** menu at bottom left of Preferences window
- Select **"Save Preferences"**

### 日本語

ゲーム開発用にBlenderを設定しましょう：

**1. 自動保存を有効化:**
- **編集 → プリファレンス**（またはMacでは**Blender → プリファレンス**）に移動
- 左側の**「保存とロード」**をクリック
- **「自動保存」**を有効化
- **「自動保存時間」**を**2分**に設定
- **☰**メニュー → **「プリファレンスを保存」**をクリック

**2. 単位をメートル法に設定:**
- **プロパティパネル**（右下）で、**シーンプロパティ**タブ（シーンアイコンのように見える）を見つける
- **「単位」**セクションを展開
- **「単位系」**を**「メートル法」**に設定
- **「長さ」**を**「メートル」**に設定
- これはUnityのデフォルト単位系と一致します

**3. スクリーンキャストキーを有効化（オプションだが役立つ）:**
- **編集 → プリファレンス → アドオン**に移動
- **「Screencast Keys」**を検索
- チェックボックスをオンにして有効化
- 押しているキーが表示されます（学習に役立ちます）

**4. Node Wranglerを有効化（マテリアルに役立つ）:**
- **編集 → プリファレンス → アドオン**で
- **「Node Wrangler」**を検索
- チェックボックスをオンにして有効化
- マテリアル作業のためのショートカットを提供

**5. 元に戻すステップを増やす:**
- **編集 → プリファレンス → システム**で
- **「元に戻すステップ」**を見つける
- **64**に増やす（デフォルトは32）
- より多くの元に戻す履歴を許可

**6. プリファレンスを保存:**
- プリファレンスウィンドウの左下の**☰**メニューをクリック
- **「プリファレンスを保存」**を選択

---

## Step 6: Basic Navigation Practice / ステップ6：基本的なナビゲーション練習

### English

Let's practice navigating in Blender:

**1. Select the Default Cube:**
- **Left-click** on the cube (it should highlight in orange)

**2. Delete the Cube:**
- Press **X** key
- Select "Delete" from the menu
- The cube disappears

**3. Add a New Object:**
- Press **Shift + A** (Add menu appears)
- Select **Mesh → UV Sphere**
- A sphere appears at the center

**4. Move the Camera View:**
- Hold **Middle Mouse Button** and drag to rotate view
- **Scroll wheel** to zoom in/out
- **Shift + Middle Mouse Button** to pan

**5. Reset View:**
- Press **Numpad 7** for top view
- Press **Numpad 1** for front view
- Press **Numpad 3** for right side view
- Press **Numpad 0** for camera view

**No Numpad?**
- Enable Emulate Numpad:
  - Edit → Preferences → Input
  - Check "Emulate Numpad"
  - Now use regular numbers (not numpad) for view shortcuts

**6. Frame Selected Object:**
- Select an object
- Press **Numpad Period (.)** or View → Frame Selected
- Camera centers on the object

**7. Undo/Redo:**
- **Ctrl + Z:** Undo
- **Ctrl + Shift + Z:** Redo

### 日本語

Blenderでのナビゲーションを練習しましょう：

**1. デフォルトキューブを選択:**
- キューブを**左クリック**（オレンジ色でハイライトされるはず）

**2. キューブを削除:**
- **X**キーを押す
- メニューから「削除」を選択
- キューブが消えます

**3. 新しいオブジェクトを追加:**
- **Shift + A**を押す（追加メニューが表示されます）
- **メッシュ → UV球**を選択
- 中央に球が表示されます

**4. カメラビューを移動:**
- **マウス中ボタン**を押しながらドラッグしてビューを回転
- **スクロールホイール**でズームイン/アウト
- **Shift +マウス中ボタン**でパン

**5. ビューをリセット:**
- **テンキー7**で上面ビュー
- **テンキー1**で正面ビュー
- **テンキー3**で右側面ビュー
- **テンキー0**でカメラビュー

**テンキーがない？**
- テンキーエミュレートを有効化:
  - 編集 → プリファレンス → 入力
  - 「テンキーをエミュレート」にチェック
  - これで通常の数字（テンキーではない）をビューショートカットに使用できます

**6. 選択したオブジェクトをフレーム:**
- オブジェクトを選択
- **テンキーのピリオド（.）**を押すか、ビュー → 選択をフレームに収める
- カメラがオブジェクトの中心に移動します

**7. 元に戻す/やり直し:**
- **Ctrl + Z:** 元に戻す
- **Ctrl + Shift + Z:** やり直す

---

## Essential Blender Shortcuts / 必須のBlenderショートカット

### English

Memorize these essential shortcuts for efficient workflow:

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Add Object** | Shift + A | Opens add menu for meshes, lights, cameras |
| **Delete** | X | Delete selected object |
| **Select** | Left Click | Select object |
| **Select All** | A | Select all objects |
| **Deselect All** | Alt + A | Deselect everything |
| **Grab/Move** | G | Move selected object (then X/Y/Z to constrain to axis) |
| **Rotate** | R | Rotate selected object (then X/Y/Z for axis) |
| **Scale** | S | Scale selected object (then X/Y/Z for axis) |
| **Duplicate** | Shift + D | Duplicate selected object |
| **Tab** | Tab | Toggle Edit Mode / Object Mode |
| **Save** | Ctrl + S | Save current file |
| **Undo** | Ctrl + Z | Undo last action |
| **Search** | F3 | Search for any command |
| **Render** | F12 | Render current scene |

**Pro Tips:**
- After pressing G, R, or S, type a number to set exact values
  - Example: G → Z → 2 → Enter (moves object 2 units up on Z axis)
- Press the axis key twice to use local orientation
  - Example: G → Z → Z (moves along object's local Z axis)

### 日本語

効率的なワークフローのために、これらの必須ショートカットを覚えましょう：

| アクション | ショートカット | 説明 |
|--------|----------|-------------|
| **オブジェクトを追加** | Shift + A | メッシュ、ライト、カメラの追加メニューを開く |
| **削除** | X | 選択したオブジェクトを削除 |
| **選択** | 左クリック | オブジェクトを選択 |
| **すべて選択** | A | すべてのオブジェクトを選択 |
| **すべて選択解除** | Alt + A | すべての選択を解除 |
| **グラブ/移動** | G | 選択したオブジェクトを移動（その後X/Y/Zで軸に制約） |
| **回転** | R | 選択したオブジェクトを回転（その後X/Y/Zで軸） |
| **スケール** | S | 選択したオブジェクトをスケール（その後X/Y/Zで軸） |
| **複製** | Shift + D | 選択したオブジェクトを複製 |
| **タブ** | Tab | 編集モード/オブジェクトモードを切り替え |
| **保存** | Ctrl + S | 現在のファイルを保存 |
| **元に戻す** | Ctrl + Z | 最後のアクションを元に戻す |
| **検索** | F3 | 任意のコマンドを検索 |
| **レンダー** | F12 | 現在のシーンをレンダリング |

**プロのヒント:**
- G、R、またはSを押した後、数字を入力して正確な値を設定
  - 例：G → Z → 2 → Enter（Z軸で2単位上に移動）
- 軸キーを2回押してローカル方向を使用
  - 例：G → Z → Z（オブジェクトのローカルZ軸に沿って移動）

---

## Step 7: Create Your First Save File / ステップ7：最初の保存ファイルを作成

### English

Let's save your first Blender file:

1. **Prepare Your Workspace:**
   - Create a `week-01` folder in your course repository (if not already created)
   - This is where you'll save Blender files for Week 1

2. **Save Your Blender File:**
   - Go to **File → Save As...**
   - Navigate to your course repository: `game-dev-2025-yourname/week-01/`
   - Name your file: `test-scene.blend`
   - Click **"Save As"**

3. **Verify Auto-Save is Working:**
   - Make a change (add an object: Shift + A → Mesh → Cube)
   - Wait 2 minutes
   - Check that auto-save created a backup file (Blender automatically saves backup files with `.blend1` extension)

**Blender File Tips:**
- `.blend` files contain your entire scene (objects, materials, lights, etc.)
- Always save frequently (Ctrl + S)
- Blender creates automatic backups (`.blend1`, `.blend2`)
- Your `.gitignore` should already exclude backup files from Git

### 日本語

最初のBlenderファイルを保存しましょう：

1. **ワークスペースを準備:**
   - コースリポジトリに`week-01`フォルダを作成（まだ作成していない場合）
   - これはWeek 1のBlenderファイルを保存する場所です

2. **Blenderファイルを保存:**
   - **ファイル → 名前を付けて保存...**に移動
   - コースリポジトリに移動：`game-dev-2025-yourname/week-01/`
   - ファイルに名前を付ける：`test-scene.blend`
   - **「名前を付けて保存」**をクリック

3. **自動保存が機能していることを確認:**
   - 変更を加える（オブジェクトを追加：Shift + A → メッシュ → 立方体）
   - 2分待つ
   - 自動保存がバックアップファイルを作成したことを確認（Blenderは自動的に`.blend1`拡張子でバックアップファイルを保存）

**Blenderファイルのヒント:**
- `.blend`ファイルにはシーン全体（オブジェクト、マテリアル、ライトなど）が含まれます
- 常に頻繁に保存（Ctrl + S）
- Blenderは自動バックアップを作成（`.blend1`、`.blend2`）
- `.gitignore`はすでにGitからバックアップファイルを除外しているはず

---

## Troubleshooting / トラブルシューティング

### Problem: Blender won't launch / 問題：Blenderが起動しない

**English:**
- **Solution 1:** Check system requirements (8GB RAM minimum, OpenGL 4.3 compatible graphics)
- **Solution 2:** Update graphics drivers
  - **Windows:** Visit your GPU manufacturer's website (NVIDIA, AMD, Intel)
  - **Mac:** Update macOS to latest version
- **Solution 3:** Try launching in safe mode:
  - Hold **Shift** while launching Blender
  - Disables add-ons that might cause issues
- **Solution 4:** Reinstall Blender

**日本語:**
- **解決策1:** システム要件を確認（最小8GB RAM、OpenGL 4.3互換グラフィックス）
- **解決策2:** グラフィックスドライバを更新
  - **Windows:** GPUメーカーのウェブサイトにアクセス（NVIDIA、AMD、Intel）
  - **Mac:** macOSを最新バージョンに更新
- **解決策3:** セーフモードで起動してみる:
  - Blenderを起動する際に**Shift**を押し続ける
  - 問題を引き起こす可能性のあるアドオンを無効化
- **解決策4:** Blenderを再インストール

---

### Problem: Interface is too small or too large / 問題：インターフェースが小さすぎるまたは大きすぎる

**English:**
- **Solution:**
  - Go to **Edit → Preferences → Interface**
  - Adjust **"Resolution Scale"** (try 1.0 for default, 1.2 for larger, 0.8 for smaller)
  - Adjust **"Line Width"** for thicker or thinner lines
  - Click Save Preferences

**日本語:**
- **解決策:**
  - **編集 → プリファレンス → インターフェース**に移動
  - **「解像度スケール」**を調整（デフォルトには1.0、大きい場合は1.2、小さい場合は0.8を試す）
  - より太い/細い線には**「線の幅」**を調整
  - プリファレンスを保存をクリック

---

### Problem: Can't navigate with trackpad / 問題：トラックパッドでナビゲートできない

**English:**
- **Solution:**
  - Go to **Edit → Preferences → Input**
  - Enable **"Emulate 3 Button Mouse"**
  - Now:
    - **Alt + Left Click Drag:** Rotate view
    - **Shift + Alt + Left Click Drag:** Pan view
    - **Two-finger scroll:** Zoom (if supported)

**日本語:**
- **解決策:**
  - **編集 → プリファレンス → 入力**に移動
  - **「3ボタンマウスをエミュレート」**を有効化
  - これで:
    - **Alt +左クリックドラッグ:** ビューを回転
    - **Shift + Alt +左クリックドラッグ:** ビューをパン
    - **2本指スクロール:** ズーム（サポートされている場合）

---

### Problem: Accidentally changed to wrong view / 問題：誤って間違ったビューに変更した

**English:**
- **Solution:** Press **Numpad 7** (top view) or **Numpad 1** (front view) to reset to standard views
- **Or:** Use the View menu in the 3D Viewport → Front, Top, Right, etc.
- **Or:** Press **~** (tilde key) to open view pie menu

**日本語:**
- **解決策:** **テンキー7**（上面ビュー）または**テンキー1**（正面ビュー）を押して標準ビューにリセット
- **または:** 3Dビューポートのビューメニューを使用 → 正面、上面、右など
- **または:** **~**（チルダキー）を押してビューパイメニューを開く

---

### Problem: Objects disappearing or clipping / 問題：オブジェクトが消えたりクリッピングしたりする

**English:**
- **Solution:** Adjust clipping distance
  - Press **N** to open sidebar
  - Go to **View** tab
  - Under **"View"**, adjust **"Clip Start"** to 0.01 and **"Clip End"** to 10000
  - This prevents objects from being clipped at close or far distances

**日本語:**
- **解決策:** クリッピング距離を調整
  - **N**を押してサイドバーを開く
  - **ビュー**タブに移動
  - **「ビュー」**の下で、**「クリップ開始」**を0.01に、**「クリップ終了」**を10000に調整
  - これにより、近距離または遠距離でオブジェクトがクリッピングされるのを防ぎます

---

### Problem: Blender running slowly / 問題：Blenderの動作が遅い

**English:**
- **Solution 1:** Reduce viewport quality
  - In 3D Viewport, click the **Viewport Shading** icon (top right, looks like spheres)
  - Switch to **"Solid"** mode (default) instead of "Material Preview" or "Rendered"
- **Solution 2:** Disable unnecessary add-ons
  - Edit → Preferences → Add-ons
  - Disable add-ons you don't use
- **Solution 3:** Reduce undo steps
  - Edit → Preferences → System → Undo Steps → Set to 32
- **Solution 4:** Close other applications to free up RAM

**日本語:**
- **解決策1:** ビューポート品質を下げる
  - 3Dビューポートで、**ビューポートシェーディング**アイコン（右上、球のように見える）をクリック
  - 「マテリアルプレビュー」または「レンダリング」ではなく**「ソリッド」**モードに切り替え
- **解決策2:** 不要なアドオンを無効化
  - 編集 → プリファレンス → アドオン
  - 使用しないアドオンを無効化
- **解決策3:** 元に戻すステップを減らす
  - 編集 → プリファレンス → システム → 元に戻すステップ → 32に設定
- **解決策4:** RAMを解放するために他のアプリケーションを閉じる

---

## Next Steps / 次のステップ

### English
Now that Blender is installed and configured:
1. ✅ Familiarize yourself with the interface
2. ✅ Practice basic navigation (rotate, pan, zoom)
3. ✅ Try adding and deleting objects (Shift + A, X)
4. ✅ Practice moving (G), rotating (R), and scaling (S) objects
5. ✅ Save your practice file to your `week-01/` folder
6. ✅ Commit and push to GitHub
7. ✅ Ready to start **Week 1 Assignment: Create a simple maze level!**

**Recommended Practice:**
- Spend 15-30 minutes just navigating and moving objects
- Watch the Quick Start tutorials in Blender: Help → Manual → Quick Start
- Get comfortable with G, R, S shortcuts before starting assignments

### 日本語
Blenderがインストールされ、設定されたので:
1. ✅ インターフェースに慣れる
2. ✅ 基本的なナビゲーションを練習（回転、パン、ズーム）
3. ✅ オブジェクトの追加と削除を試す（Shift + A、X）
4. ✅ オブジェクトの移動（G）、回転（R）、スケール（S）を練習
5. ✅ 練習ファイルを`week-01/`フォルダに保存
6. ✅ GitHubにコミットしてプッシュ
7. ✅ **Week 1課題の準備完了：シンプルな迷路レベルを作成！**

**推奨される練習:**
- 15〜30分間、ナビゲートとオブジェクトの移動だけを練習
- Blenderのクイックスタートチュートリアルを見る：ヘルプ → マニュアル → クイックスタート
- 課題を始める前にG、R、Sショートカットに慣れる

---

## Additional Resources / 追加リソース

### English
- **Official Blender Manual:** https://docs.blender.org/manual/en/latest/
- **Blender Fundamentals (Video Series):** https://www.youtube.com/playlist?list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6
- **Blender Guru (Beginner Tutorial):** https://www.youtube.com/watch?v=nIoXOplUvAw
- **Blender Hotkey Cheat Sheet:** https://www.blender.org/support/
- **Blender Stack Exchange:** https://blender.stackexchange.com/
- **r/blender Community:** https://www.reddit.com/r/blender/

### 日本語
- **公式Blenderマニュアル（日本語）:** https://docs.blender.org/manual/ja/latest/
- **Blender基礎（ビデオシリーズ）:** https://www.youtube.com/playlist?list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6 （英語）
- **Blender Guru（初心者チュートリアル）:** https://www.youtube.com/watch?v=nIoXOplUvAw （英語、日本語字幕あり）
- **Blenderホットキーチートシート:** https://www.blender.org/support/
- **Blender Stack Exchange:** https://blender.stackexchange.com/ （英語）
- **r/blenderコミュニティ:** https://www.reddit.com/r/blender/ （英語）

---

## Help and Support / ヘルプとサポート

### English
If you encounter any issues with Blender setup:
1. Check the Troubleshooting section above
2. Ask classmates (collaboration is encouraged!)
3. Post in the course discussion forum
4. Contact the instructor
5. Blender Community: https://www.blender.org/community/
6. Blender Artists Forum: https://blenderartists.org/

**Remember:** Blender has a learning curve, but with practice, you'll become proficient. Don't give up!

### 日本語
Blenderのセットアップで問題が発生した場合:
1. 上記のトラブルシューティングセクションを確認
2. クラスメートに聞く（協力が推奨されます！）
3. コースディスカッションフォーラムに投稿
4. インストラクターに連絡
5. Blenderコミュニティ: https://www.blender.org/community/
6. Blender Artistsフォーラム: https://blenderartists.org/

**覚えておいてください:** Blenderには学習曲線がありますが、練習すれば熟達できます。諦めないでください！

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
