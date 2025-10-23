# Game Development Course 2025
# ゲーム開発コース2025

**12-Week Introduction to Blender and Unity3D for Non-Programmers**

**Developer:** Yuri Tijerino

---

## Course Overview

This repository contains all course materials for a 12-week game development course designed for complete beginners with no programming experience. Students will learn 3D modeling in Blender and game development in Unity3D while building a complete maze game.

このリポジトリには、プログラミング経験のない完全な初心者向けの12週間ゲーム開発コースのすべての教材が含まれています。学生はBlenderで3Dモデリングを学び、Unity3Dでゲーム開発を学びながら、完全な迷路ゲームを構築します。

---

## Structure / 構造

```
2025-godot-class/
├── CURRICULUM_OVERVIEW.md          # Full course curriculum
├── lectures/                       # Weekly lecture materials
│   ├── week-01/
│   │   ├── LECTURE_PLAN.md
│   │   ├── assignments/
│   │   │   └── WEEK01_ASSIGNMENT.md
│   │   ├── materials/
│   │   │   ├── GITHUB_SETUP_GUIDE.md
│   │   │   └── CURSOR_SETUP_GUIDE.md
│   │   ├── slides/
│   │   └── resources/
│   ├── week-02/
│   │   ├── LECTURE_PLAN.md
│   │   ├── assignments/
│   │   │   └── WEEK02_ASSIGNMENT.md
│   │   ├── materials/
│   │   ├── slides/
│   │   └── resources/
│   ├── week-03/ to week-12/        # Additional weeks (coming soon)
│   └── ...
├── docs/                           # GitHub Pages site
│   ├── index.html                  # Main landing page
│   ├── styles.css
│   ├── weeks/                      # HTML versions of lectures
│   └── guides/                     # HTML versions of setup guides
└── web-bundles/                    # Additional resources

```

---

## Course Phases

### Phase 1: Blender Fundamentals (Weeks 1-2)
- Blender interface and 3D modeling basics
- Materials, textures, and simple animations
- UV unwrapping and bone rigging introduction

### Phase 2: Unity3D Fundamentals (Weeks 3-4)
- Unity interface and GameObjects
- Physics, collisions, and input systems

### Phase 3: Ball Maze Game (Weeks 5-7)
- Maze creation and player controller
- AI enemy implementation
- Game states and polish
- **Midterm Project:** Complete ball maze game

### Phase 4: Character Integration (Weeks 8-9)
- Character models and setup
- Character animation and ball-pushing mechanics

### Phase 5: Audio & Polish (Weeks 10-11)
- Sound effects and audio triggers
- Background music and audio mixing

### Phase 6: Final Project (Week 12)
- Final integration and presentation
- **Final Project:** Complete game with characters and audio

---

## Tools Required / 必要なツール

- **Blender** 4.0+ (Free / 無料): https://www.blender.org/
- **Unity3D** 2022 LTS (Free Personal License / 無料個人ライセンス): https://unity.com/
- **Cursor AI** (Free Student Pro / 無料学生プロ): https://cursor.com/students
- **GitHub** account: https://github.com/
- **Git** or **GitHub Desktop**: https://desktop.github.com/

---

## Setup Instructions / セットアップ手順

### For Instructors / インストラクター向け

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/2025-godot-class.git
   ```

2. **Set up GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: /docs
   - Save

3. **Customize materials**
   - Update CURRICULUM_OVERVIEW.md with your information
   - Adjust lecture plans based on your teaching style
   - Add additional resources as needed

### For Students / 学生向け

1. **Visit the course website**
   - URL will be provided by instructor
   - Or: https://yourusername.github.io/2025-godot-class/

2. **Set up your development environment**
   - Follow the Cursor AI Setup Guide
   - Follow the GitHub Setup Guide
   - Install Blender and Unity (guides in Week 1-3)

3. **Create your course repository**
   - Name it: `game-dev-2025-yourname`
   - Follow GitHub setup guide for structure

4. **Complete weekly assignments**
   - Follow lecture notes and assignments
   - Commit work to your GitHub repository
   - Submit GitHub repo link to instructor

---

## Weekly Materials

Each week includes:
- **Lecture Plan:** Detailed 100-minute lecture breakdown
- **Lecture Slides:** HTML presentation slides
- **Assignment:** Hands-on project with grading rubric
- **Materials:** Additional resources, tutorials, FAQs
- **Resources:** Links to videos, documentation, assets

各週には以下が含まれます：
- **講義計画:** 詳細な100分講義の内訳
- **講義スライド:** HTMLプレゼンテーションスライド
- **課題:** 採点基準付きの実践的プロジェクト
- **教材:** 追加リソース、チュートリアル、FAQ
- **リソース:** ビデオ、ドキュメント、アセットへのリンク

---

## Current Status / 現在の状況

✅ **Completed / 完了:**
- Course curriculum structure
- Week 1: Blender Basics
- Week 2: Materials & Textures
- GitHub Pages landing page
- Setup guides (Cursor AI, GitHub)

🚧 **In Progress / 進行中:**
- Week 3-12 detailed materials
- HTML versions of all lectures
- Additional setup guides

---

## Contributing / 貢献

This is a course materials repository. If you find errors or have suggestions:
1. Open an issue
2. Submit a pull request
3. Contact the course developer

これはコース教材リポジトリです。エラーを見つけた場合や提案がある場合：
1. issueを開く
2. プルリクエストを送信
3. コース開発者に連絡

---

## License / ライセンス

**Copyright © 2025 Yuri Tijerino. All rights reserved.**

This course material is proprietary and intended for educational use in the context of this specific course. Unauthorized distribution, reproduction, or commercial use is prohibited.

このコース教材は独自のものであり、この特定のコースのコンテキストでの教育使用を目的としています。無断での配布、複製、商業利用は禁止されています。

---

## Contact / 連絡先

**Course Developer:** Yuri Tijerino

For questions, issues, or feedback about the course materials, please open an issue in this repository or contact the instructor directly.

コース教材に関する質問、問題、フィードバックについては、このリポジトリでissueを開くか、インストラクターに直接連絡してください。

---

## Acknowledgments / 謝辞

Special thanks to:
- Blender Foundation for the amazing open-source 3D software
- Unity Technologies for making game development accessible
- Cursor AI for providing student free access
- GitHub for hosting course materials
- All open-source contributors whose tools and assets support this course

特別な感謝：
- 素晴らしいオープンソース3DソフトウェアのためのBlender Foundation
- ゲーム開発をアクセス可能にしたUnity Technologies
- 学生への無料アクセスを提供するCursor AI
- コース教材をホストするGitHub
- このコースをサポートするツールとアセットを提供するすべてのオープンソース貢献者

---

**Happy Game Development! / ゲーム開発を楽しんでください！** 🎮🎨🎵
