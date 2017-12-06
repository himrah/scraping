from requests import Session
from bs4 import BeautifulSoup as BS
import csv
import sys
import codecs
class SC:
	def scrap(self):
		#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg=20&c=IN&scroll=1&pr=0&frsc=22'
		if sys.stdout.encoding != 'cp850':
			 sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
		if sys.stderr.encoding != 'cp850':
			sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')	 
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		head=['Title','Path','address','Phone','Description','URL']
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		f=open('link.txt').read()		
		li=f.split('\n')
		for i in li:
			k=[]
			r=s.get(i)
			soup=BS(r.content,'html.parser')
			
			title=soup.find('h2','judulProduk-detail')
			if(title):
				k.append(title.text)
			else:
				k.append("Not Given")		

			path = soup.find('div','divBreadcum')			
			if path:
				k.append(path.text.strip())
			else:
				k.append("Not Given")

			add = soup.find('div','productInfo')
			if add:
				k.append(add.find('p').text.strip())	
			else:
				k.append("Not Given")

			ph = soup.find('p','kontakPar')
			if ph:
				k.append(ph.text.strip())	
			else:
				k.append("Not Given")

			dt = soup.find('div','detailProduk productDetailPage')
			if dt:
				k.append(dt.text.strip())		
			else:
				k.append("Not Given")

			k.append(i)
			row.writerow(k)
			print(i)	

obj=SC()
obj.scrap()



"""al=soup.find('div','blog-area fix')
al.find_all('article')[3].find('a').get('href')

list=[]

url='https://yellowpages.co.id/cari/bisnis/distributor?page='+str(i)
driver.get(url)
soup=BS(driver.page_source,'html.parser')
al=soup.find('div','blog-area fix')
t=al.find_all('article')
for i in t:
i.find('a').get('href')



PAge

url
search term
title==soup.find('h2','judulProduk-detail').text
path=====soup.find('div','divBreadcum').text
address=====soup.find('div','productInfo').find('p').text.strip()
phone==========soup.find('p','kontakPar').text.strip()
details=========soup.find('div','detailProduk productDetailPage').text.strip()"""



""" driver = webdriver.Firefox(executable_path='C:/Users/Rahul Kumar/Downloads/geckodriver.exe')

>>> for i in range(1,18):
...     url='https://yellowpages.co.id/cari/bisnis/warehouse?page='+str(i)
...     driver.get(url)
...     soup=BS(driver.page_source,'html.parser')
...     al=soup.find('div','blog-area fix')
...     t=al.find_all('article')
...     for j in t:
...         f.write(j.find('a').get('href')+'\n')
...     print(url)



"""