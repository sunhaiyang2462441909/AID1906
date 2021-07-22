"""
seve_image.py
二进制文件存储演示
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

# # 存储图片
# with open('touxiang.jpeg', 'rb') as f:
#     data = f.read()
# try:
#     sql = "update class_1 set image = %s where name='Abby';"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class_1 where name='Abby'"
cur.execute(sql)
data = cur.fetchone()
with open('girl.jpg', 'wb') as f:
    f.write(data[0])

# 关闭游标和数据库
cur.close()
db.close()
