import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('university_life.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255),
    energy_level VARCHAR(255),
    description VARCHAR(255)
)
''')
conn.commit()