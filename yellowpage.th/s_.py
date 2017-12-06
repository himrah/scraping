#translate : import goslate
# gs=goslate.Goslate() gs.translate(l[0].text,'en')

#address = str(re.search(r'Address:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').strip()	 
#add = str(re.search(r'Address:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').strip()
#tel = str(re.search(r'Tel:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip()
#email = str(re.search(r'Email:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip()
#website = str(re.search(r'Website:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip()
#Fax = str(re.search(r'Fax:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip()
#Worktime = str(re.search(r'Work-Time:(.*?)</tr>',str(r.content)).group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip()
#title = str(re.search(r'style="padding: 0px;">(.*?)</h4>',str(r.content)).group(1)).replace('\\n','').replace('<h4>','').strip()
#category = str(re.search(r'Category :(.*?)</a>',str(r.content)).group(1)).replace('\\n','').replace('<h4>','').strip()
#path = soup.find('div','breadcrumbs').text.replace('\n','')

from requests import Session
from bs4 import BeautifulSoup as BS
import csv
import re
import sys
import codecs
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
		head=['Title','Path','address','Tel','Fax','Email','work','website','Category','Email','Url']
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		f=open('link.txt').read()		
		li=f.split('\n')
		num=1
		for i in li:
			k=[]
			r=s.get(i)
			soup=BS(r.content,'html.parser')
			
			#title=re.search(r'style="padding: 0px;">(.*?)</h4>',str(r.content))
			title=soup.find('div','col-xs-12 col-md-12 col-lg-12')
			if(title):
				k.append(title.find('h4').text)
				#k.append(str(title.group(1)).replace('\\n','').replace('<h4>','').strip())
			else:
				k.append("Not Given")

			path = soup.find('div','breadcrumbs')		
			if path:
				k.append(path.text.replace('\n','').strip())
			else:
				k.append("Not Given")

			add = re.search(r'Address:(.*?)</tr>',str(r.content))
			if add:
				k.append(str(add.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').strip())	
			else:
				k.append("Not Given")

			tel = re.search(r'Tel:(.*?)</tr>',str(r.content))
			if tel:
				k.append(str(tel.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip())	
			else:
				k.append("Not Given")


			fax = re.search(r'Fax:(.*?)</tr>',str(r.content))
			if fax:
				k.append(str(fax.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip())	
			else:
				k.append("Not Given")


			email = re.search(r'Email:(.*?)</tr>',str(r.content))
			if email:
				k.append(str(email.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip())	
			else:
				k.append("Not Given")



			work = re.search(r'Work-Time:(.*?)</tr>',str(r.content))
			if work:
				k.append(str(work.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip())	
			else:
				k.append("Not Given")


			website = re.search(r'Website:(.*?)</tr>',str(r.content))
			if website:
				k.append(str(website.group(1)).replace('\\n','').replace('</b></td>','').replace('</td>','').replace('<td class="table-right">','').replace('<br>','').strip())	
			else:
				k.append("Not Given")



			category = re.search(r'Category :(.*?)</a>',str(r.content))
			if category:
				k.append(str(category.group(1)).replace('\\n','').replace('<h4>','').strip())
			else:
				k.append('Not Given')	

			k.append(i)	


			#dt = soup.find('div','detailProduk productDetailPage')
			#if dt:
			#	k.append(dt.text.strip())		
			#else:
			#	k.append("Not Given")

			k.append(i)
			row.writerow(k)
			print(i+' '+str(num))
			num+=1

obj=SC()
obj.scrap()