import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS users_table (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS items_table (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(query)

connection.commit()
connection.close()
