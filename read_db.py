"""
read_db.py
数据库读操作示例  select
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='s199812060.',
                     database='stu',
                     charset='utf8')

# 创建游标 (操作数据库语句,获取查询结果)
cur = db.cursor()

# 获取数据库数数据
sql = "select name,age from class_1 where gender='m';"
cur.execute(sql)  # 执行正确后cur调用函数获取结果
# 获取查询结果
one_row = cur.fetchone()
print(one_row)  # 元组

# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)  # 元组套元组

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)  # 元组套元组
# 关闭游标和数据库
cur.close()
db.close()
