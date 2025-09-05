import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILENAME = "db.sqlite3"
DB_PATH = ROOT_DIR / DB_FILENAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# criar tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "name TEXT, "
    "weight REAL"
    ")"
)
connection.commit()

# limpando a tabela e reiniciando o AUTOINCREMENT
cursor.execute(f"DELETE FROM {TABLE_NAME}")
cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")
connection.commit()

# Registrar valores nas colunas da tabela
insert_qurery = (
    f"INSERT INTO {TABLE_NAME} "
    "(name, weight) "
    "VALUES "
    "(?, ?)"
)
cursor.execute(insert_qurery, ('Maria', 60.5))
cursor.executemany(insert_qurery, [('Pedro', 63.2), ('Eduardo', 71.9)])
insert_qurery_2 = (
    f"INSERT INTO {TABLE_NAME} "
    "(name, weight) "
    "VALUES "
    "(:nome, :peso)"
)
cursor.execute(insert_qurery_2, {'nome': 'João', 'peso': 83.2})
cursor.executemany(insert_qurery_2, [
    {'nome': 'Ana', 'peso': 59.1},
    {'nome': 'Carla', 'peso': 47.8},
])
connection.commit()

# removendo registros
cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = 3")
connection.commit()

# atualizando registros
cursor.execute(f"UPDATE {TABLE_NAME} SET weight = 65.0 WHERE id = 2")
connection.commit()

cursor.close()
connection.close()
