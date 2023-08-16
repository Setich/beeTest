import sqlite3

db = sqlite3.connect(":memory:")
sql = db.cursor()

sql.execute("""
    CREATE TABLE clients (
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        change_date TEXT NOT NULL
        )""")

sql.execute("INSERT INTO clients (id, name, change_date) VALUES (?, ?, ?)", (1, 'Aleksey', "16.08.23"))

sql.execute("UPDATE clients SET id = ?, name = ?, change_date = ? where id = ?",
            (32, 'Anton', '22.12.2019', 1))

sql.execute('DELETE FROM clients WHERE name = ?', ('Anton',))

db.commit()

db.close()



