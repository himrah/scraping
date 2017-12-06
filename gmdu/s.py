
"""https://search.gmdu.net/iokiohoi/Beauty%20Products.html 2
https://search.gmdu.net/iokiohoh/Beauty%20Products.html 1
k
m
n
p
q
r
s
t
u
v
w
x
y
z
l=['h','i','k','m','n','p','q','r','s','t','u','v','w','x','y','z','ih']

iokiohoh
iokiohoih


Business type : re.search(r'Business Type</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
main market : re.search(r'Main Markets</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
product_service : re.search(r'Product/Service</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
Employees : re.search(r'Employees</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
region : re.search(r'Region</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
Category : re.search(r'Category</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
Link Tool : re.search(r'Link Tool</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)
Company Tags : re.search(r'Company Tags</span><span class="general-value">(.*?)</span></div>',str(r.content)).group(1)

contact_person : re.search(r'Contact Person</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)
Telephone : re.search(r'Telephone</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)
Fax Number : re.search(r'Fax Number</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)

Website : re.search(r'Website</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)
Post Code : re.search(r'Post Code</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)
Address : re.search(r'Address</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)
Online Map : re.search(r'Online Map</span><span class="contact-value"(.*?)</span></div>',str(r.content)).group(1)

title : re.search(r'<h1 itemprop="name">(.*?)</h1>',str(r.content)).group(1)

path = soup.find('div','position').text.replace('\n','').strip()"""

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
		head=['Title','Path','Business Type','Main Market','Product/Service','Employees','Region','Category','Link Tool','Company Tag','Contact Person','Telphone','Fax Number','Website','Post Code','Address','Online Map','URL']
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		f=open('link.txt').read()		
		li=f.split('\n')
		num=1
		for i in li:
			k=[]
			r=s.get(i)
			content=str(r.content)
			soup=BS(r.content,'html.parser')
			
			#title=re.search(r'style="padding: 0px;">(.*?)</h4>',str(r.content))
			title = re.search(r'<h1 itemprop="name">(.*?)</h1>',str(r.content))
			if(title):
				k.append(title.group(1))
				#k.append(str(title.group(1)).replace('\\n','').replace('<h4>','').strip())
			else:
				k.append("Not Given")

			path = soup.find('div','position')	
			if path:
				k.append(path.text.replace('\n','').strip())
			else:
				k.append("Not Given")



			business_type = re.search(r'Business Type</span><span class="general-value">(.*?)</span></div>',content)
			if business_type:
				k.append(business_type.group(1).strip())
			else:
				k.append("Not Given")

			main_market = re.search(r'Main Markets</span><span class="general-value">(.*?)</span></div>',content)
			if main_market:
				k.append(main_market.group(1).strip())
			else:
				k.append("Not Given")	
							

			product_service = re.search(r'Product/Service</span><span class="general-value">(.*?)</span></div>',content)
			if product_service:
				k.append(product_service.group(1).strip())
			else:
				k.append("Not Given")	

			employees = re.search(r'Employees</span><span class="general-value">(.*?)</span></div>',content)
			if employees:
				k.append(employees.group(1).strip())
			else:
				k.append("Not Given")	


			region = re.search(r'Region</span><span class="general-value">(.*?)</span></div>',content)
			if region:
				k.append(region.group(1).strip())
			else:
				k.append("Not Given")	



			category = re.search(r'Category</span><span class="general-value">(.*?)</span></div>',content)
			if category:
				k.append(category.group(1).strip())
			else:
				k.append("Not Given")	


			link_tool = re.search(r'Link Tool</span><span class="general-value">(.*?)</span></div>',content)
			if link_tool:
				k.append(link_tool.group(1).strip())
			else:
				k.append("Not Given")	


			company_tag = re.search(r'Company Tags</span><span class="general-value">(.*?)</span></div>',content)
			if company_tag:
				k.append(company_tag.group(1).strip())
			else:
				k.append("Not Given")	

			contact_person = re.search(r'Contact Person</span><span class="contact-value"(.*?)</span></div>',content)	
			if contact_person:
				k.append(contact_person.group(1).strip())
			else:
				k.append("Not Given")

			telephone = re.search(r'Telephone</span><span class="contact-value"(.*?)</span></div>',content)	
			if telephone:
				k.append(telephone.group(1).strip())
			else:
				k.append("Not Given")

			fax_number = re.search(r'Fax Number</span><span class="contact-value"(.*?)</span></div>',content)	
			if fax_number:
				k.append(fax_number.group(1).strip())
			else:
				k.append("Not Given")

			website = re.search(r'Website</span><span class="contact-value"(.*?)</span></div>',content)	
			if website:
				k.append(website.group(1).strip())
			else:
				k.append("Not Given")

			post_code = re.search(r'Post Code</span><span class="contact-value"(.*?)</span></div>',content)	
			if post_code:
				k.append(post_code.group(1).strip())
			else:
				k.append("Not Given")

			address = re.search(r'Address</span><span class="contact-value"(.*?)</span></div>',content)	
			if address:
				k.append(address.group(1).strip())
			else:
				k.append("Not Given")

			online_map = re.search(r'Online Map</span><span class="contact-value"(.*?)</span></div>',content)	
			if online_map:
				k.append(online_map.group(1).strip())
			else:
				k.append("Not Given")


			k.append(i)
			row.writerow(k)
			print(i+' '+str(num))
			num+=1



"""

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

			k.append(i)	"""


			#dt = soup.find('div','detailProduk productDetailPage')
			#if dt:
			#	k.append(dt.text.strip())		
			#else:
			#	k.append("Not Given")


obj=SC()
obj.scrap()