import sqlite3
import random

# 连接到SQLite数据库
# 数据库文件是 university_life.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('C:\\Users\\wzy668\\Downloads\\activity\\university_life.db')
cursor = conn.cursor()

def get_random_activity(category, energy_level):
    # 执行查询
    cursor.execute(
        "SELECT description FROM activities WHERE category = ? AND energy_level = ?",
        (category, energy_level)
    )
    # 获取所有匹配的记录
    records = cursor.fetchall()
    # 检查是否有任何记录
    if records:
        # 随机选择一个记录
        random_record = random.choice(records)
        return random_record[0]
    else:
        return "没有找到匹配的记录。"
category = "休息放松"
energy_level = "0~20"
activity = get_random_activity(category, energy_level)
print("随机抽取的数据：", activity)
# 关闭Cursor和Connection
cursor.close()
conn.close()