from bs4 import BeautifulSoup as BS
from requests import Session
import csv
import os
import re
class SC:
	def scrap(self):
		#osdfk
		f=open('direct.txt').read()
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})

		for i in f[6388:]:
			r=s.get('http://'+i)
			soup=BS(r.content,'html.parser')
			content=soup.find_all('div',attrs={'id':'g_st_container'})
			if(content):
			 for j in content:
			     #temp=re.search('(a-zA-Z0-9_|\w+).@(\w+).(\w+)',str(j))
			     if(temp):
			         temp=temp.group(0)
			         row.writerow([temp,i])
			         print(temp)
			         num+=1
			#num+=1d
			print(i+' : '+str(num))
			num+=1
	#email re.search('(a-zA-Z0-9_|\w+).@(\S+)',str(j)).group(0
