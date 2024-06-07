import sqlite3

def get_random_word(game_type):
    conn = sqlite3.connect('game_words.db')
    cursor = conn.cursor()

    if game_type == 'wordle':
        cursor.execute('SELECT word FROM wordle_words ORDER BY RANDOM() LIMIT 1')
    elif game_type == 'riddle':
        cursor.execute('SELECT riddle, answer FROM riddle_words ORDER BY RANDOM() LIMIT 1')

    word = cursor.fetchone()
    conn.close()
    if game_type == 'wordle':
        word = word[0]
    print(word)
    return word