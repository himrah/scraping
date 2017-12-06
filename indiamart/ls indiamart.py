from selenium import webdriver
import codecs
from requests import Session
from bs4 import BeautifulSoup as BS
import sys
import time
import csv

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
		head=['Title','Name','Description','Phone','City','Full Address','URL','Page url']
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		row.writerow(head)
		#data={'mcatName':'Warehouse Management System','mcatId':40905,'searchCity':0,'end':56,'rand':3,'prod_serv':'S','showkm':0,'debug_mod':0,'biz':0,'price':0,'cntAll':77,'odd':'odd'}
		#driver = webdriver.Firefox(executable_path='C:/Users/Rahul Kumar/Downloads/geckodriver.exe')
		#c=['shimoga', 'vadodara', 'tiruvannamalai', 'thoothukudi']
		#c=['hingoli', 'hisar', 'hissar', 'hooghly', 'hoshangabad', 'hoshiarpur', 'hospet', 'hosur', 'howrah', 'hubli', 'hyderabad', 'ichalkaranji''idukki', 'imphal', 'indore', 'jabalpur', 'jafrabad', 'jaipur', 'jaisalmer', 'jaithra', 'jajpur', 'jalandhar', 'jalgaon', 'jalna', 'jalor', 'jalpaiguri','jamalpur', 'jammu', 'jammu-city', 'jamnagar', 'jamshedpur', 'jaunpur', 'jhajjar', 'jhansi', 'jharsuguda', 'jhunjhunu', 'jind', 'jintur', 'jodhpur','silvassa', 'sindhudurg', 'sirohi', 'sirsa', 'sitamarhi', 'sivaganga', 'sivasagar', 'siwan', 'solan', 'solapur', 'sonipat', 'sonitpur', 'south-24-parganas','kozhikode', 'krishna-nagar', 'krishnagiri', 'kullu', 'kumbakonam', 'kumta', 'kundaim', 'kurnool', 'kurukshetra', 'kutch', 'ladakh', 'laharpur', 'lakhimpur-kheri', 'lakshadweep', 'latur', 'lucknow', 'ludhiana', 'machilipatnam', 'madikeri', 'madurai', 'mahabaleshwar', 'mahabubnagar', 'mahesana', 'malappuram', 'malda', 'malegaon', 'malout', 'manali', 'manawar', 'mandi', 'mandi-dabwali', 'mandi-gobindgarh', 'mandla', 'mandsaur', 'mandya', 'mangalore', 'manipal','hingoli', 'hisar', 'hissar', 'hooghly', 'hoshangabad', 'hoshiarpur', 'hospet', 'hosur', 'howrah', 'hubli', 'hyderabad', 'ichalkaranji''idukki', 'imphal', 'indore', 'jabalpur', 'jafrabad', 'jaipur', 'jaisalmer', 'jaithra', 'jajpur', 'jalandhar', 'jalgaon', 'jalna', 'jalor', 'jalpaiguri','jamalpur', 'jammu', 'jammu-city', 'jamnagar', 'jamshedpur', 'jaunpur', 'jhajjar', 'jhansi', 'jharsuguda', 'jhunjhunu', 'jind', 'jintur', 'jodhpur','silvassa', 'sindhudurg', 'sirohi', 'sirsa', 'sitamarhi', 'sivaganga', 'sivasagar', 'siwan', 'solan', 'solapur', 'sonipat', 'sonitpur', 'south-24-parganas','kozhikode', 'krishna-nagar', 'krishnagiri', 'kullu', 'kumbakonam', 'kumta', 'kundaim', 'kurnool', 'kurukshetra', 'kutch', 'ladakh', 'laharpur', 'lakhimpur-kheri', 'lakshadweep', 'latur', 'lucknow', 'ludhiana', 'machilipatnam', 'madikeri', 'madurai', 'mahabaleshwar', 'mahabubnagar', 'mahesana', 'malappuram', 'malda', 'malegaon', 'malout', 'manali', 'manawar', 'mandi', 'mandi-dabwali', 'mandi-gobindgarh', 'mandla', 'mandsaur', 'mandya', 'mangalore', 'manipal']
		#d=['midnapore', 'mirzapur', 'moga', 'mohali', 'moradabad', 'morena', 'mormugoa','deoria', 'dera-bassi', 'dewas', 'dhanbad', 'dhar-city', 'dharmapuri', 'dharwad', 'dhenkanal','cooch-behar', 'coorg', 'cortalim', 'cuddalore', 'cuttack', 'dadra', 'dahanu', 'daman', 'darbhanga', 'darjeeling','bhadrak', 'bhadurgarh', 'bhagalpur', 'bhandara', 'bharatpur', 'bharuch', 'bhavnagar', 'bhilai', 'bhilwara','bikaner', 'bilaspur', 'bilimora', 'birbhum', 'bokaro-steel-city', 'bolangir', 'borsad', 'botad', 'bulandshahr','baramati', 'baran', 'bardez', 'bardhaman', 'bareilly', 'bargarh', 'barmer', 'barnala', 'basti', 'batala', 'bathinda','amreli', 'amritsar', 'amroha', 'anand', 'anantapur', 'anantnag', 'angamaly', 'ariyalur', 'arrah', 'asansol','rayagada', 'rewa', 'rewari', 'rohtak', 'rohtas', 'roorkee', 'ropar', 'rourkela', 'rudrapur', 'rupnagar', 'sabarkantha', 'sagar', 'saharanpur', 'salem','himmatnagar', 'kochi','south-sikkim', 'sriganganagar', 'srikakulam', 'srikalahasti', 'srinagar', 'sujanpur', 'surat', 'surendranagar', 'surguja', 'suryapet', 'tiruvarur', 'tiswadi', 'tohana', 'tonk', ]
		#c =['Delhi','Gurgaon','Navi Mumbai','Thane','berhampur', 'bettiah', 'betul','bhadrak', 'bhadurgarh', 'bhagalpur', 'bhandara', 'bharatpur', 'bharuch', 'bhavnagar', 'bhilai', 'bhilwara','bhimavaram', 'bhind', 'bhiwadi', 'bhiwani', 'bhopal', 'bhubaneshwar', 'bhuj', 'bidar', 'bijapur', 'bijnor','bikaner', 'bilaspur', 'bilimora', 'birbhum', 'bokaro-steel-city', 'bolangir', 'botad', 'bulandshahr']
		#ct=0

		"""for ct in c:
			u='https://dir.indiamart.com/search.mp?ss=3rd+party+logistics+provider&cq='+str(ct)
			driver.get(u)
			#r=s.get(u)
			#string =str(r.content)
			string=str(driver.page_source)
			st=string.replace('\\','').replace('tt','')
			soup=BS(st,'html.parser')
			temp=soup.find_all('div','lst')
			print(ct)
			for i in temp:
				#km=[]
				k=[]
				if(i.find('a')):
					k.append(i.find('a').text)
				else:
					k.append('Not Given')
				if(i.find('a','lcname')):	
					k.append(i.find('a','lcname').text)
				else:
					k.append('Not Given')
				if(i.find('p','desc')):	
					k.append(i.find('p','desc').text)
				else:
					k.append('Not Given')
				if(i.find('span','ls_co phn')):
					k.append(i.find('span','ls_co phn').text)
				else:	
					k.append('Not Given')
				if(i.find('span','clg')):
					k.append(i.find('span','clg').next)
				else:
					k.append('Not Given')
				if(i.find('span','srad cty-t')):
					k.append(i.find('span','srad cty-t').text)
				else:
					k.append('Not Given')
				#k.append(i.find('a','lcname').get('href'))
				if(i.find('a').get('href')):
					k.append(i.find('a').get('href'))
				else:
					k.append('Not Given')
				k.append(u)
				#km.append(k)
				row.writerow(k)"""
		#nnn=216
		nnn=56
		for num in range(1,500):
			url='https://dir.indiamart.com/impcatProductPagination.php'
		    #U='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=borsad&pg=2&c=IN&scroll=1&pr=0&frsc=20'
			#url='https://dir.indiamart.com/search.mp/next?ss=3rd+party+logistics+provider&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
			#url='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=kolkata&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
			#url='https://dir.indiamart.com/search.mp?ss=warehouse&cq='+str(ct)
			#url='https://dir.indiamart.com/search.mp/next?ss=logistic+provider&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
			#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg='+str(num)+'&c=IN&scroll='+str(num)+'&pr=0&frsc='+str(num)
			#data={'mcatName':'Goods Warehousing Service','mcatId':104870,'catId':344,'searchCity':0,'end':str(nnn),'rand':1,'prod_serv':'S','showkm':0,'debug_mod':0,'biz':0,'price':0,'cntAll':str(nnn),'odd':'undefined'}
			#data={'mcatName':'Warehousing Services','mcatId':42702,'searchCity':0,'end':str(nnn),'rand':5,'prod_serv':'S','showkm':0,'debug_mod':0,'biz':0,'price':0,'cntAll':str(nnn+20),'odd':'odd'}
			#data={'mcatName':'Warehousing Services','mcatId':42702,'catId':344,'searchCity':0,'end':str(nnn),'rand':3,'prod_serv':'S','showkm':0,'debug_mod':0,'biz':0,'price':0,'cntAll':str(nnn-20),'odd':'odd'}
			#response = webdriver.request('POST', url,data)
            data={'mcatName':'Logistics Service','mcatId':69544,'catId':352,'searchCity':0,'end':str(nnn),'rand':1,'prod_serv':'S','showkm':0,'debug_mod':0,'biz':0,'price':0,'cntAll':str(nnn),'odd':'undefined'}
			r=s.post(url,data)
			#driver.close()
			#driver = webdriver.Firefox(executable_path='C:/Users/Rahul Kumar/Downloads/geckodriver.exe')
			#driver.get(url)
			string=str(r.content)

			#string=str(driver.page_source)
			#st=string.replace('\\','').replace('tt','')
			soup=BS(string,'html.parser')
			temp=soup.find_all('div','lst')
			km=[]
			print('writing : ',num)
			#print('writi : ',temp)
			for i in temp:
				#km=[]
				k=[]
				if(i.find('a')):
					k.append(i.find('a').text)
				else:
					k.append('Not Given')	
				if(i.find('a','lcname')):
					k.append(i.find('a','lcname').text)
				else:
					k.append('Not Given')
				if(i.find('p','desc')):	
					k.append(i.find('p','desc').text)
				else:
					k.append('Not Given')
				if(i.find('span','ls_co phn')):
					k.append(i.find('span','ls_co phn').text)
				else:
					k.append('Not Given')
				if(i.find('span','clg')):	
					k.append(i.find('span','clg').next)
				else:
					k.append('Not Given')
				if(i.find('span','srad cty-t')):
					k.append(i.find('span','srad cty-t').text)
				else:
					k.append('Not Given')
				#k.append(i.find('a','lcname').get('href'))
				if(i.find('a').get('href')):
					k.append(i.find('a').get('href'))
				else:
					k.append('Not Given')	
				k.append(url)
				#print(k)
				#km.append(k)
				row.writerow(k)
			#time.sleep(5)	
			nnn=nnn+20	
			
			#ct=ct+1	"""

		print(nnn)	
