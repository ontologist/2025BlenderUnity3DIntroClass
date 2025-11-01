#!/usr/bin/env python3
"""
Generate HTML files for weeks 7-12 using templates from Week 6
"""
import os
import re

# Read Week 6 templates
def read_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_slides_html(week_num, icon, title_en, title_jp, topics, lecture_plan_path):
    """Generate slides.html for a week"""
    template = read_template('docs/weeks/week-06/slides.html')
    
    # Replace week-specific content
    template = template.replace('Week 6: AI Enemy Implementation', f'Week {week_num}: {title_en}')
    template = template.replace('<h1>🤖 Week 6</h1>', f'<h1>{icon} Week {week_num}</h1>')
    template = template.replace('AI Enemy Implementation<br>AI敵ボールの実装', f'{title_en}<br>{title_jp}')
    
    # Read lecture plan for detailed content
    if os.path.exists(lecture_plan_path):
        with open(lecture_plan_path, 'r', encoding='utf-8') as f:
            lecture_content = f.read()
        
        # Extract learning objectives
        obj_match = re.search(r'### English\n(.*?)\n### 日本語', lecture_content, re.DOTALL)
        if obj_match:
            objectives = [line.strip('- ').strip() for line in obj_match.group(1).strip().split('\n') if line.strip().startswith('-')]
    else:
        objectives = topics[:8]  # Default to topics
    
    return template

def generate_lecture_html(week_num, icon, title_en, title_jp, lecture_plan_path):
    """Generate lecture.html for a week"""
    template = read_template('docs/weeks/week-06/lecture.html')
    
    # Replace week-specific content
    template = template.replace('Week 6: AI Enemy Implementation', f'Week {week_num}: {title_en}')
    template = template.replace('<h1>🤖 Week 6: AI Enemy Implementation</h1>', f'<h1>{icon} Week {week_num}: {title_en}</h1>')
    template = template.replace('第6週：AI敵ボールの実装', f'第{week_num}週：{title_jp}')
    
    return template

def generate_assignment_html(week_num, icon, title_en, title_jp, assignment_md_path):
    """Generate assignment.html for a week"""
    template = read_template('docs/weeks/week-06/assignment.html')
    
    # Replace week-specific content
    template = template.replace('Week 6 Assignment: AI Enemy Implementation', f'Week {week_num} Assignment: {title_en}')
    template = template.replace('第6週課題：AI敵ボールの実装', f'第{week_num}週課題：{title_jp}')
    
    return template

# Week data
weeks = [
    (7, "🎮", "Game States & Polish", "ゲーム状態と仕上げ"),
    (8, "👤", "Character Models & Setup", "キャラクターモデルのインポートとセットアップ"),
    (9, "🎬", "Character Animation & Physics", "キャラクターアニメーションとボール押し機能"),
    (10, "🔊", "Sound Effects & Audio Triggers", "効果音とオーディオトリガー"),
    (11, "🎵", "Background Music & Mixing", "バックグラウンドミュージックとオーディオミキシング"),
    (12, "🎓", "Final Project & Presentation", "最終プロジェクトの統合とプレゼンテーション"),
]

print("Generating HTML files for weeks 7-12...")
for week_num, icon, title_en, title_jp in weeks:
    week_dir = f'docs/weeks/week-{week_num:02d}'
    os.makedirs(week_dir, exist_ok=True)
    
    lecture_plan = f'lectures/week-{week_num:02d}/LECTURE_PLAN.md'
    assignment_md = f'lectures/week-{week_num:02d}/assignments/WEEK{week_num:02d}_ASSIGNMENT.md'
    
    # Generate slides
    slides_html = generate_slides_html(week_num, icon, title_en, title_jp, [], lecture_plan)
    with open(f'{week_dir}/slides.html', 'w', encoding='utf-8') as f:
        f.write(slides_html)
    print(f"  Created {week_dir}/slides.html")
    
    # Generate lecture
    lecture_html = generate_lecture_html(week_num, icon, title_en, title_jp, lecture_plan)
    with open(f'{week_dir}/lecture.html', 'w', encoding='utf-8') as f:
        f.write(lecture_html)
    print(f"  Created {week_dir}/lecture.html")
    
    # Generate assignment (skip if week 7 already exists)
    if week_num == 7 and os.path.exists(f'{week_dir}/assignment.html'):
        print(f"  Skipped {week_dir}/assignment.html (already exists)")
    else:
        assignment_html = generate_assignment_html(week_num, icon, title_en, title_jp, assignment_md)
        with open(f'{week_dir}/assignment.html', 'w', encoding='utf-8') as f:
            f.write(assignment_html)
        print(f"  Created {week_dir}/assignment.html")

print("\nAll HTML files generated!")

