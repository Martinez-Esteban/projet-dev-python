from curses import curs_set
import sqlite3
import bcrypt


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
        wins INTEGER,
        looses INTEGER,
        games INTEGER
    )""")

    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)",
                   (username, password))
    cursor.execute("INSERT INTO scores (username, wins, looses, games) VALUES (?, ?, ?, ?)",
                   (username, 0, 0, 0))
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


def add_win(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE scores SET wins = wins + 1 WHERE username = ?", (username,))
    cursor.execute(
        "UPDATE scores SET games = games + 1 WHERE username = ?", (username,))
    conn.commit()
    conn.close()


def add_loose(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE scores SET looses = looses + 1 WHERE username = ?", (username,))
    cursor.execute(
        "UPDATE scores SET games = games + 1 WHERE username = ?", (username,))
    conn.commit()
    conn.close()


def tie(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE scores SET games = games +1 WHERE username = ?", (username,))
    conn.commit()
    conn.close()


def get_scores():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    scores = cursor.execute(
        "SELECT * FROM scores ORDER BY wins DESC;").fetchall()
    conn.commit()
    conn.close()
    return scores
