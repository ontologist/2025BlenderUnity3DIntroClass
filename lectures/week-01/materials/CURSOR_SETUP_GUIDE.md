# Cursor Editor Setup Guide / Cursor エディタセットアップガイド
**Developer / 開発者:** Yuri Tijerino

---

## Introduction / 紹介

### English
Cursor is an AI-powered code editor built on VS Code that will help you write and understand code for Unity3D. It provides intelligent code completion, explanations, and assistance - perfect for learning game development!

**Key Features for This Course:**
- AI-powered code completion and suggestions
- Natural language code explanations
- Built-in terminal for Git commands
- C# language support for Unity scripting
- GitHub integration

### 日本語
CursorはVS Codeをベースにした AI搭載のコードエディタで、Unity3D用のコードを書き、理解するのに役立ちます。インテリジェントなコード補完、説明、アシスタンスを提供し、ゲーム開発の学習に最適です！

**このコースの主な機能:**
- AI搭載のコード補完と提案
- 自然言語によるコード説明
- Gitコマンド用の組み込みターミナル
- UnityスクリプティングのためのC#言語サポート
- GitHub統合

---

## Step 1: Download Cursor / ステップ1：Cursorをダウンロード

### English

1. **Visit the Cursor website:**
   - Go to https://www.cursor.com

2. **Download for your operating system:**
   - **Windows:** Click "Download for Windows"
   - **Mac:** Click "Download for Mac"
     - For Apple Silicon (M1/M2/M3): Download ARM version
     - For Intel Macs: Download Intel version
   - **Linux:** Click "Download for Linux"

3. **Wait for download to complete**
   - File size is approximately 100-150 MB
   - Save to your Downloads folder

### 日本語

1. **Cursorウェブサイトにアクセス:**
   - https://www.cursor.com にアクセス

2. **オペレーティングシステム用にダウンロード:**
   - **Windows:** 「Download for Windows」をクリック
   - **Mac:** 「Download for Mac」をクリック
     - Apple Silicon（M1/M2/M3）の場合：ARMバージョンをダウンロード
     - Intel Macの場合：Intelバージョンをダウンロード
   - **Linux:** 「Download for Linux」をクリック

3. **ダウンロードが完了するまで待つ**
   - ファイルサイズは約100-150 MB
   - Downloadsフォルダに保存

---

## Step 2: Install Cursor / ステップ2：Cursorをインストール

### For Windows / Windows用

#### English
1. Locate the downloaded file: `CursorSetup.exe`
2. Double-click to run the installer
3. If Windows SmartScreen appears, click "More info" → "Run anyway"
4. Follow the installation wizard:
   - Accept the license agreement
   - Choose installation location (default is fine)
   - Select "Create a desktop shortcut" if desired
5. Click "Install"
6. Wait for installation to complete (1-2 minutes)
7. Click "Finish" to launch Cursor

#### 日本語
1. ダウンロードしたファイルを見つける：`CursorSetup.exe`
2. ダブルクリックしてインストーラーを実行
3. Windows SmartScreenが表示された場合、「詳細情報」→「実行」をクリック
4. インストールウィザードに従う：
   - ライセンス契約に同意
   - インストール場所を選択（デフォルトで問題なし）
   - 必要に応じて「デスクトップショートカットを作成」を選択
5. 「インストール」をクリック
6. インストールが完了するまで待つ（1〜2分）
7. 「完了」をクリックしてCursorを起動

---

### For Mac / Mac用

#### English
1. Locate the downloaded file: `Cursor.dmg`
2. Double-click to open the disk image
3. Drag the Cursor icon to the Applications folder
4. Eject the Cursor disk image
5. Open Applications folder
6. Double-click Cursor to launch
7. If macOS says "Cursor cannot be opened because it is from an unidentified developer":
   - Right-click Cursor → "Open"
   - Click "Open" in the dialog
   - This only needs to be done once

#### 日本語
1. ダウンロードしたファイルを見つける：`Cursor.dmg`
2. ダブルクリックしてディスクイメージを開く
3. CursorアイコンをApplicationsフォルダにドラッグ
4. Cursorディスクイメージを取り出す
5. Applicationsフォルダを開く
6. Cursorをダブルクリックして起動
7. macOSが「Cursorは識別されていない開発者のため開けません」と表示した場合：
   - Cursorを右クリック →「開く」
   - ダイアログで「開く」をクリック
   - これは一度だけ行う必要があります

---

### For Linux / Linux用

