import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
import random

from random_word import get_random_word

# Example word to guess
words = ["абвгд", "бвгде", "вгдеж"]


class WordleGame(FloatLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        Window.size_hint=(None, None)
        Window.size=(800, 600)
        
        self.padding = (35, 10)
        self.spacing = 35

        self.secret_word = ""  

        self.keys = ['Я', 'В', 'Е', 'Р', 'Т', 'Ъ', 'У', 'И', 'О', 'П', 'Ч',
                'А', 'С', 'Д', 'Ф', 'Г', 'Х', 'Й', 'К', 'Л', 'Ш', 'Щ',
                'Enter', 'З', 'Ь', 'Ц', 'Ж', 'Б', 'Н', 'М', 'Ю', 'Delete', 'Clear']

        self.restart()
        
        
    def generate_word(self):
        self.secret_word = get_random_word('wordle')

    def on_key_press(self, instance):
        key = instance.text
        if len(self.user_input) < 5:
            if key != 'Enter' and key != 'Delete':
                self.user_input += key
        if key == 'Delete':
            self.user_input = self.user_input[:-1]

            self.labels[self.tries * 5 + len(self.user_input)].text = ""

        if key == 'Clear':
            self.user_input = ""
            for i in range(5):
                self.labels[self.tries * 5 + i].text = ""

        if len(self.user_input) == 5:
            if key == "Enter":
                self.answers.append(self.user_input)
                self.user_input = ""
                colors = self.check_letters()
                self.color_buttons(colors)
                self.color_grid(colors)
                res = self.check_word()
                if res or self.tries == 5:
                    self.show_popup(res)
                self.tries += 1
        for i in range(len(self.user_input)):
            self.labels[self.tries * 5 + i].text = self.user_input[i]
        pass

    def check_letters(self):
        colors = []

        for i in range(0, 5):
            if self.answers[self.tries][i].lower() == self.secret_word[i]:
                colors.append("G")
            elif self.answers[self.tries][i].lower() in self.secret_word:
                colors.append("Y")
            else:
                colors.append("N")

        return colors

    def check_word(self):
        if self.answers[self.tries].lower() == self.secret_word.lower():
            return True
        else:
            return False

    def show_popup(self, result):
        content = BoxLayout(orientation="vertical")

        if result:
            label = Label(text="You win!", font_size=24)
        elif not result and self.tries == 5:
            label = Label(text="You lose!", font_size=24)

        close_button = Button(text="Restart", size=(100, 50))
        close_button.x=100
        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title="Result",
                      content=content,
                      size_hint=(None, None),
                      size=(300, 200),
                      auto_dismiss=True)

        close_button.bind(on_release=popup.dismiss, on_press=self.restart_button)
        
        popup.open()

    def color_grid(self, colors):
        for i in range(5):
            color = colors[i]
            if color == "G":
                self.canvas.add(Color(0, 0.5, 0, 1))
            elif color == "Y":
                self.canvas.add(Color(0.8, 0.8, 0, 1))
            else:
                self.canvas.add(Color(0.4, 0.4, 0.4, 1))

            self.canvas.add(self.squares[self.tries * 5 + i])

        for label in self.labels:
            self.remove_widget(label)
        for i in range(6):
            for j in range(5):
                self.add_widget(self.labels[i * 5 + j])

        for j in range(self.tries + 1):
            for i in range(5):
                self.labels[j * 5 + i].text = self.answers[j][i]

    def color_buttons(self, colors):
        for i in range(5):
            for button in self.buttons:
                if button.text == self.answers[self.tries][i]:
                    if colors[i] == "G":
                        button.background_color = (0, 0.8, 0, 1)
                    elif colors[i] == "Y":
                        button.background_color = (0.8, 0.8, 0, 1)
                    elif colors[i] == "N":
                        button.background_color = (0.2, 0.2, 0.2, 1)

    def restart_button(self, instance):
        self.restart()

    def restart(self):
        self.clear_widgets()

        self.user_input = ""
        self.answers = []
        self.tries = 0
        self.labels = []
        self.squares = []
        self.buttons = []

        with self.canvas:

            Color(0.3, 0.3, 0.3, 1)

            for i in range(6):
                for j in range(5):
                    self.square = Rectangle(pos=(Window.size[0]*0.33+55*j, Window.size[1]*0.76-55*i), size=(50, 50))
                    self.squares.append(self.square)

        for i in range(6):
            for j in range(5):
                self.label = Label(text="", pos=(-Window.size[0]*0.1375+55*j, Window.size[1]*0.3-55*i), font_size=30, bold=True)
                
                self.labels.append(self.label)
                self.add_widget(self.label)

        keyboard_layout = GridLayout(cols=11, rows=3, size_hint=(None, None), size=(550, 150), pos_hint={'center_x':0.5, 'y':0.02})
        for key in self.keys:
            button = Button(text=key, size_hint=(None, None), size=(50, 50), background_color=(0.9, 0.9, 0.9, 1))
            button.bind(on_press=self.on_key_press)
            self.buttons.append(button)
            keyboard_layout.add_widget(button)
        self.add_widget(keyboard_layout)

        self.generate_word()

        self.top_layout = BoxLayout(orientation='horizontal', size_hint=(0.93, 0.085), pos_hint={"center_x": 0.5, "top":0.99})

        self.btn_wordle = Button(text="Портал към играта Познай гатанката", font_size='20sp')
        self.btn_wordle.bind(on_press=lambda x: self.switch_screen('riddle'))
        self.top_layout.add_widget(self.btn_wordle)

        self.add_widget(self.top_layout)

        pass