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

# Example word to guess
words = ["абвгд", "бвгде", "вгдеж"]

secret_word = random.choice(words)
print(secret_word)

class WordleGame(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=11
        width = Window.size[0]
        height = Window.size[1]

        keys = [ 'Я', 'В', 'Е', 'Р', 'Т', 'Ъ', 'У', 'И', 'О', 'П', 'Ч',
                'А', 'С', 'Д', 'Ф', 'Г', 'Х', 'Й', 'К', 'Л', 'Ш', 'Щ',
                'Enter', 'З', 'Ь', 'Ц', 'Ж', 'Б', 'Н', 'М', 'Ю', 'Delete' ]
        
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
                    self.square = Rectangle(pos=(250+60*j, 480-i*60), size=(50, 50))
                    self.squares.append(self.square)
        
        
        for i in range(6):
            for j in range(5):
                self.label = Label(text="", pos=(60*j-124, 205-i*60), font_size=30, bold=True)
                self.labels.append(self.label)
                self.add_widget(self.label)

        for i in range(2):
                for j in range(11):
                    if i==2 and j>=10:
                        break
                    self.button = Button(text=keys[11*i+j], pos=(95+55*j, 110-i*55), size_hint=(None, None), size=(50, 50))
                    self.button.bind(on_press=self.on_key_press)
                    self.buttons.append(self.button)
                    self.add_widget(self.button)
        
        for j in range(10):
            self.button = Button(text=keys[22+j], pos=(125+55*j, 0), size_hint=(None, None), size=(50, 50))
            self.button.bind(on_press=self.on_key_press)
            self.buttons.append(self.button)
            self.add_widget(self.button)

    

        
    def on_key_press(self, instance):
        key=instance.text
        if len(self.user_input) < 5:
            if key!='Enter' and key!='Delete':
                self.user_input+=key
        if key=='Delete':
            self.user_input = self.user_input[:-1]
            
            self.labels[self.tries*5+len(self.user_input)].text=""
            
        if len(self.user_input) == 5:
            if key=="Enter":
                self.answers.append(self.user_input)
                self.user_input = ""
                colors = self.check_letters()
                self.color_buttons(colors)
                self.tries+=1
        print(self.user_input)
        for i in range(len(self.user_input)):
            self.labels[self.tries*5+i].text=self.user_input[i]
        pass

    def check_letters(self):
        colors = []

        for i in range(0, 5):
            if self.answers[self.tries][i].lower() == secret_word[i]:
                colors.append("G")
            elif self.answers[self.tries][i].lower() in secret_word:
                colors.append("Y")
            else:
                colors.append("N")

        return colors
    
    def check_word(self):
        if self.answers[self.tries]==secret_word:
            print("You Win!")
        
        return True
    
    def color_buttons(self, colors):
        for i in range(5):
            for button in self.buttons:
                if button.text==self.answers[self.tries][i]:
                    if colors[i]=="G":
                        button.background_color=(0, 0.8, 0, 1)
                    elif colors[i]=="Y":
                        button.background_color=(0.8, 0.8, 0, 1)
                    elif colors[i]=="N":
                        button.background_color=(0.2, 0.2, 0.2, 1)
            


class WordleApp(App):
    def build(self):
        return WordleGame()

if __name__ == '__main__':
    WordleApp().run()
