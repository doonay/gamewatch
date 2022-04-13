import db_full
import pyParser
import requests

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

    def scan_games(self, year='22'):
        year = self.text_year.text
        finalCardList = pyParser.parsing('20' + year)
        #print('20' + year)
        for i in finalCardList:
            print(i)

    def get_games_from_db(self):
        self.cards = db_full.db_select_all_data('games')
        #назначаем картинку
        #self.pic.canvas.source =
        print(type(self.cards))
        #for card in self.cards:
        #    print(card)
        print('downloading...', self.cards[0][2])
        self.img_downloader(self.cards[0][2])
        self.pic.source = 'assets/img.jpg'

    def next_game(self):
        print('next')

    def prev_game(self):
        print('prev')

    def img_downloader(self, link):
        p = requests.get(link)
        out = open("assets/img.jpg", "wb")
        out.write(p.content)
        out.close()


class GuiApp(App):
    def build(self):
        return Screen()

    def on_start(self, **kwargs):
        print(dir(self.root))
        self.root.text_year.text = '22'
        self.root.get_games_from_db()

if __name__ == '__main__':
	GuiApp().run()