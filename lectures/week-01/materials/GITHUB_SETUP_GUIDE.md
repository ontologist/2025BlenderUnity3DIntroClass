# GitHub Setup Guide / GitHub セットアップガイド
**Developer / 開発者:** Yuri Tijerino

---

## Introduction / 紹介

### English
GitHub is a platform for version control and collaboration. In this course, you'll use GitHub to:
- Store all your project files
- Track changes to your work over time
- Submit assignments
- Build a portfolio of your game development projects

This guide will walk you through setting up GitHub for this course in about 10-15 minutes.

### 日本語
GitHubはバージョン管理とコラボレーションのためのプラットフォームです。このコースでは、GitHubを以下のために使用します：
- すべてのプロジェクトファイルを保存
- 作業の変更を時間とともに追跡
- 課題を提出
- ゲーム開発プロジェクトのポートフォリオを構築

このガイドでは、約10〜15分でこのコース用のGitHubのセットアップを説明します。

---

## Step 1: Create a GitHub Account / ステップ1：GitHubアカウントを作成

### English
1. Go to https://github.com
2. Click "Sign up" in the top right corner
3. Enter your email address
4. Create a strong password
5. Choose a username (this will be public)
   - Tip: Use a professional username like `firstname-lastname` or `firstnamelastname`
6. Verify your account via email
7. Choose the FREE plan (sufficient for this course)

### 日本語
1. https://github.com にアクセス
2. 右上の「Sign up」をクリック
3. メールアドレスを入力
4. 強力なパスワードを作成
5. ユーザー名を選択（これは公開されます）
   - ヒント：`firstname-lastname`や`firstnamelastname`のようなプロフェッショナルなユーザー名を使用
6. メールでアカウントを確認
7. FREEプランを選択（このコースには十分）

---

## Step 2: Install Git or GitHub Desktop / ステップ2：GitまたはGitHub Desktopをインストール

### Option A: GitHub Desktop (Recommended for Beginners / 初心者推奨)

#### English
1. Download from https://desktop.github.com
2. Install the application
3. Launch GitHub Desktop
4. Sign in with your GitHub account
5. Configure your name and email (this appears on your commits)

#### 日本語
1. https://desktop.github.com からダウンロード
2. アプリケーションをインストール
3. GitHub Desktopを起動
4. GitHubアカウントでサインイン
5. 名前とメールを設定（これはコミットに表示されます）

### Option B: Git Command Line / オプションB：Gitコマンドライン

#### English
1. **Windows:** Download from https://git-scm.com/download/win
2. **Mac:** Open Terminal and type `git --version` (it will prompt to install if not present)
3. **Linux:** Use your package manager: `sudo apt-get install git` (Ubuntu/Debian)

Configure Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### 日本語
1. **Windows:** https://git-scm.com/download/win からダウンロード
2. **Mac:** ターミナルを開いて`git --version`と入力（存在しない場合はインストールするよう促されます）
3. **Linux:** パッケージマネージャーを使用：`sudo apt-get install git`（Ubuntu/Debian）

Gitを設定：
```bash
git config --global user.name "あなたの名前"
git config --global user.email "your.email@example.com"
```

---

## Step 3: Create Your Course Repository / ステップ3：コース用リポジトリを作成

### English

1. **Go to GitHub.com and log in**
2. **Click the "+" icon in the top right → "New repository"**
3. **Repository settings:**
   - **Repository name:** `game-dev-2025-yourname`
     - Example: `game-dev-2025-yuri-tijerino`
   - **Description:** "Game Development Course - Blender and Unity3D"
   - **Visibility:** Choose "Public" (recommended) or "Private"
   - **Initialize with:**
     - ✅ Check "Add a README file"
     - ✅ Check "Add .gitignore" → Choose "Unity" template
     - ❌ Don't add a license (not needed for coursework)
4. **Click "Create repository"**

### 日本語

1. **GitHub.comにアクセスしてログイン**
2. **右上の「+」アイコンをクリック → 「New repository」**
3. **リポジトリ設定:**
   - **リポジトリ名:** `game-dev-2025-yourname`
     - 例：`game-dev-2025-yuri-tijerino`
   - **説明:** "Game Development Course - Blender and Unity3D"
   - **可視性:** 「Public」（推奨）または「Private」を選択
   - **初期化:**
     - ✅ 「Add a README file」にチェック
     - ✅ 「Add .gitignore」にチェック → 「Unity」テンプレートを選択
     - ❌ ライセンスは追加しない（課題には不要）
4. **「Create repository」をクリック**

---

## Step 4: Clone Repository to Your Computer / ステップ4：リポジトリをコンピュータにクローン

