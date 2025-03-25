import mysql.connector
import re

pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
text = "<html>这里是一些网址：(http://example.com), 发顺丰的<b>ads</b>https://secure.example.com, （www.example.org）测试</html>"
matches = re.findall(pattern, text)

for match in matches:
    print(match)

# conn = conn = mysql.connector.connect(user='root', password='', host='localhost', port='3306', database='yijingdb', use_unicode=True)

# database_config = { 'user':'root', 'password':'', 'host':'localhost', 'database':'hbzb_cms' }
# connection = mysql.connector.connect(**database_config)
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM cms_info_clob WHERE f_info_id in (SELECT f_info_id FROM cms_info_node WHERE f_node_id=280)")
# rows = cursor.fetchall()
# print('rows', len(rows))
# i = 0
# for row in rows:
#     i = i+1
#     primary_key = row[0]
#     data = row[2]
#     print(data)
#     url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#     updated_data = re.sub(url_regex, '', data)
#     print(updated_data)
#     if i>1:
#         break
#     # cursor.execute("UPDATE cms_info_clob SET f_value=%s WHERE f_info_id=%s", (updated_data, primary_key))
# connection.commit() 
# cursor.close() 
# connection.close()