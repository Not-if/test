"""
pycharm操作数据库流程演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 生成游标对象(操作数据库,执行sql语句)
cur = db.cursor()
f = open('dict.txt')
# 执行各种对数据库的读写操作
try:
    exe = []
    for line in f:
        word = line.split(' ',1)[0]
        mean = line.split(' ',1)[1]
        exe.append((word,mean))

    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql, exe)

    db.commit()  # 将操作结果立即提交
except Exception as e:
    db.rollback()  # 事务回滚
    print(e)

# 关闭游标和数据库连接
cur.close()
db.close()