"""	def writing(self,links):
		xl=open('t.csv','wt',newline='')
		self.parser(links)

		print('writing header in rows')
		row=csv.writer(xl)
		head=['Path','Title','Specification','Description','Price','Total Price','Wholesale price','Seller Name','Address','Image Link','URL']
		#[title,image,path,price,wholesale,seller,specs,des]
		row.writerow(head)
		val=[]		"""	

obj=SC()
obj.scrap()			

#['Hyderabad','Ahmedabad','Surat','Jaipur','Lucknow','Kanpur','Visakhapatnam','Indore','Bhopal','Patna','Vadodara','Ghaziabad','Ludhiana','Agra','Madurai']

#https://dir.indiamart.com/search.mp?ss=warehousing+services&source=autosuggest
#https://dir.indiamart.com/search.mp/next?ss=warehousing+services&pg=2&c=IN&scroll=1&pr=0&frsc=21


#https://dir.indiamart.com/search.mp?ss=warehousing+services&cq=delhi
#https://dir.indiamart.com/search.mp/next?ss=warehousing+services&cq=delhi&pg=2&c=IN&scroll=1&pr=0&frsc=21&_=1498178287493

#https://dir.indiamart.com/impcatProductPagination.php?mcatName=Warehouse Management System&mcatId=40905&searchCity=&end=56&rand=3prod_serv=S&showkm=0&debug_mod=0&biz=&price=0&cntAll=77&odd=odd
