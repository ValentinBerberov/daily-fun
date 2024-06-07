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
from kivy.core.window import Window
import sqlite3

from random_word import get_random_word

# Riddle Game Screen
class RiddleGame(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        Window.size = (800, 600)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        
        self.padding = (35, 10)
        
        self.spacing = 35

        #RIDDLE TEXT AND ANSWER
        self.riddle, self.answer = get_random_word('riddle')
        self.riddle=self.riddle.upper()
        self.answer=self.answer.upper()

        self.answer
        self.attempts = []
        self.max_attempts = 5

        self.btn_wordle = Button(text="Портал към играта Уърдъл", font_size='20sp', size_hint=(None, None), size=(730, 50))
        self.btn_wordle.bind(on_press=lambda x: self.switch_screen('wordle'))
        self.add_widget(self.btn_wordle)

        self.add_widget(Label(text=self.riddle, font_size='24sp', size_hint=(1, 0.4)))

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.answer_input = TextInput(multiline=False, font_size='32sp', size_hint=(0.7, 1))
        self.guess_button = Button(text="Познай", font_size='32sp', size_hint=(0.3, 1))
        self.guess_button.bind(on_press=self.make_guess)
        self.input_layout.add_widget(self.answer_input)
        self.input_layout.add_widget(self.guess_button)
        self.add_widget(self.input_layout)

        self.feedback_label = Label(text="", font_size='24sp', size_hint=(1, 0.2))
        self.add_widget(self.feedback_label)

    def make_guess(self, instance):
        guess = self.answer_input.text.upper()
        self.answer_input.text = ''
        
        if guess:
            self.attempts.append(guess)
            if guess == self.answer:
                self.feedback_label.text = f"Ти позна! Отговорът е {self.answer}"
                self.end_game(win=True)
            elif len(self.attempts) >= self.max_attempts:
                self.feedback_label.text = f"Ти загуби! Отговорът е {self.answer}"
                self.end_game(win=False)
            else:
                self.feedback_label.text = f"Неправилно! Имаш още {self.max_attempts - len(self.attempts)} останали опита."

    def end_game(self, win):
        self.answer_input.disabled = True
        self.guess_button.disabled = True
