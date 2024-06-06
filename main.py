import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.animation import Animation
import sqlite3

from starting_page import *

from wordle_bg import *

from riddles_bg import *

import database as dp

dp.setup_database()

# Database helper functions
def get_random_word(game_type):
    conn = sqlite3.connect('game_words.db')
    cursor = conn.cursor()

    if game_type == 'wordle':
        cursor.execute('SELECT word FROM wordle_words ORDER BY RANDOM() LIMIT 1')
    elif game_type == 'riddle':
        cursor.execute('SELECT riddle, answer FROM riddle_words ORDER BY RANDOM() LIMIT 1')

    word = cursor.fetchone()
    conn.close()
    print(word)
    return word

class MyGameApp(App):
    def build(self):
       self.screen_manager = BoxLayout()
       self.switch_screen('main_menu')
       return self.screen_manager

    def switch_screen(self, screen_name):
        self.screen_manager.clear_widgets()
        if screen_name == 'main_menu':
            self.screen_manager.add_widget(MainMenu(switch_screen=self.switch_screen))
        elif screen_name == 'wordle':
             self.screen_manager.add_widget(WordleGame(switch_screen=self.switch_screen))
        elif screen_name == 'riddle':
             self.screen_manager.add_widget(RiddleGame(switch_screen=self.switch_screen))

if __name__ == '__main__':
    MyGameApp().run()