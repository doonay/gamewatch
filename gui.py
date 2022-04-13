import db_full
import pyParser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

size = Window.size
print(size)


class Screen(FloatLayout):

    def scan_games(self):
        pass

    def get_games_from_db(self):
        pass

    def next_game(self):
        print('next')

    def prev_game(self):
        print('prev')

class GuiApp(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
	GuiApp().run()