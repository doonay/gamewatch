import db_full
import pyParser
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

size = Window.size
print(size)


class Screen(FloatLayout):
    cards = []
    img_count = 0

    def scan_games(self, year='22'):
        year = self.text_year.text
        finalCardList = pyParser.parsing('20' + year)
        #print('20' + year)
        for i in finalCardList:
            print(i)

    def get_games_from_db(self):
        self.cards = db_full.db_select_all_data('games')
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'
        pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
        self.pic.source = 'assets/' + self.cards[self.img_count][0] + '.jpg'

    def next_game(self):
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count += 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.pic.source = filename
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.pic.source = 'assets/' + self.cards[self.img_count][0] + '.jpg'

    def prev_game(self):
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count -= 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.pic.source = filename
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.pic.source = 'assets/' + self.cards[self.img_count][0] + '.jpg'


class GuiApp(App):
    def build(self):
        return Screen()

    def on_start(self, **kwargs):
        self.root.text_year.text = '22'
        self.root.get_games_from_db()

if __name__ == '__main__':
	GuiApp().run()