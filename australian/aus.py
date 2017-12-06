from bs4 import BeautifulSoup as BS
from requests import Session
import csv
import os
import re
class SC:
	def scrap(self):
		#os.chdir('/sdcard/YoloShare')
		f=open('links.txt','r').read()
		f=f.split('\n')
		#xl=open('t.csv','wt',newline='', encoding="utf-8")
		#row=csv.writer(xl)
		wr=open('product_links.txt','wt')
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"http://www.australiancosmetics.com.au"})

		for i in f:
			print('before')
			r=s.post(i)
			print('after')
			regex='<a class="main-link" href="(.*?)">'
			link=re.findall(regex,r.text)
			for l in link:
				wr.write(i+' : '+l+'\n')
			print(i)	
			r=s.post(i+'page/2/')
			num=2
			while(r.status_code==200):
				regex='<a class="main-link" href="(.*?)">'
				link=re.findall(regex,r.text)
				for l in link:
					wr.write(i+' : '+l+'\n')
				print(r.url)	
				num+=1;
				p='page/'+str(num)+'/'
				r=s.get(i+p)			

obj=SC();
obj.scrap();