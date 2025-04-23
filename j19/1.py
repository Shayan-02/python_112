import sqlite3
connection = sqlite3.connect("./j19/dbpython_112.db")
cursor = connection.cursor()

sql = """
 CREATE TABLE IF NOT EXISTS user (
 userId INTEGER ,
 name VARCHAR (60),
 family VARCHAR (60),
 email VARCHAR (60)
 );
"""

# cursor.execute("""
#     create table if not exists teacher (
#         teacherID INTEGER,
#         name text,
#         family text,
#         email text
#     )
# """)

cursor.execute(sql)

sql = """
 INSERT INTO user VALUES (4,'Django course',5000,'this is django course using python language');
"""
cursor.execute(sql)

connection.commit()
connection.close()