### Option A: Using GitHub Desktop / GitHub Desktopを使用

#### English
1. On your repository page on GitHub.com, click the green "Code" button
2. Click "Open with GitHub Desktop"
3. Choose where to save the repository on your computer
   - Recommended: Create a folder like `Documents/GameDev2025/`
4. Click "Clone"

Your repository is now on your computer!

#### 日本語
1. GitHub.comのリポジトリページで、緑色の「Code」ボタンをクリック
2. 「Open with GitHub Desktop」をクリック
3. コンピュータ上でリポジトリを保存する場所を選択
   - 推奨：`Documents/GameDev2025/`のようなフォルダを作成
4. 「Clone」をクリック

リポジトリがコンピュータ上にあります！

### Option B: Using Command Line / コマンドラインを使用

#### English
1. On your repository page, click the green "Code" button
2. Copy the HTTPS URL
3. Open Terminal (Mac/Linux) or Git Bash (Windows)
4. Navigate to where you want to store your projects:
```bash
cd ~/Documents
mkdir GameDev2025
cd GameDev2025
```
5. Clone the repository:
```bash
git clone https://github.com/yourusername/game-dev-2025-yourname.git
```
6. Enter your repository folder:
```bash
cd game-dev-2025-yourname
```

#### 日本語
1. リポジトリページで、緑色の「Code」ボタンをクリック
2. HTTPS URLをコピー
3. ターミナル（Mac/Linux）またはGit Bash（Windows）を開く
4. プロジェクトを保存したい場所に移動:
```bash
cd ~/Documents
mkdir GameDev2025
cd GameDev2025
```
5. リポジトリをクローン:
```bash
git clone https://github.com/yourusername/game-dev-2025-yourname.git
```
6. リポジトリフォルダに入る:
```bash
cd game-dev-2025-yourname
```

---

## Step 5: Set Up Folder Structure / ステップ5：フォルダ構造をセットアップ

### English
Create folders for each week of the course:

**Option A: Using File Explorer / Finder**
Create these folders manually in your repository:
```
game-dev-2025-yourname/
├── week-01/
├── week-02/
├── week-03/
├── week-04/
├── week-05/
├── week-06/
├── week-07/
├── week-08/
├── week-09/
├── week-10/
├── week-11/
└── week-12/
```

**Option B: Using Command Line**
```bash
# Navigate to your repository folder
cd game-dev-2025-yourname

# Create all week folders at once
mkdir week-{01..12}
```

### 日本語
コースの各週のフォルダを作成:

**オプションA：ファイルエクスプローラー / Finderを使用**
リポジトリに手動でこれらのフォルダを作成:
```
game-dev-2025-yourname/
├── week-01/
├── week-02/
├── week-03/
├── week-04/
├── week-05/
├── week-06/
├── week-07/
├── week-08/
├── week-09/
├── week-10/
├── week-11/
└── week-12/
```

**オプションB：コマンドラインを使用**
```bash
# リポジトリフォルダに移動
cd game-dev-2025-yourname

# すべての週フォルダを一度に作成
mkdir week-{01..12}
```

---

## Step 6: Create and Improve .gitignore / ステップ6：.gitignoreを作成・改善

### English
The .gitignore file tells Git which files NOT to track. This is important because Blender and Unity create many temporary files we don't need to save.

**Edit your .gitignore file:**
1. Open the `.gitignore` file in your repository (use any text editor)
2. Add these lines for Blender:

```gitignore
# Blender
*.blend1
*.blend2
*.blend3
*.blend4
*.blend5
*.blend6
*.blend7
*.blend8
*.blend9

# Blender Backup files
*.blend1
*.blend2

# Blender Cache
blendcache_*/

# OS Files
.DS_Store
Thumbs.db
```

3. The Unity entries should already be there from the template
4. Save the file

### 日本語
.gitignoreファイルは、Gitに追跡しないファイルを指示します。これは、BlenderとUnityが多くの一時ファイルを作成し、それらを保存する必要がないため重要です。

**.gitignoreファイルを編集:**
1. リポジトリの`.gitignore`ファイルを開く（任意のテキストエディタを使用）
2. Blender用にこれらの行を追加:

```gitignore
# Blender
*.blend1
*.blend2
*.blend3
*.blend4
*.blend5
*.blend6
*.blend7
*.blend8
*.blend9

# Blender Backup files
*.blend1
*.blend2

# Blender Cache
blendcache_*/

# OS Files
.DS_Store
Thumbs.db
```

3. Unityのエントリはテンプレートから既に存在するはず
4. ファイルを保存

