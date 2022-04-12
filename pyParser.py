import requests
from bs4 import BeautifulSoup
import sqlite3

def parsing(year: int):
	host = 'https://www.igromania.ru'
	url = '/games/pc/all/' + str(year) + '/'
	img_prefix = 'https:'
	link_prefix = 'https://www.igromania.ru'		
	allLinksOfYear = []

	r = requests.get(host + url)
	soup = BeautifulSoup(r.text, 'lxml')

	pages = soup.find('div', class_='pages').find_all('a')
	last_page = int(pages[1].get_text())

	for page in range(last_page):
		cards_page = host + url + 'all/all/0/' + str(page + 1) + '/'
		allLinksOfYear.append(cards_page)

	finalCardList = []
	for link in allLinksOfYear:
		#print(link)
		r = requests.get(link)
		soup = BeautifulSoup(r.text, 'lxml')
		gamecards = soup.find_all('div', class_='game-card')
		for gamecard in gamecards:
			base_string = gamecard.find('a')
			name = base_string.img.get('alt')
			img_link = img_prefix + base_string.img.get('src')
			temp_card = (name, year, img_link)
			#link = link_prefix + base_string.get('href')
			finalCardList.append(temp_card)
			print('---- В этом месте в ГУИ сделать прогресс бар ----')

	return finalCardList

def main():
	finalCardList = parsing(2022)
	print(type(finalCardList), finalCardList)
	for card in finalCardList:
		print(type(card), card)
	print('Names is parsed!')

if __name__ == "__main__":
	# Test
	main()