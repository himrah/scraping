import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

def abc():
#last_height = driver.execute_script('return document.body.scrollHeight')
#SPT=.5
	w=open('result.txt','w')
	f=open('links.txt','r').read().split('\n')
	#driver=webdriver.Chrome(executable_path='/home/himah/Download/ch/chromedriver')
	driver=webdriver.Chrome(executable_path='/home/himrah/Downloads/ch/chromedriver')
	for i in f:
	     driver.get(i)
	     soup=BS(driver.page_source,'html.parser')
	     body=soup.find('div','_55wo _55wp _55x2 _56bf')
	     if body:
	     	t=body.find_all('a','touchable')
	     	for j in t:
	     		w.write(i+'\\'+j.get('href')+'\n')
	     	T=True
	     	print(i)
	     	page_number=2
	     	while T:
	     		nxt=i+'?page='+str(page_number)
	     		driver.get(nxt)
	     		soup=BS(driver.page_source,'html.parser')
	     		body=soup.find('div','_55wo _55wp _55x2 _56bf')
	     		if body:
	     			t=body.find_all('a','touchable')
	     			for j in t:
	     				w.write(nxt+'\\'+j.get('href')+'\n')
	     			page_number+=1
	     			T=True
	     		else:
	     			T=False
	     		print(nxt)	

abc()					
