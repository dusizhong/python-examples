import mysql.connector
def query_db():
    # ①、连接数据库
    conn = conn = mysql.connector.connect(user='root', password='',
        host='localhost', port='3306', database='yijingdb', use_unicode=True)
    # ②、获取游标
    c = conn.cursor()
    # ③、调用执行select语句查询数据
    c.execute('select * from book_chapter where chapter_sort > %s', (1,))
    # 通过游标的description属性获取列信息
    description = c.description
    # 使用fetchall获取游标中的所有结果集
    rows = c.fetchall()
    # ④、关闭游标
    c.close()
    # ⑤、关闭连接
    conn.close()
    return description, rows