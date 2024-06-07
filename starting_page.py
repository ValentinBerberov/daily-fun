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

Window.clearcolor = 0.396, 0.718, 1, 1

# Main Menu Screen
class MainMenu(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(**kwargs)
        self.switch_screen = switch_screen
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 50


        self.add_widget(Label(text="Меню за игри!", color = (1,0.149,0.149,1),font_name='fonts/SeymourOne-Regular.ttf', font_size='48sp', size_hint=(1, 0.2)))

        btn_wordle = Button(text="Уърдъл", background_color=(0, 0.051,1,1), font_name='fonts/SeymourOne-Regular.ttf',font_size='32sp', size_hint=(1, 0.2))
        btn_wordle.bind(on_press=lambda x: self.switch_screen('wordle'))
        self.add_widget(btn_wordle)

        btn_riddle = Button(text="Познай гатанката", background_color=(0, 0.051,1,1) ,font_name='fonts/SeymourOne-Regular.ttf',font_size='32sp', size_hint=(1, 0.2))
        btn_riddle.bind(on_press=lambda x: self.switch_screen('riddle'))
        self.add_widget(btn_riddle)

if __name__ == '__main__':
    MainMenu().run()