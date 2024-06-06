import sqlite3

def setup_database():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS hangman_words (
                        id INTEGER PRIMARY KEY,
                        word TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS wordle_words (
                        id INTEGER PRIMARY KEY,
                        word TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS riddle_words (
                        id INTEGER PRIMARY KEY,
                        riddle TEXT NOT NULL,
                        answer TEXT NOT NULL)''')

    # Insert sample data
    hangman_words = ['python', 'kivy', 'hangman']
    wordle_words = ['apple', 'grape', 'berry']
    riddle_words = [
        ('I speak without a mouth and hear without ears. I have no body, but I come alive with wind.', 'echo')
    ]

    cursor.executemany('INSERT INTO hangman_words (word) VALUES (?)', [(word,) for word in hangman_words])
    cursor.executemany('INSERT INTO wordle_words (word) VALUES (?)', [(word,) for word in wordle_words])
    cursor.executemany('INSERT INTO riddle_words (riddle, answer) VALUES (?, ?)', riddle_words)

    conn.commit()
    conn.close()

setup_database()