---

## Step 7: Make Your First Commit / ステップ7：最初のコミットを行う

### Option A: Using GitHub Desktop / GitHub Desktopを使用

#### English
1. Open GitHub Desktop
2. You should see your changes listed (new folders, updated .gitignore)
3. At the bottom left:
   - **Summary:** Enter "Set up project structure"
   - **Description (optional):** "Created weekly folders and updated .gitignore for Blender and Unity"
4. Click "Commit to main"
5. Click "Push origin" to upload to GitHub

#### 日本語
1. GitHub Desktopを開く
2. 変更がリストされているはず（新しいフォルダ、更新された.gitignore）
3. 左下で:
   - **Summary:** 「Set up project structure」と入力
   - **Description (オプション):** 「Created weekly folders and updated .gitignore for Blender and Unity」
4. 「Commit to main」をクリック
5. 「Push origin」をクリックしてGitHubにアップロード

### Option B: Using Command Line / コマンドラインを使用

#### English
```bash
# Check what files have changed
# 変更されたファイルを確認
git status

# Add all changes
# すべての変更を追加
git add .

# Commit with a message
# メッセージ付きでコミット
git commit -m "Set up project structure

Created weekly folders and updated .gitignore for Blender and Unity"

# Push to GitHub
# GitHubにプッシュ
git push
```

#### 日本語
```bash
# 何のファイルが変更されたかチェック
git status

# すべての変更を追加
git add .

# メッセージ付きでコミット
git commit -m "プロジェクト構造をセットアップ

週次フォルダを作成し、BlenderとUnity用に.gitignoreを更新"

# GitHubにプッシュ
git push
```

---

## Step 8: Verify on GitHub / ステップ8：GitHubで確認

### English
1. Go to your repository on GitHub.com
2. Refresh the page
3. You should see:
   - All your week folders (week-01 through week-12)
   - Updated .gitignore file
   - Your commit message

**Congratulations! Your GitHub repository is set up!**

### 日本語
1. GitHub.comでリポジトリにアクセス
2. ページを更新
3. 以下が表示されるはず:
   - すべての週フォルダ（week-01からweek-12）
   - 更新された.gitignoreファイル
   - コミットメッセージ

**おめでとうございます！GitHubリポジトリがセットアップされました！**

---

## Basic Git Workflow for Assignments / 課題用の基本的なGitワークフロー

### English

This is the workflow you'll follow every week:

1. **Work on your project** (create Blender files, Unity projects, etc.)
2. **Save your work** regularly in the appropriate week folder
3. **Commit your changes:**
   - Open GitHub Desktop
   - Review your changes
   - Write a descriptive commit message
   - Click "Commit to main"
4. **Push to GitHub:**
   - Click "Push origin"
5. **Verify on GitHub.com** that your files are uploaded

**Commit Message Tips:**
- Be descriptive: "Complete Week 1 maze layout" not "done"
- Use present tense: "Add textures to walls" not "Added textures"
- Include what changed and why if helpful

**Example Commit Messages:**
```
Create basic maze layout in Blender

Added walls, floor, and goal area for Week 1 assignment.
```

```
Fix maze wall colliders in Unity

Walls were not blocking player properly. Added Box Colliders.
```

### 日本語

これは毎週従うワークフローです：

1. **プロジェクトに取り組む**（Blenderファイル、Unityプロジェクトなどを作成）
2. **作業を保存** 適切な週フォルダに定期的に
3. **変更をコミット:**
   - GitHub Desktopを開く
   - 変更を確認
   - 説明的なコミットメッセージを書く
   - 「Commit to main」をクリック
4. **GitHubにプッシュ:**
   - 「Push origin」をクリック
5. **GitHub.comで確認** ファイルがアップロードされていることを確認

**コミットメッセージのヒント:**
- 説明的にする：「Week 1の迷路レイアウトを完成」であって「完了」ではない
- 現在形を使用：「壁にテクスチャを追加」であって「壁にテクスチャを追加した」ではない
- 何が変更されたか、なぜ変更されたかを含める（役立つ場合）

**コミットメッセージの例:**
```
Blenderで基本的な迷路レイアウトを作成

Week 1の課題用に壁、床、ゴールエリアを追加。
```

```
Unityで迷路の壁のコライダーを修正

壁がプレイヤーを適切にブロックしていなかった。Box Collidersを追加。
```

---

## Troubleshooting / トラブルシューティング

### Problem: Can't push to GitHub / 問題：GitHubにプッシュできない

**English:**
- **Solution 1:** Make sure you're logged into GitHub Desktop
- **Solution 2:** Check your internet connection
- **Solution 3:** Try pulling first: Repository → Pull

