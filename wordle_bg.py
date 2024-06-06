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


# Wordle Game Screen
class WordleGame(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        self.padding = 35
        self.spacing = 35

        #
        self.word = "APPLE".upper()
        self.attempts = []
        self.max_attempts = 5

        self.top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        self.btn_riddle = Button(text="Портал към играта Познай гатанката", font_size='20sp')
        self.btn_riddle.bind(on_press=lambda x: self.switch_screen('riddle'))
        self.top_layout.add_widget(self.btn_riddle)
        
        self.add_widget(self.top_layout)

        self.wordle_layout = GridLayout(cols=1, size_hint=(1, 0.7))
        self.add_widget(self.wordle_layout)

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.word_input = TextInput(multiline=False, font_size='32sp', size_hint=(0.7, 1))
        self.guess_button = Button(text="Познай", font_size='32sp', size_hint=(0.3, 1))
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
