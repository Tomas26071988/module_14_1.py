import sqlite3

connection = sqlite3.connect('.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
) 
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                   (f"User1{i}", f"{i}example1@gmail.com", f'{i * 10}', '1000'))

cursor.execute('UPDATE Users SET balance = 500 WHERE id IN (1, 3, 5, 7, 9)')
cursor.execute('DELETE FROM Users WHERE id IN (3, 6, 9)')

# записываю изменения
connection.commit()

# выделяю все (можно со звездочкой делать ) и прописываю где нет возраста 60)
cursor.execute('SELECT * FROM Users WHERE age != 60')
res = cursor.fetchall()

for record in res:
   print(f'Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}')

connection.commit()
connection.close()