#### English
1. Locate the downloaded file: `cursor-*.AppImage` or `cursor-*.deb`
2. **For AppImage:**
   ```bash
   chmod +x cursor-*.AppImage
   ./cursor-*.AppImage
   ```
3. **For .deb (Debian/Ubuntu):**
   ```bash
   sudo dpkg -i cursor-*.deb
   sudo apt-get install -f
   ```
4. Launch from applications menu or command line: `cursor`

#### 日本語
1. ダウンロードしたファイルを見つける：`cursor-*.AppImage`または`cursor-*.deb`
2. **AppImageの場合:**
   ```bash
   chmod +x cursor-*.AppImage
   ./cursor-*.AppImage
   ```
3. **.deb（Debian/Ubuntu）の場合:**
   ```bash
   sudo dpkg -i cursor-*.deb
   sudo apt-get install -f
   ```
4. アプリケーションメニューまたはコマンドラインから起動：`cursor`

---

## Step 3: Initial Setup / ステップ3：初期セットアップ

### English

When you first launch Cursor:

1. **Welcome Screen:**
   - You'll see a welcome screen with options
   - Click "Get Started"

2. **Choose Your Theme:**
   - Select "Dark" (recommended for long coding sessions)
   - Or select "Light" if you prefer
   - You can change this later in Settings

3. **Import Settings (Optional):**
   - If you've used VS Code before, you can import settings
   - Otherwise, click "Skip" or "Start Fresh"

4. **Sign In or Create Account:**
   - **Option A: Sign in with email**
     - Enter your email address
     - Check your email for verification code
     - Enter the code
   - **Option B: Continue without account (Limited features)**
     - You can use Cursor without signing in, but some AI features will be limited

### 日本語

Cursorを初めて起動すると：

1. **ウェルカム画面:**
   - オプション付きのウェルカム画面が表示されます
   - 「Get Started」をクリック

2. **テーマを選択:**
   - 「Dark」を選択（長時間のコーディングセッションに推奨）
   - または好みに応じて「Light」を選択
   - 後で設定で変更できます

3. **設定をインポート（オプション）:**
   - 以前にVS Codeを使用したことがある場合、設定をインポートできます
   - そうでない場合は、「Skip」または「Start Fresh」をクリック

4. **サインインまたはアカウントを作成:**
   - **オプションA：メールでサインイン**
     - メールアドレスを入力
     - 確認コードのためにメールをチェック
     - コードを入力
   - **オプションB：アカウントなしで続行（機能制限あり）**
     - サインインせずにCursorを使用できますが、一部のAI機能が制限されます

---

## Step 4: Get Free Student Pro Plan / ステップ4：無料学生プロプランを取得

### English

**IMPORTANT: As a student, you can get Cursor Pro for FREE!**

**Standard Free Plan:**
- ✅ Basic AI code completion
- ✅ Code explanations
- ✅ Full editor features
- ✅ Git integration
- ✅ C# language support
- ⚠️ Limited AI requests per day (~50)

**Pro Plan ($20/month normally, FREE for students):**
- ✅ Unlimited AI requests
- ✅ Advanced AI models (GPT-4, Claude)
- ✅ Priority support
- ✅ Faster responses
- ✅ More powerful code generation

### How to Get Free Student Pro:

1. **Visit the Student Page:**
   - Go to https://cursor.com/students
   - Click "Apply for Student Plan"

2. **Sign Up/Sign In:**
   - Use your school email address if possible (.edu, .ac.jp, etc.)
   - Or sign up with personal email and verify student status

3. **Verify Your Student Status:**
   - **Option A: School Email**
     - Enter your school email address
     - Cursor will send a verification email
     - Click the verification link

   - **Option B: Upload Student ID/Document**
     - Upload a photo of your student ID
     - Or upload enrollment verification document
     - Make sure the document clearly shows:
       - Your name
       - School name
       - Current enrollment status/date

   - **Option C: Use GitHub Student Developer Pack**
     - If you already have GitHub Student Developer Pack:
     - Connect your GitHub account
     - Cursor will automatically verify

4. **Wait for Approval:**
   - Usually approved within 24-48 hours
   - Check your email for confirmation

5. **Activate Pro Features:**
   - Once approved, restart Cursor
   - Pro features will be automatically enabled
   - Check your account settings to confirm

**Recommendation for this course:** Apply for the FREE Student Pro plan! It will make learning much easier with unlimited AI assistance.

### 日本語

