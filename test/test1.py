#codeing=utf-8
import MySQLdb

conn = MySQLdb.connect(host='172.16.109.105',port=3306,user='root',passwd='root',db='itgfz2014',charset='utf8')

cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

members = cursor.execute("select * from itgfz_member")

for member in cursor.fetchmany(members):
    print member

cursor.close()
conn.commit()
conn.close()