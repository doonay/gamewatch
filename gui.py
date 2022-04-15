import db_full
import pyParser
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem

size = Window.size
print(size)

class GameCard(MDCard):
    source = StringProperty()
    text = StringProperty()
    shadow = StringProperty()

class Screen(FloatLayout):
    cards = []
    img_count = 0

    def scan_games(self, year='22'):
        year = self.textinput.text
        finalCardList = pyParser.parsing('20' + year)
        #print('20' + year)
        #for i in finalCardList:
        #    print(i)

    def get_games_from_db(self):
        self.cards = db_full.db_select_all_data('games')
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        for card in self.cards:
            self.ids.list_wgt.add_widget(
                OneLineListItem(text=str(card[0]))
            )

        if os.path.exists(filename):
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]
            pass
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]
            pass

    def next_game(self):
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count += 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]

    def prev_game(self):
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count -= 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.game_card.source = filename
            self.game_card.text = self.cards[self.img_count][0]
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.game_card.source = filename
            self.game_card.text = self.cards[self.img_count][0]

class GuiApp(MDApp):
    def build(self):
        return Screen()

    def on_start(self, **kwargs):
        #self.root.textinput.text = '22'
        self.root.get_games_from_db()

if __name__ == '__main__':
	GuiApp().run()