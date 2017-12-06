from selenium import webdriver
from requests import Session
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup as BS
import time
import csv

class SC:
	def scrap(self):
		#display=Display(visible=0, size=(800,600))
		#display.start()
		#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg=20&c=IN&scroll=1&pr=0&frsc=22'
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		head=['Title','Name','Description','Phone','City','Full Address','URL','Page url']
		xl=open('t.csv','wt',newline='')
		row=csv.writer(xl)
		row.writerow(head)
		#driver = webdriver.Firefox(executable_path='C:/Users/Rahul Kumar/Downloads/geckodriver.exe')
		#c=['solapur','sonipat','','raipur', 'raisen', 'rajahmundry']
		c=['navi mumbai', 'mumbai', 'delhi', 'thane','vadodara', 'pune', 'Ahmedabad', 'Faridabad','Noida','Gurgaon','Jaipur','Haridwar','bengaluru','kanpur']
		#donec=['Kanchipuram','kolar','mandi','Chennai','Muzaffarpur','Muzaffarnagar','vellore','Tiruvannamalai','navi mumbai', 'mumbai', 'delhi', 'thane','vadodara', 'pune', 'Ahmedabad', 'Faridabad','Noida','Gurgaon','Jaipur','Haridwar','bengaluru','kanpur']

		#c =['Navi Mumbai','Thane''berhampur', 'bettiah', 'betul','bhadrak', 'bhadurgarh', 'bhagalpur', 'bhandara', 'bharatpur', 'bharuch', 'bhavnagar', 'bhilai', 'bhilwara','bhimavaram', 'bhind', 'bhiwadi', 'bhiwani', 'bhopal', 'bhubaneshwar', 'bhuj', 'bidar', 'bijapur', 'bijnor','bikaner', 'bilaspur', 'bilimora', 'birbhum', 'bokaro-steel-city', 'bolangir', 'botad', 'bulandshahr']
		#ct=0
		for ct in c:
			"""u='https://dir.indiamart.com/search.mp?ss=warehousing+services&cq='+str(ct)
												driver.get(u)
												r=driver.page_source
												#r=s.get(u)			
												string=str(r)
												st=string.replace('\\','').replace('tt','')
												soup=BS(st,'html.parser')
												temp=soup.find_all('div','lst')
												for i in temp:
													#km=[]
													k=[]
													t=i.find('a')
													if t:
														k.append(i.find('a').text)
													else:
														k.append('Not Given')
													if(i.find('a','lcname')):	
														k.append(i.find('a','lcname').text)
													else:
														k.append('Not given')
													if(i.find('p','desc')):
														k.append(i.find('p','desc').text)
													else:
														k.append('Not given')	
													rs=i.find('span','ls_co phn').text
													if rs:
														k.append(rs)
													else:
														k.append('Not given')
													if(i.find('span','clg')):
														k.append(i.find('span','clg').next)
													else:
														k.append('Not Given')
													if(i.find('span','srad cty-t')):
														k.append(i.find('span','srad cty-t').text)
													else:
														k.append('Not Given')
													#k.append(i.find('a','lcname').get('href'))
													if(i.find('span','srad cty-t')):
														k.append(i.find('a').get('href'))
													else:
														k.append('Not Given')
													k.append(u)
													#km.append(k)
													row.writerow(k)"""
			#print(ct)

			for num in range(2,11):
			    #U='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=borsad&pg=2&c=IN&scroll=1&pr=0&frsc=20'
				url='https://dir.indiamart.com/search.mp/next?ss=warehousing+services&cq='+ct+'&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp/next?ss=warehouse&cq=kolkata&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp?ss=warehouse&cq='+str(ct)
				#url='https://dir.indiamart.com/search.mp/next?ss=logistic+provider&pg='+str(num)+'&c=IN&scroll=1&pr=0&frsc=22'
				#url='https://dir.indiamart.com/search.mp/next?ss=logistics+provider&pg='+str(num)+'&c=IN&scroll='+str(num)+'&pr=0&frsc='+str(num)
				#print('ui  ',url)
				#driver.clear()
				#driver.get(url)
				#r=driver.page_source
				r=s.get(url)
				string=str(r)
				st=string.replace('\\','').replace('tt','')
				#st=string.replace('\\t','').replace('\\n','').replace('\\&quot;','').replace('\\gt;','>').replace('\\lt;','<').replace('\\/','')
				soup=BS(st,'html.parser')
				temp=soup.find_all('div','lst')
				km=[]
				print('writing : ',num)
				for i in temp:
					#km=[]
					k=[]
					t=i.find('a')
					if t:
						k.append(i.find('a').text)
					else:
						k.append('Not Given')

					if(i.find('a','lcname')):	
						k.append(i.find('a','lcname').text)
					else:
						k.append('Not given')
					
					if(i.find('p','desc')):
						k.append(i.find('p','desc').text)
					else:
						k.append('Not given')	
					
					rs=i.find('span','ls_co phn')
					if rs:
						k.append(rs)
					else:
						k.append('Not given')
					if(i.find('span','clg')):
						k.append(i.find('span','clg').next)
					else:
						k.append('Not Given')
					if(i.find('span','srad cty-t')):
						k.append(i.find('span','srad cty-t').text)
					else:
						k.append('Not Given')
					#k.append(i.find('a','lcname').get('href'))
					if(i.find('span','srad cty-t')):
						k.append(i.find('a').get('href'))
					else:
						k.append('Not Given')
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




us = driver.find_element_by_name('txtUsername')
us.send_keys('rahim')
pas = driver.find_element_by_name('txtPassword')
pas.send_keys('himanshi')
c = driver.find_element_by_class_name('g-recaptcha')
c.click()
c = driver.find_element_by_name('btnSubmit')
c.click()







http://www.ali.web.id/web2/member_list.php?p=str(259)
250

 m=soup.find_all('div','member_list')
 m[0].find('a').get('href')


for i in link:
	driver.get(i)
	soup=BS(driver.page,'html.parser')
	dt=soup.find_all('div','profile_right')
	data=[i.text for i in dt]
	data.append(i)
	row.writerow(data)