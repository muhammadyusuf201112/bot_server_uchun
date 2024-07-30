import sqlite3
def create_db():
    conn = sqlite3.connect('toshiba_malika_bozor.db')
    curr = conn.cursor()
    curr.execute("""
    CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username VARCHAR(25)
    )
    """)

    conn.commit()
    conn.close()

print('Kutubxona muvafaqiyatli ishga tushdi')