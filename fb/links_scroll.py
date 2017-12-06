
import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

def():
last_height = driver.execute_script('return document.body.scrollHeight')
SPT=.5
driver=webdriver.Chrome()
	for i in f:
	     driver.get(i)
	     while True:
	         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	         time.sleep(SPT)
	         new_height = driver.execute_script("return document.body.scrollHeight")
	         if new_height == last_height:
	             break
	         last_height = new_height
	     #l.append()
	     soup=BS(driver.page_source,'html.parser') 
	     t=soup.find_all('a','touchable primary')
	     for j in t:
	         ll.append(j.get('href')+' : '+i)
	     print(i+str(num))
	     num=num+1