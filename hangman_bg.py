<<<<<<< Updated upstream
=======
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


kivy.require('1.11.1')


# def get_random_word(game_type):
#     conn = sqlite3.connect('game_words.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT word FROM words WHERE game_type = ?", (game_type,))
#     words = cursor.fetchall()
#     conn.close()
#     return random.choice(words)[0]


# Main Menu Screen
class MainMenu(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        self.padding = 55
        self.spacing = 55

        #self.welcomeLabel = Label(text="WELCOME TO GAME MENU!", font_size='40sp', size_hint=(None, None))
        #self.welcomeLabel.bind(size=self.welcomeLabel.setter('text_size'))
        #BoxLayout.add_widget(self.welcomeLabel)

        self.add_widget(Label(text="Welcome to the Game Menu", font_size='32sp', size_hint=(1, 0.2)))
        #self.animate_label()

        btn_wordle = Button(text="Wordle", font_size='24sp', size_hint=(1, 0.2))
        btn_wordle.bind(on_press=lambda x: self.switch_screen('wordle'))
        self.add_widget(btn_wordle)

        btn_riddle = Button(text="Riddle Guessing", font_size='24sp', size_hint=(1, 0.2))
        btn_riddle.bind(on_press=lambda x: self.switch_screen('riddle'))
        self.add_widget(btn_riddle)

    #def animate_label(self, instance):
        #grow = Animation(width = 200, height = 100, duration = 1.5)
        #shrink = Animation(width = 100, height = 50, duration = 1.5)
        #animation_label = grow + shrink
        #animation_label.start(self.welcomeLabel)



# Wordle Game Screen
class WordleGame(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.word = "APPLE".upper()
        self.attempts = []        
        self.max_attempts = 5

        self.top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        #self.btn_hangman = Button(text="Hangman", font_size='20sp')
        #self.btn_hangman.bind(on_press=lambda x: self.switch_screen('hangman'))
        #self.top_layout.add_widget(self.btn_hangman)

        self.btn_riddle = Button(text="Riddle", font_size='20sp')
        self.btn_riddle.bind(on_press=lambda x: self.switch_screen('riddle'))
        self.top_layout.add_widget(self.btn_riddle)
        
        self.add_widget(self.top_layout)

        self.wordle_layout = GridLayout(cols=1, size_hint=(1, 0.7))
        self.add_widget(self.wordle_layout)

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.word_input = TextInput(multiline=False, font_size='32sp', size_hint=(0.7, 1))
        self.guess_button = Button(text="Guess", font_size='32sp', size_hint=(0.3, 1))
        self.guess_button.bind(on_press=self.make_guess)
        self.input_layout.add_widget(self.word_input)
        self.input_layout.add_widget(self.guess_button)
        self.add_widget(self.input_layout)

    def make_guess(self, instance):
        guess = self.word_input.text.upper()
        self.word_input.text = ''

        if len(guess) == 5 and guess.isalpha() and guess not in self.attempts:
            self.attempts.append(guess)
            self.update_display()

            if guess == self.word:
                self.end_game(win=True)
            elif len(self.attempts) >= self.max_attempts:
                self.end_game(win=False)

    def update_display(self):
        self.wordle_layout.clear_widgets()
        for attempt in self.attempts:
            hbox = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
            for i, letter in enumerate(attempt):
                color = (1, 1, 1, 1)
                if letter == self.word[i]:
                    color = (0, 1, 0, 1)  # Green
                elif letter in self.word:
                    color = (1, 1, 0, 1)  # Yellow
                lbl = Label(text=letter, font_size='24sp', color=color)
                hbox.add_widget(lbl)
            self.wordle_layout.add_widget(hbox)

    def end_game(self, win):
        if win:
            self.wordle_layout.add_widget(Label(text=f"You won! The word was {self.word}", font_size='32sp'))
        else:
            self.wordle_layout.add_widget(Label(text=f"You lost! The word was {self.word}", font_size='32sp'))
        self.word_input.disabled = True
        self.guess_button.disabled = True

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
        #self.btn_hangman = Button(text="Hangman", font_size='20sp')
        #self.btn_hangman.bind(on_press=lambda x: self.switch_screen('hangman'))
        #self.top_layout.add_widget(self.btn_hangman)

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
>>>>>>> Stashed changes
