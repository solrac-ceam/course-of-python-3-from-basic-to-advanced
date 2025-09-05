import sqlite3

from main import DB_PATH, TABLE_NAME

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)
    
cursor.close()
connection.close()