**重要：学生は Cursor Proを無料で利用できます！**

**標準無料プラン:**
- ✅ 基本的なAIコード補完
- ✅ コード説明
- ✅ 完全なエディタ機能
- ✅ Git統合
- ✅ C#言語サポート
- ⚠️ 1日あたりのAIリクエスト制限（約50）

**プロプラン（通常月額$20、学生は無料）:**
- ✅ 無制限のAIリクエスト
- ✅ 高度なAIモデル（GPT-4、Claude）
- ✅ 優先サポート
- ✅ より速い応答
- ✅ より強力なコード生成

### 無料学生プロの取得方法:

1. **学生ページにアクセス:**
   - https://cursor.com/students にアクセス
   - 「Apply for Student Plan」をクリック

2. **サインアップ/サインイン:**
   - 可能であれば学校のメールアドレスを使用（.edu、.ac.jpなど）
   - または個人メールでサインアップして学生ステータスを確認

3. **学生ステータスを確認:**
   - **オプションA：学校のメール**
     - 学校のメールアドレスを入力
     - Cursorが確認メールを送信
     - 確認リンクをクリック

   - **オプションB：学生証/書類をアップロード**
     - 学生証の写真をアップロード
     - または在籍確認書類をアップロード
     - 書類に以下が明確に表示されていることを確認:
       - あなたの名前
       - 学校名
       - 現在の在籍状況/日付

   - **オプションC：GitHub Student Developer Packを使用**
     - すでにGitHub Student Developer Packを持っている場合:
     - GitHubアカウントを接続
     - Cursorが自動的に確認

4. **承認を待つ:**
   - 通常24〜48時間以内に承認
   - 確認メールをチェック

5. **プロ機能を有効化:**
   - 承認されたら、Cursorを再起動
   - プロ機能が自動的に有効になります
   - アカウント設定で確認

**このコースの推奨:** 無料学生プロプランに申し込んでください！無制限のAIサポートで学習がはるかに簡単になります。

---

## Step 5: Install Essential Extensions / ステップ5：必須の拡張機能をインストール

### English

Extensions enhance Cursor's functionality. For Unity development, install these:

1. **Open Extensions View:**
   - Click the Extensions icon in the left sidebar (four squares)
   - Or press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)

2. **Install C# Extension:**
   - Search for "C#"
   - Find "C# Dev Kit" by Microsoft
   - Click "Install"
   - Wait for installation to complete

3. **Install Unity Code Snippets (Optional but Recommended):**
   - Search for "Unity Code Snippets"
   - Find "Unity Code Snippets" by Kleber Silva
   - Click "Install"

4. **Install GitLens (Optional):**
   - Search for "GitLens"
   - Find "GitLens — Git supercharged" by GitKraken
   - Click "Install"
   - Provides enhanced Git integration

### 日本語

拡張機能はCursorの機能を強化します。Unity開発には以下をインストール:

1. **拡張機能ビューを開く:**
   - 左サイドバーの拡張機能アイコン（4つの正方形）をクリック
   - または`Ctrl+Shift+X`（Windows/Linux）または`Cmd+Shift+X`（Mac）を押す

2. **C#拡張機能をインストール:**
   - 「C#」を検索
   - Microsoftの「C# Dev Kit」を見つける
   - 「Install」をクリック
   - インストールが完了するまで待つ

3. **Unity Code Snippetsをインストール（オプションだが推奨）:**
   - 「Unity Code Snippets」を検索
   - Kleber Silvaの「Unity Code Snippets」を見つける
   - 「Install」をクリック

4. **GitLensをインストール（オプション）:**
   - 「GitLens」を検索
   - GitKrakenの「GitLens — Git supercharged」を見つける
   - 「Install」をクリック
   - 強化されたGit統合を提供

---

## Step 6: Configure Cursor for Unity / ステップ6：Unity用にCursorを設定

### English

1. **Open Settings:**
   - Click the gear icon (⚙️) in the bottom left
   - Select "Settings"
   - Or press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)

2. **Configure Auto Save:**
   - Search for "auto save"
   - Set "Files: Auto Save" to "afterDelay"
   - Set "Files: Auto Save Delay" to "1000" (1 second)
   - This ensures your scripts are saved before Unity recompiles

3. **Configure Font Size (Optional):**
   - Search for "font size"
   - Adjust "Editor: Font Size" to your preference (14 is good for beginners)

