# nba-stat-table__overlay

from selenium import webdriver
from bs4 import BeautifulSoup

# create class
class Player():
	"""docstring for player"""
	def __init__(self):
		self.name = ""
		self.link = ""

def get_player_list():
				

			
  # create driver
  driver = webdriver.PhantomJS(r'Z:\manas1\phantomjs.exe')
  url = 'https://in.global.nba.com/playerindex/?_ga=2.110418629.1354572313.1551276365-121493775.1548256063'

  # download html page
  driver.get(url)

  # create soup
  soup = BeautifulSoup(driver.page_source,'lxml')

  div = soup.find('div', class_ = 'nba-stat-table__overlay')

  player_list = []
  for a in div.find_all('a'):
      # print (a.text)
      # print('href=' + a.get('href'))
      new_play = Player()
      new_play.name = a.text
      new_play.link = a['href']
      player_list.append(new_play)

  for one_player in player_list:
	  print(one_player.name)
	  print(one_player.link)



  driver.quit()

  return player_list

get_player_list()  