**日本語:**
- **解決策1:** GitHub Desktopにログインしていることを確認
- **解決策2:** インターネット接続を確認
- **解決策3:** まずプルしてみる：Repository → Pull

---

### Problem: Made changes but they don't show in GitHub Desktop / 問題：変更したのにGitHub Desktopに表示されない

**English:**
- **Solution:** Make sure you saved the files in your repository folder, not somewhere else on your computer

**日本語:**
- **解決策:** コンピュータの他の場所ではなく、リポジトリフォルダにファイルを保存したことを確認

---

### Problem: Accidentally committed something I shouldn't have / 問題：誤って不要なものをコミットした

**English:**
- **Solution 1:** If you haven't pushed yet, you can undo the commit in GitHub Desktop: Repository → Undo commit
- **Solution 2:** Add the file pattern to .gitignore and commit again
- **Solution 3:** Ask the instructor for help

**日本語:**
- **解決策1:** まだプッシュしていない場合、GitHub Desktopでコミットを元に戻せる：Repository → Undo commit
- **解決策2:** ファイルパターンを.gitignoreに追加して再度コミット
- **解決策3:** インストラクターに助けを求める

---

## Quick Reference / クイックリファレンス

### GitHub Desktop Workflow / GitHub Desktopワークフロー

| Action / アクション | How to do it / 方法 |
|---------------------|---------------------|
| See changes / 変更を見る | Open GitHub Desktop |
| Commit / コミット | Write message → "Commit to main" |
| Upload / アップロード | Click "Push origin" |
| Download latest / 最新をダウンロード | Click "Pull origin" or Repository → Pull |
| Undo commit / コミットを取り消す | Repository → Undo commit |
| View history / 履歴を表示 | Click "History" tab |

### Command Line Workflow / コマンドラインワークフロー

| Action / アクション | Command / コマンド |
|---------------------|-------------------|
| Check status / ステータス確認 | `git status` |
| Add files / ファイルを追加 | `git add .` |
| Commit / コミット | `git commit -m "message"` |
| Push / プッシュ | `git push` |
| Pull / プル | `git pull` |
| View history / 履歴表示 | `git log` |
| Undo last commit / 最後のコミットを取り消す | `git reset --soft HEAD~1` |

---

## Next Steps / 次のステップ

### English
Now that your GitHub is set up:
1. ✅ Complete your Week 1 Blender assignment
2. ✅ Save it in the `week-01/` folder
3. ✅ Commit and push to GitHub
4. ✅ Verify it's visible on GitHub.com
5. ✅ Share your repository URL with the instructor (if required)

**Your repository URL format:**
`https://github.com/yourusername/game-dev-2025-yourname`

### 日本語
GitHubがセットアップされたので:
1. ✅ Week 1のBlender課題を完了
2. ✅ `week-01/`フォルダに保存
3. ✅ コミットしてGitHubにプッシュ
4. ✅ GitHub.comで表示されることを確認
5. ✅ インストラクターにリポジトリURLを共有（必要な場合）

**リポジトリURLの形式:**
`https://github.com/yourusername/game-dev-2025-yourname`

---

## Additional Resources / 追加リソース

### English
- **GitHub Documentation:** https://docs.github.com/en
- **GitHub Desktop Documentation:** https://docs.github.com/en/desktop
- **Git Basics Tutorial:** https://git-scm.com/doc
- **Interactive Git Tutorial:** https://learngitbranching.js.org/

### 日本語
- **GitHubドキュメント（日本語）:** https://docs.github.com/ja
- **GitHub Desktopドキュメント:** https://docs.github.com/ja/desktop
- **Git基礎チュートリアル:** https://git-scm.com/book/ja/v2
- **インタラクティブGitチュートリアル:** https://learngitbranching.js.org/ （英語）

---

## Help and Support / ヘルプとサポート

### English
If you encounter any issues with GitHub setup:
1. Check the Troubleshooting section above
2. Ask classmates (collaboration is encouraged!)
3. Post in the course discussion forum
4. Contact the instructor
5. GitHub Support: https://support.github.com

### 日本語
GitHubのセットアップで問題が発生した場合:
1. 上記のトラブルシューティングセクションを確認
2. クラスメートに聞く（協力が推奨されます！）
3. コースディスカッションフォーラムに投稿
4. インストラクターに連絡
5. GitHubサポート: https://support.github.com

---

**Copyright © 2025 Yuri Tijerino. All rights reserved.**
**著作権 © 2025 Yuri Tijerino. 無断転載を禁じます。**
