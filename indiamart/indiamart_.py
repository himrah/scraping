from requests import Session
from bs4 import BeautifulSoup as BS
import time
import csv

class SC:
	def scrap(self):
		#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg=20&c=IN&scroll=1&pr=0&frsc=22'
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		head=['Title','Name','Description','Phone','City','Full Address','URL','Page url']
		xl=open('t.csv','wt',newline='')
		row=csv.writer(xl)
		row.writerow(head)
		c=['egmore','anderi east','ludiyana']
		#donec=['Kanchipuram','kolar','mandi','Chennai','Muzaffarpur','Muzaffarnagar','vellore','Tiruvannamalai','navi mumbai', 'mumbai', 'delhi', 'thane','vadodara', 'pune', 'Ahmedabad', 'Faridabad','Noida','Gurgaon','Jaipur','Haridwar','bengaluru','kanpur']

		#c =['Navi Mumbai','Thane''berhampur', 'bettiah', 'betul','bhadrak', 'bhadurgarh', 'bhagalpur', 'bhandara', 'bharatpur', 'bharuch', 'bhavnagar', 'bhilai', 'bhilwara','bhimavaram', 'bhind', 'bhiwadi', 'bhiwani', 'bhopal', 'bhubaneshwar', 'bhuj', 'bidar', 'bijapur', 'bijnor','bikaner', 'bilaspur', 'bilimora', 'birbhum', 'bokaro-steel-city', 'bolangir', 'botad', 'bulandshahr']
		#ct=0

		for ct in c:
			u='https://dir.indiamart.com/search.mp?ss=warehousing+services&cq='+str(ct)
			r=s.get(u)
			string=str(r.content)
			st=string.replace('\\','').replace('tt','')
			soup=BS(st,'html.parser')
			temp=soup.find_all('div','lst')
			for i in temp:
				#km=[]
				k=[]
				k.append(i.find('a').text)
				k.append(i.find('a','lcname').text)
				k.append(i.find('p','desc').text)
				rs=i.find('span','ls_co phn').text
				if rs:
					k.append(rs)
				else:
					k.append('Not given')	
				k.append(i.find('span','clg').next)
				k.append(i.find('span','srad cty-t').text)
				#k.append(i.find('a','lcname').get('href'))
				k.append(i.find('a').get('href'))
				k.append(u)
				#km.append(k)
				row.writerow(k)

			for num in range(2,11):

			    #U='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=borsad&pg=2&c=IN&scroll=1&pr=0&frsc=20'
				url='https://dir.indiamart.com/search.mp/next?ss=warehousing+services&cq='+ct+'&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=kolkata&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp?ss=warehouse&cq='+str(ct)
				#url='https://dir.indiamart.com/search.mp/next?ss=logistic+provider&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg='+str(num)+'&c=IN&scroll='+str(num)+'&pr=0&frsc='+str(num)
				r=s.get(url)
				string=str(r.content)
				st=string.replace('\\','').replace('tt','')
				soup=BS(st,'html.parser')
				temp=soup.find_all('div','lst')
				km=[]
				print('writing : ',num)
				for i in temp:
					#km=[]
					k=[]
					k.append(i.find('a').text)
					k.append(i.find('a','lcname').text)
					k.append(i.find('p','desc').text)
					rs = i.find('span','ls_co phn').text
					if rs:
						k.append(rs)
					else:
						k.append('Not Given')
					k.append(i.find('span','clg').next)
					k.append(i.find('span','srad cty-t').text)
					#k.append(i.find('a','lcname').get('href'))
					k.append(i.find('a').get('href'))
					k.append(url)
					#km.append(k)
					row.writerow(k)
				#time.sleep(5)		
				
				#ct=ct+1	


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
