from requests import Session
from bs4 import BeautifulSoup as BS
import csv
#import sys
#import codecs
class SC:
	def scrap(self):
		#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg=20&c=IN&scroll=1&pr=0&frsc=22'
#if sys.stdout.encoding != 'cp850':
#	 sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
#if sys.stderr.encoding != 'cp850':
#	sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')	 
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		head=['Name','URL','Address','Phone','Fax']
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		#f=open('link.txt').read()		
		
		#li=f.split('\n')
		u='http://www.yellowpages.my/listing/guide/logistics/page/'
		for i in range(1,2):
			url=u+str(i)
			r=s.get(url)
			soup=BS(r.content,'html.parser')
			upper = soup.find_all(attrs={'style':'border: solid 1px #E1E1E1'})
			lower = soup.find_all('div','cbp-vm-cta')
			z = zip(upper,lower)
			for upper,lower in z:
				k=[]

				title = upper.find('div','cbp-vm-companytext')
				#title = upper.find('div','cbp-vm-company')
				if(title):
					k.append(title.text.strip())
				elif upper.find('div','cbp-vm-company'):
					k.append(upper.find('div','cbp-vm-company').text.strip())
				else:('Not Given')

				url = upper.find('div','cbp-vm-company').find('a')	
				if url:
					k.append(url.get('href'))
				else:
					k.append("Not Given")

				add = upper.find('div','cbp-vm-address')
				if add:
					k.append(str(add.next.next.next.next).strip())	
				else:
					k.append("Not Given")

				ph = lower.find(attrs={'data-original-title':'Phone'})
				if ph:
					k.append(ph.get('data-content'))
				else:
					k.append("Not Given")

				fx = lower.find(attrs={'data-original-title':'Phone'})
				if fx:
					k.append(fx.get('data-content'))		
				else:
					k.append("Not Given")

				row.writerow(k)
			print(i)	

obj=SC()
obj.scrap()

""" 
 pr=soup.find_all(attrs={'style':'border: solid 1px #E1E1E1'})
name = pr[0].find('div','cbp-vm-company').text
 url = pr[0].find('div','cbp-vm-company').find('a').get('href')
 address = pr[0].find('div','cbp-vm-address').next.next.next.next

 ph=soup.find_all(attrs={'data-original-title':'Phone'})
 ph[0].get('data-content')

 n=soup.find_all('div','cbp-vm-cta')
 phone = n[0].find(attrs={'data-original-title':'Phone'}).get('data-content')
 fax = n[0].find(attrs={'data-original-title':'Fax'}).get('data-content')"""