4. **Configure Tab Size:**
   - Search for "tab size"
   - Set "Editor: Tab Size" to "4" (Unity standard)
   - Enable "Editor: Detect Indentation"

### 日本語

1. **設定を開く:**
   - 左下の歯車アイコン（⚙️）をクリック
   - 「Settings」を選択
   - または`Ctrl+,`（Windows/Linux）または`Cmd+,`（Mac）を押す

2. **自動保存を設定:**
   - 「auto save」を検索
   - 「Files: Auto Save」を「afterDelay」に設定
   - 「Files: Auto Save Delay」を「1000」（1秒）に設定
   - これにより、Unityが再コンパイルする前にスクリプトが保存されます

3. **フォントサイズを設定（オプション）:**
   - 「font size」を検索
   - 「Editor: Font Size」を好みに調整（初心者には14が良い）

4. **タブサイズを設定:**
   - 「tab size」を検索
   - 「Editor: Tab Size」を「4」に設定（Unity標準）
   - 「Editor: Detect Indentation」を有効化

---

## Step 7: Connect to GitHub / ステップ7：GitHubに接続

### English

1. **Open Source Control:**
   - Click the Source Control icon in the left sidebar (branch icon)
   - Or press `Ctrl+Shift+G` (Windows/Linux) or `Cmd+Shift+G` (Mac)

2. **Sign in to GitHub:**
   - Click "Sign in with GitHub"
   - A browser window will open
   - Click "Authorize" to allow Cursor to access your GitHub
   - Close the browser and return to Cursor

3. **Clone Your Repository:**
   - Click "Clone Repository"
   - Select "Clone from GitHub"
   - Find your `game-dev-2025-yourname` repository
   - Choose where to save it on your computer
   - Click "Select Repository Location"

Now you can commit and push directly from Cursor!

### 日本語

1. **ソースコントロールを開く:**
   - 左サイドバーのソースコントロールアイコン（ブランチアイコン）をクリック
   - または`Ctrl+Shift+G`（Windows/Linux）または`Cmd+Shift+G`（Mac）を押す

2. **GitHubにサインイン:**
   - 「Sign in with GitHub」をクリック
   - ブラウザウィンドウが開きます
   - 「Authorize」をクリックしてCursorがGitHubにアクセスできるようにする
   - ブラウザを閉じてCursorに戻る

3. **リポジトリをクローン:**
   - 「Clone Repository」をクリック
   - 「Clone from GitHub」を選択
   - `game-dev-2025-yourname`リポジトリを見つける
   - コンピュータ上で保存する場所を選択
   - 「Select Repository Location」をクリック

これでCursorから直接コミットしてプッシュできます！

---

## Using Cursor's AI Features / CursorのAI機能を使う

### English

Cursor's AI can help you understand and write code. Here are the key features:

### 1. **Cursor Chat (Ctrl+L or Cmd+L)**
Ask questions about code in natural language:

**Example Questions:**
```
"What does this Unity script do?"
"How do I move a GameObject with arrow keys?"
"Explain what a Rigidbody is in Unity"
"How do I detect collisions in Unity?"
```

### 2. **AI Code Completion (Automatic)**
As you type, Cursor suggests code completions:
- Press `Tab` to accept suggestion
- Press `Esc` to dismiss
- Keep typing to ignore

**Example:**
```csharp
// Start typing: void Update()
// Cursor suggests the rest based on context
void Update()
{
    // Cursor suggests: if (Input.GetKey(KeyCode.W))
}
```

### 3. **Code Explanation (Ctrl+K or Cmd+K)**
Select code and press `Ctrl+K` / `Cmd+K`:
- Type "explain" to get explanation
- Type "comment" to add comments
- Type "fix" to find and fix errors

### 4. **Generate Code**
In Cursor Chat, describe what you want:

**Example:**
```
"Generate a C# script that moves a ball forward when I press the up arrow key"
```

Cursor will generate the code, which you can then copy into your project.

### 日本語

CursorのAIはコードの理解と作成を支援します。主な機能は以下です：

### 1. **Cursor Chat（Ctrl+LまたはCmd+L）**
自然言語でコードについて質問:

**質問例:**
```
「このUnityスクリプトは何をしますか？」
「矢印キーでGameObjectを移動するにはどうすればよいですか？」
「UnityでRigidbodyとは何か説明してください」
「Unityで衝突を検出するにはどうすればよいですか？」
```

### 2. **AIコード補完（自動）**
入力すると、Cursorがコード補完を提案:
- `Tab`を押して提案を受け入れる
- `Esc`を押して却下
- 入力を続けて無視

