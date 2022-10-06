import mysql.connector as m

db = 'miniproject'

connection = m.connect(host='localhost', user='root',
                    password='admin', database=db)

cursor = connection.cursor()

cursor.execute('SHOW TABLES;')
table_names = []
for record in cursor.fetchall():
    table_names.append(record[0])

backup_test = db + '_backup'
try:
    cursor.execute(f'CREATE DATABASE {backup_test}')
except:
    pass

cursor.execute(f'USE {backup_test}')

for table_name in table_names:
cursor.execute(
        f'CREATE TABLE {table_name} SELECT * FROM {db}.{table_name}')
