                                                    
from bs4 import BeautifulSoup
driver=webdriver.PhantomJS(r'Z:\manas1\phantomjs.exe')
url = 'https://in.global.nba.com/playerindex/?_ga=2.71736659.1354572313.1551276365-121493775.1548256063'
driver.get(url)
print (driver.page_source)