**例:**
```csharp
// 入力開始: void Update()
// Cursorがコンテキストに基づいて残りを提案
void Update()
{
    // Cursorが提案: if (Input.GetKey(KeyCode.W))
}
```

### 3. **コード説明（Ctrl+KまたはCmd+K）**
コードを選択して`Ctrl+K` / `Cmd+K`を押す:
- 「explain」と入力して説明を取得
- 「comment」と入力してコメントを追加
- 「fix」と入力してエラーを見つけて修正

### 4. **コード生成**
Cursor Chatで、必要なものを説明:

**例:**
```
「上矢印キーを押すとボールが前進するC#スクリプトを生成」
```

Cursorがコードを生成し、プロジェクトにコピーできます。

---

## Basic Cursor Shortcuts / 基本的なCursorショートカット

### Essential Shortcuts / 必須ショートカット

| Action / アクション | Windows/Linux | Mac |
|---------------------|---------------|-----|
| Open file / ファイルを開く | `Ctrl+P` | `Cmd+P` |
| Save file / ファイルを保存 | `Ctrl+S` | `Cmd+S` |
| Save all / すべて保存 | `Ctrl+K S` | `Cmd+K S` |
| Open terminal / ターミナルを開く | `Ctrl+` | `Cmd+` |
| Cursor Chat / Cursor チャット | `Ctrl+L` | `Cmd+L` |
| Command Palette / コマンドパレット | `Ctrl+K` | `Cmd+K` |
| Find in file / ファイル内検索 | `Ctrl+F` | `Cmd+F` |
| Find in project / プロジェクト内検索 | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Go to line / 行に移動 | `Ctrl+G` | `Cmd+G` |
| Comment line / 行をコメント | `Ctrl+/` | `Cmd+/` |
| Duplicate line / 行を複製 | `Shift+Alt+Down` | `Shift+Option+Down` |
| Delete line / 行を削除 | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Format document / ドキュメント整形 | `Shift+Alt+F` | `Shift+Option+F` |

---

## Working with Unity Projects in Cursor / CursorでUnityプロジェクトを扱う

### English

**Opening Unity Project in Cursor:**

1. **Method 1: From Cursor**
   - File → Open Folder
   - Navigate to your Unity project folder
   - Select the folder containing "Assets" folder
   - Click "Open"

2. **Method 2: From Unity (Week 3 onwards)**
   - In Unity, go to Edit → Preferences → External Tools
   - Set "External Script Editor" to Cursor
   - Double-click any script in Unity to open in Cursor

**Workflow:**
1. Edit C# scripts in Cursor
2. Save (Ctrl+S / Cmd+S)
3. Switch to Unity
4. Unity automatically detects changes and recompiles
5. Test in Unity

### 日本語

**CursorでUnityプロジェクトを開く:**

1. **方法1：Cursorから**
   - File → Open Folder
   - Unityプロジェクトフォルダに移動
   - 「Assets」フォルダを含むフォルダを選択
   - 「Open」をクリック

2. **方法2：Unityから（第3週以降）**
   - Unityで、Edit → Preferences → External Toolsに移動
   - 「External Script Editor」をCursorに設定
   - Unity内の任意のスクリプトをダブルクリックしてCursorで開く

**ワークフロー:**
1. CursorでC#スクリプトを編集
2. 保存（Ctrl+S / Cmd+S）
3. Unityに切り替え
4. Unityが自動的に変更を検出して再コンパイル
5. Unityでテスト

---

## Troubleshooting / トラブルシューティング

### Problem: Cursor won't start / 問題：Cursorが起動しない

**English:**
- **Solution 1:** Restart your computer
- **Solution 2:** Reinstall Cursor
- **Solution 3:** Check system requirements (8GB RAM minimum)
- **Solution 4:** Temporarily disable antivirus

**日本語:**
- **解決策1:** コンピュータを再起動
- **解決策2:** Cursorを再インストール
- **解決策3:** システム要件を確認（最小8GB RAM）
- **解決策4:** 一時的にアンチウイルスを無効化

---

### Problem: AI features not working / 問題：AI機能が動作しない

**English:**
- **Solution 1:** Make sure you're signed in (check bottom left corner)
- **Solution 2:** Check internet connection
- **Solution 3:** You may have reached daily limit (free plan)
- **Solution 4:** Restart Cursor

