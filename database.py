import sqlite3

def setup_database():
    conn = sqlite3.connect('game_words.db')
    cursor = conn.cursor()

    cursor.execute(f'DROP TABLE IF EXISTS wordle_words')

    cursor.execute(f'DROP TABLE IF EXISTS riddle_words')


    cursor.execute('''CREATE TABLE IF NOT EXISTS wordle_words (
                        id INTEGER PRIMARY KEY,
                        word TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS riddle_words (
                        id INTEGER PRIMARY KEY,
                        riddle TEXT NOT NULL,
                        answer TEXT NOT NULL)''')

    # Insert sample data

    wordle_words = ['пазар', 'пачка', 'порив', 'попче']
    riddle_words = [
        ('Труди се направо здраво и надясно, и наляво.', 'ключът'), ('От мен запомни: каквото и да правиш, в тези вълни няма да се удавиш.', 'радиовълните'), 
        ('Скромна е моята щерка, знам, но я целуват всички с план','чашата')
    ]


    cursor.executemany('INSERT INTO wordle_words (word) VALUES (?)', [(word,) for word in wordle_words])
    cursor.executemany('INSERT INTO riddle_words (riddle, answer) VALUES (?, ?)', riddle_words)

    conn.commit()
    conn.close()

