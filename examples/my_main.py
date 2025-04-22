import os #для взаимодействия с ОС
import psycopg2 #для взаимодействия с PostgreSQL
from dotenv import load_dotenv #

load_dotenv()

connection = psycopg2.connect(
    host=os.environ.get('PG_HOST'),
    port=os.environ.get('PG_PORT'),
    user=os.environ.get('PG_USER'),
    password=os.environ.get('PG_PASSWORD'),
    dbname=os.environ.get('PG_DATABASE')
    # sslmode='require'
)

connection.autocommit = True

cursor = connection.cursor()

# Вариант 2: Вывод тестового сообщения
cursor.execute("SELECT %s as connected;", ('Connection to postgres successful!',))
print(cursor.fetchall())  # ('Connection to postgres successful!',)

#
# query = 'INSERT INTO test VALUES(%s, %s);'
# queryArgument = ('dima', 1)
# cursor.execute(query, ('vadim', 5))
#

# #
readDataQuery = 'SELECT * FROM test WHERE name = %s;'
cursor.execute(readDataQuery, ('dima',))
for record in cursor.fetchall():
    print(record)
# #

cursor.close()
connection.close()

# createTableQuery = """
#     CREATE TABLE IF NOT EXISTS my_table(
#       id BIGSERIAL PRIMARY KEY NOT NULL ,
#       name varchar,
#       date TIMESTAMP NOT NULL DEFAULT current_timestamp
#     );
#   """
# cursor.execute(createTableQuery)





# #  Вариант 1: Вывод имени БД
# cursor.execute("SELECT %s as db_name;", (os.environ.get('PG_DATABASE')))
# print(cursor.fetchone())  # Например: ('test',)