**日本語:**
- **解決策1:** サインインしていることを確認（左下隅をチェック）
- **解決策2:** インターネット接続を確認
- **解決策3:** 1日の制限に達している可能性（無料プラン）
- **解決策4:** Cursorを再起動

---

### Problem: C# extension not working / 問題：C#拡張機能が動作しない

**English:**
- **Solution 1:** Reload window: Ctrl+Shift+P → "Reload Window"
- **Solution 2:** Reinstall C# extension
- **Solution 3:** Install .NET SDK: https://dotnet.microsoft.com/download

**日本語:**
- **解決策1:** ウィンドウをリロード：Ctrl+Shift+P → 「Reload Window」
- **解決策2:** C#拡張機能を再インストール
- **解決策3:** .NET SDKをインストール：https://dotnet.microsoft.com/download

---

### Problem: Can't connect to GitHub / 問題：GitHubに接続できない

**English:**
- **Solution 1:** Sign out and sign in again
- **Solution 2:** Revoke Cursor permissions on GitHub.com → Settings → Applications → Authorized OAuth Apps
- **Solution 3:** Use GitHub Desktop instead for Git operations

**日本語:**
- **解決策1:** サインアウトして再度サインイン
- **解決策2:** GitHub.com → Settings → Applications → Authorized OAuth AppsでCursorの権限を取り消す
- **解決策3:** Git操作にはGitHub Desktopを代わりに使用

---

## Tips for Using Cursor Effectively / Cursorを効果的に使うためのヒント

### English

1. **Ask Specific Questions:**
   - ❌ "How do I make a game?"
   - ✅ "How do I make a ball move forward in Unity using C#?"

2. **Use AI to Learn, Not Just Copy:**
   - Read and understand generated code
   - Ask "explain this line by line"
   - Modify code to see what changes

3. **Start Simple:**
   - Don't ask AI to generate entire complex systems
   - Build incrementally
   - Test small pieces of code

4. **Use AI for Debugging:**
   - Paste error messages in Cursor Chat
   - Ask "why is this code not working?"
   - Learn from explanations

5. **Comment Your Code:**
   - Use AI to generate comments: Select code → Ctrl+K → "add comments"
   - Helps you remember what code does later

### 日本語

1. **具体的な質問をする:**
   - ❌ 「ゲームの作り方は？」
   - ✅ 「C#を使ってUnityでボールを前進させるにはどうすればよいですか？」

2. **AIをコピーだけでなく学習に使う:**
   - 生成されたコードを読んで理解する
   - 「これを1行ずつ説明してください」と質問
   - コードを変更して何が変わるか確認

3. **シンプルに始める:**
   - AIに複雑なシステム全体を生成させない
   - 段階的に構築
   - 小さなコード片をテスト

4. **デバッグにAIを使う:**
   - エラーメッセージをCursor Chatに貼り付け
   - 「このコードがなぜ動かないのですか？」と質問
   - 説明から学ぶ

5. **コードにコメントを付ける:**
   - AIを使ってコメントを生成：コードを選択 → Ctrl+K → 「add comments」
   - 後でコードが何をするか覚えるのに役立つ

---

## Next Steps / 次のステップ

### English
Now that Cursor is set up:
1. ✅ Familiarize yourself with the interface
2. ✅ Try opening your GitHub repository folder in Cursor
3. ✅ Experiment with Cursor Chat (Ctrl+L / Cmd+L)
4. ✅ Ask it questions like "What is Unity3D?" or "What is C#?"
5. ✅ Ready for Week 3 when we start Unity scripting!

### 日本語
Cursorがセットアップされたので:
1. ✅ インターフェースに慣れる
2. ✅ CursorでGitHubリポジトリフォルダを開いてみる
3. ✅ Cursor Chat（Ctrl+L / Cmd+L）を試す
4. ✅ 「Unity3Dとは何ですか？」や「C#とは何ですか？」のような質問をする
5. ✅ Unityスクリプティングを開始する第3週の準備が整いました！

---

## Additional Resources / 追加リソース

### English
- **Cursor Documentation:** https://docs.cursor.com
- **Cursor Community Forum:** https://forum.cursor.com
- **VS Code Keyboard Shortcuts:** https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf (Cursor uses same shortcuts)

### 日本語
- **Cursorドキュメント:** https://docs.cursor.com
- **Cursorコミュニティフォーラム:** https://forum.cursor.com
- **VS Codeキーボードショートカット:** https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf （Cursorは同じショートカットを使用）

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
