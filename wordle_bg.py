import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView

# Example word to guess
SECRET_WORD = "PYTHON"

class WordleGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.guess_input = TextInput(
            hint_text='Enter your guess',
            multiline=False,
            size_hint=(1, 0.1),
            font_size=32
        )
        self.add_widget(self.guess_input)

        self.submit_button = Button(
            text='Submit Guess',
            size_hint=(1, 0.1),
            font_size=32,
            on_press=self.check_guess
        )
        self.add_widget(self.submit_button)

        self.result_grid = GridLayout(
            cols=len(SECRET_WORD),
            size_hint=(1, 0.8),
            spacing=5
        )
        self.add_widget(self.result_grid)

    def check_guess(self, instance):
        guess = self.guess_input.text.upper()
        if len(guess) != len(SECRET_WORD):
            self.show_popup('Error', 'Invalid guess length')
            return

        self.result_grid.clear_widgets()
        for i, char in enumerate(guess):
            color = self.get_color(char, i)
            label = Label(
                text=char,
                color=color,
                font_size=32,
                size_hint=(1, 1)
            )
            self.result_grid.add_widget(label)
        self.guess_input.text = ''

    def get_color(self, char, index):
        if char == SECRET_WORD[index]:
            return (0, 1, 0, 1)  # Green
        elif char in SECRET_WORD:
            return (1, 1, 0, 1)  # Yellow
        else:
            return (0.5, 0.5, 0.5, 1)  # Grey

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint=(1, 0.25))
        content.add_widget(close_button)
        popup = Popup(title=title, content=content, size_hint=(0.5, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

class WordleApp(App):
    def build(self):
        return WordleGame()

if __name__ == '__main__':
    WordleApp().run()