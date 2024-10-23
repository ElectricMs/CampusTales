import sqlite3
import random

# 连接到SQLite数据库
# 数据库文件是 university_life.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('./activity/university_life.db')
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
energy_level = "20~40"
activity = get_random_activity(category, energy_level)
print("随机抽取的数据：", activity)
# 关闭Cursor和Connection
cursor.close()
conn.close()

# 休息放松  认真学习  体育运动  打游戏娱乐  广泛交友  学习技能  
# 兼职赚钱  社团活动  组织活动  参与竞赛  参与科研  谈情说爱（女生版）  谈情说爱（男生版）