import sqlite3

conn=sqlite3.connect('employee.db')

cur=conn.cursor()

# cur.execute("""
# CREATE TABLE employee (
#         firstname text,
#         lastname text,
#         pay integer
#         )
# """)

# cur.execute("""
# INSERT INTO employee VALUES ('mary','ts',1000)
# """)
conn.commit()
cur.execute("SELECT * FROM employee where firstname='mary' ")
print(cur.fetchall())

conn.close()
