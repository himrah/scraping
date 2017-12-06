"""table=soup.find('table','text2_thai')
dl = table.find_all('tr',attrs={'valign':'middle','bgcolor':'#BC9CF8'})
for i in dl:
	i.replaceWith('')
tr=table.find_all('tr',attrs={'valign':'middle'})
tr[3].find_all('td',attrs={'colspan':'2'})[1].text

address = tr[0]
telephone = tr[1]
Fax = tr[2]
Email = tr[3]
Website = tr[4]
Contact = tr[5]

#type_of_service=table.find_all('td',attrs={'colspan':'3'})[0].text.strip()
type_of_service=str(table.find_all('td',attrs={'colspan':'3'})[0]).replace('<br/>',',').replace('<td colspan="3" valign="middle">','').replace('</td>',' ').strip()
service_include=str(table.find_all('td',attrs={'colspan':'3'})[1]).replace('<br/>',',').replace('<td colspan="3" valign="middle">','').replace('</td>',' ').strip()
area_service=str(table.find_all('td',attrs={'colspan':'4'})[0]).replace('<br/>',',').replace('<td colspan="4">','').replace('</td>',' ').strip()
tocs=str(table.find_all('td',attrs={'colspan':'4'})[1]).replace('<br/>',',').replace('<td colspan="4">','').replace('</td>',' ').strip()"""
import requests
from bs4 import BeautifulSoup as BS
import csv
class SC:
	def scrap(self):
		f=open('link.txt').read()
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		head=['Address','Telephone','Fax','Email','Website','Contact','Type of Service','Service Include','Area Services','Type of Cargo Service']
		li=f.split('\n')
		for u in li:
			data=[]
			r=requests.get(u)
			soup=BS(r.content,'html.parser')
			table=soup.find('table','text2_thai')
			dl = table.find_all('tr',attrs={'valign':'middle','bgcolor':'#BC9CF8'})
			for d in dl:
				d.replaceWith('')
			tr=table.find_all('tr',attrs={'valign':'middle'})
			if(tr[0]):
				#data.append(tr[0].text)
				data.append(tr[0].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')
			if(tr[1]):
				data.append(tr[1].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')
			if(tr[2]):
				data.append(tr[2].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')
			if(tr[3]):
				data.append(tr[3].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')												
			if(tr[4]):
				data.append(tr[4].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')
			if(tr[5]):
				data.append(tr[5].find_all('td',attrs={'colspan':'2'})[1].text.strip())
			else:
				data.append('Not Given')
			if(str(table.find_all('td',attrs={'colspan':'3'})[0]).replace('<br/>',',').replace('<td colspan="3" valign="middle">','').replace('</td>',' ').strip()):
				data.append(str(table.find_all('td',attrs={'colspan':'3'})[0]).replace('<br/>',',').replace('<td colspan="3" valign="middle">','').replace('</td>',' ').strip())
			else:
				data.append('Not Given')
			temp=str(table.find_all('td',attrs={'colspan':'3'})[1]).replace('<br/>',',').replace('<td colspan="3" valign="middle">','').replace('</td>',' ').strip()
			if(temp):
				data.append(temp)
			else:
				data.append('Not Given')
			temp=str(table.find_all('td',attrs={'colspan':'4'})[0]).replace('<br/>',',').replace('<td colspan="4">','').replace('</td>',' ').strip()
			if(temp):
				data.append(temp)
			else:
				data.append('Not Given')
			temp=str(table.find_all('td',attrs={'colspan':'4'})[1]).replace('<br/>',',').replace('<td colspan="4">','').replace('</td>',' ').strip()							
			if(temp):
				data.append(temp)
			else:
				data.append('Not Given')
			data.append(u)	
			row.writerow(data)
			print(u)
obj=SC()
obj.scrap()			


							

