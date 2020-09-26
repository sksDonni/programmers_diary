from sqlite3 import *

conn = connect("projects.db")

cursor = conn.cursor()
cursor.execute("""SELECT * FROM project_names""")
# conn.commit()
record = cursor.fetchall()
print(record)