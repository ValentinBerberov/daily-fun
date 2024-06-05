import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

kivy.require('1.11.1')

class GameMenuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(text="Welcome to the Game Menu!", font_size='24sp', size_hint=(1, 0.2))
        layout.add_widget(label)

        # Adding buttons for the games
        btn_game1 = Button(text="Start Game 1", font_size='20sp', size_hint=(1, 0.2))
        btn_game1.bind(on_press=self.start_game1)
        layout.add_widget(btn_game1)

        btn_game2 = Button(text="Start Game 2", font_size='20sp', size_hint=(1, 0.2))
        btn_game2.bind(on_press=self.start_game2)
        layout.add_widget(btn_game2)

        btn_game3 = Button(text="Start Game 3", font_size='20sp', size_hint=(1, 0.2))
        btn_game3.bind(on_press=self.start_game3)
        layout.add_widget(btn_game3)

        return layout

    def start_game1(self, instance):
        print("Starting Game 1")

    def start_game2(self, instance):
        print("Starting Game 2")

    def start_game3(self, instance):
        print("Starting Game 3")

if __name__ == '__main__':
    GameMenuApp().run()
