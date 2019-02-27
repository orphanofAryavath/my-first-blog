
from selenium import webdriver
from bs4 import BeautifulSoup
driver=Webdriver.PhantomJS(r'Z:\manas1\phantomjs.exe')
driver.get('https://python.org')
print (driver.page_source)
