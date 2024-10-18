import re
from docx import Document
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('university_life.db')
cursor = conn.cursor()
def parse_and_insert_data(doc_path):
    doc = Document(doc_path)
    current_category = None
    current_energy_level = None
    for para in doc.paragraphs:
        text = para.text.strip()
        print(text)
        if not text:
            continue
        if text.startswith('休息放松') or text.startswith('认真学习') or text.startswith('体育运动') or text.startswith('打游戏娱乐') or text.startswith('广泛交友') or text.startswith('学习技能') or text.startswith('兼职赚钱') or text.startswith('社团活动') or text.startswith('组织活动') or text.startswith('参与竞赛') or text.startswith('参与科研') or text.startswith('谈情说爱（男生版）') or text.startswith('谈情说爱（女生版）'):
            current_category = text
        elif text.startswith('0~') or text.startswith('20~') or text.startswith('40~') or text.startswith('60~') or text.startswith('80~'):
            current_energy_level = text
        else:
            text = re.sub(r'^\d+\.\s*', '', text)
            description = text.replace('“', '').replace('”', '')
            print(current_category, current_energy_level, description)
            cursor.execute('''
            INSERT INTO activities (category, energy_level, description) VALUES (?, ?, ?)
            ''', (current_category, current_energy_level, description))

    conn.commit()

# 读取文档并插入数据
doc_path = "C:\\Users\\wzy668\\Downloads\\游戏文本.docx"
parse_and_insert_data(doc_path)

# 关闭数据库连接
conn.close()
