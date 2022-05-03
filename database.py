import sqlite3, bcrypt

def connect():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        score TEXT
    )""")

    conn.commit()
    conn.close()
    
def add_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
    conn.commit()
    conn.close()
    
def check_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is None:
        print("Wrong username")
        return False
    else:
        if bcrypt.checkpw(password, result[2]):
            return True
        else:
            return False
        
def user_not_exist(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is None:
        return True
    else:
        return False