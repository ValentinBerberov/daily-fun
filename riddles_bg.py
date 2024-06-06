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


# Riddle Game Screen
class RiddleGame(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind."
        self.answer = "ECHO".upper()
        self.attempts = []
        self.max_attempts = 4

        self.top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.btn_hangman = Button(text="Hangman", font_size='20sp')
        self.btn_hangman.bind(on_press=lambda x: self.switch_screen('hangman'))
        self.top_layout.add_widget(self.btn_hangman)

        self.btn_wordle = Button(text="Wordle", font_size='20sp')
        self.btn_wordle.bind(on_press=lambda x: self.switch_screen('wordle'))
        self.top_layout.add_widget(self.btn_wordle)
        
        self.add_widget(self.top_layout)

        self.add_widget(Label(text=self.riddle, font_size='24sp', size_hint=(1, 0.4)))

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.answer_input = TextInput(multiline=False, font_size='32sp', size_hint=(0.7, 1))
        self.guess_button = Button(text="Guess", font_size='32sp', size_hint=(0.3, 1))
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
                self.feedback_label.text = f"You got it! The answer is {self.answer}"
                self.end_game(win=True)
            elif len(self.attempts) >= self.max_attempts:
                self.feedback_label.text = f"You lost! The answer was {self.answer}"
                self.end_game(win=False)
            else:
                self.feedback_label.text = f"Incorrect! You have {self.max_attempts - len(self.attempts)} attempts left."

    def end_game(self, win):
        self.answer_input.disabled = True
        self.guess_button.disabled = True

class MyGameApp(App):
    def build(self):
        self.screen_manager = BoxLayout()
        self.switch_screen('main_menu')
        return self.screen_manager

    def switch_screen(self, screen_name):
        self.screen_manager.clear_widgets()
        if screen_name == 'main_menu':
            self.screen_manager.add_widget(MainMenu(switch_screen=self.switch_screen))
        elif screen_name == 'hangman':
            self.screen_manager.add_widget(HangmanGame(switch_screen=self.switch_screen))
        elif screen_name == 'wordle':
            self.screen_manager.add_widget(WordleGame(switch_screen=self.switch_screen))
        elif screen_name == 'riddle':
            self.screen_manager.add_widget(RiddleGame(switch_screen=self.switch_screen))

if __name__ == '__main__':
    MyGameApp().run()
