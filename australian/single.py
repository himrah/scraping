"""title: re.search('<h1>(.*?)</h1>',r.text).group(1),  
addrs : re.search('<div class="address-data" itemprop="streetAddress"><p>(.*?)</p>',r.text).group(1),  soup.find('div','address-data').text
gps : soup.find('div',attrs={'itemprop':'geo'}).text.replace('\t','').replace('\n','')

phone : 	for i in soup.find_all('a','phone'):
				i.text
email : soup.find('a',itemprop={'email'}).text

url : soup.find('a',itemprop={'url'}).text"""


from requests import Session
from bs4 import BeautifulSoup as BS
import csv
import sys
import re
#import codecs
class SC:
	def scrap(self):
		#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg=20&c=IN&scroll=1&pr=0&frsc=22'
		"""if sys.stdout.encoding != 'cp850':
			 sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
		if sys.stderr.encoding != 'cp850':
			sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')	 """
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"http://www.australiancosmetics.com.au/"})
		head=['Title','email','address','Phone','gps','s_URL','Main_URL']
		xl=open('rss.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		f=open('prd.txt').read()		
		li=f.split('\n')
		for i in li:
			k=[]
			r=s.post(i)
			soup=BS(r.content,'html.parser')
			
			title=re.search('<h1>(.*?)</h1>',r.text)
			if(title):
				k.append(title.group(1))
			else:
				k.append("Not Given")		

			email = soup.find('a',itemprop={'email'})			
			if email:
				k.append(email.text.strip())
			else:
				k.append("Not Given")

			add = soup.find('div','address-data')
			if add:
				k.append(add.text.strip())	
			else:
				k.append("Not Given")

			ph = soup.find_all('a','phone')
			if ph:
				p=''
				for j in ph:
					p+=str(j.text)
				k.append(p)
			else:
				k.append("Not Given")


			gps = soup.find('div',attrs={'itemprop':'geo'})
			if gps:
				k.append(gps.text.replace('\t','').replace('\n','').strip())		
			else:
				k.append("Not Given")

			s_url = soup.find('a',itemprop={'url'})
			if(s_url):
				k.append(s_url.text.strip())
			else:
				k.append('Not Given')	

			k.append(i)
			row.writerow(k)
			print(i)	

obj=SC()
obj.scrap()