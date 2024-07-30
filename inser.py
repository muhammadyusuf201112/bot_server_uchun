import sqlite3

def insert_user(user_id,username):
    conn = sqlite3.connect('toshiba_malika_bozor.db')
    curr = conn.cursor()
    
    query = "INSERT INTO users(user_id,username) VALUES(?,?)" 
    curr.execute(query, (user_id,username))

    conn.commit()
    conn.close()