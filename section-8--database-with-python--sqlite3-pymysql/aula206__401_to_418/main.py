# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql

dotenv.load_dotenv()


TABLE_NAME = "customers"


connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS ${TABLE_NAME} ("
            "id INT NOT NULL AUTO_INCREMENT, "
            "nome VARCHAR(50) NOT NULL, "
            "idade INT NOT NULL, "
            "PRIMARY KEY (id) "
            ")"
        )
        # Cuidado, isso apaga todos os dados da tabela
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}") 
        
    # Inserir dados        
    with connection.cursor() as cursor:
        insert_query = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES "
            "(%s, %s)"
        )
        cursor.execute(insert_query, ("Luiz", 25))
        
        insert_query_2 = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES "
            "(%(name)s, %(age)s)"
        )
        data = {"name": "Maria", "age": 30}
        cursor.execute(insert_query_2, data)

        data_list = [
            {"name": "Le", "age": 41},
            {"name": "Sara", "age": 35},
            {"name": "Carlos", "age": 11},
        ]
        cursor.executemany(insert_query_2, data_list)
    connection.commit()

    # Consultar dados
    with connection.cursor() as cursor:
        search_query = f"SELECT * FROM {TABLE_NAME} WHERE idade > %s"
        cursor.execute(search_query, (18,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        
        print("--" * 20)
        find_query = f"SELECT * FROM {TABLE_NAME} WHERE id = %s"
        cursor.execute(find_query, (2,))
        result = cursor.fetchone()
        print(result)

    # Apagar dados
    with connection.cursor() as cursor:
        delete_query = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
        cursor.execute(delete_query, (3,))
        connection.commit()
        
        print("--" * 20)
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        results = cursor.fetchall()
        for row in results:
            print(row)

    # Atualizar dados
    with connection.cursor() as cursor:
        update_query = (
            f"UPDATE {TABLE_NAME} "
            "SET nome = %s "
            "WHERE id = %s"
        )
        cursor.execute(update_query, ("Maria Eduarda", 2))
        connection.commit()

        print("--" * 20)
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        results = cursor.fetchall()
        for row in results:
            print(row)


print("\nDictionary Cursor")
print("==" * 20)
other_connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    cursorclass=pymysql.cursors.DictCursor,  # Retorna dicionários ao invés de tuplas
)

with other_connection:
    with other_connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        results = cursor.fetchall()
        print("--" * 20)
        for row in results:
            print(row)
        
        print("--" * 20)
        for row in results:
            print(row["nome"], row["idade"])

        # usando scroll para navegar pelos resultados
        cursor.scroll(-2) # volta 2 posições
        print("--" * 20)
        for row in cursor.fetchall():
            print(row)

        cursor.scroll(0, mode="absolute") # volta para o início
        print("--" * 20)
        for row in cursor.fetchall():
            print(row)


print("\nServer Side Cursor")
print("==" * 20)
another_connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    cursorclass=pymysql.cursors.SSDictCursor,  # Server Side Cursor, carrega aos poucos os dados do servidor. Existe tambem o SScursor (tuplas)
)

with another_connection:
    with another_connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        print("--" * 20)
        for row in cursor.fetchall_unbuffered():
            print(row)
            if row["id"] >= 2:
                break  # para testar o carregamento aos poucos
        
        print("--" * 20)
        for row in cursor.fetchall_unbuffered():
            print(row)
