from requests import Session
from bs4 import BeautifulSoup as BS
import re
import csv

class SC:
	def scrap(self):
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		u='https://www.indotrading.com/AjaxMethod.asmx/UpdateCompanyPhoneLeads'

		#xl=open('t.csv','wt',newline='')
		xl=open('t.csv','wt',newline='', encoding="utf-8")
		row=csv.writer(xl)
		head=['Path','Title','Description','Company Information','Product Detail','Company Detail','Address','Phone','URL']
		row.writerow(head)
		f=open('newproduct.txt','r').read()
		#url=['https://en.indotrading.com/product/lampu-sorot-led-p80744.aspx','https://en.indotrading.com/product/lampu-flash-strobo-p325254.aspx','https://en.indotrading.com/product/lampu-sorot-led-p340609.aspx','https://en.indotrading.com/product/lampu-senter-led-p230543.aspx','https://en.indotrading.com/product/lampu-rotator-polisi-p193378.aspx','https://en.indotrading.com/product/senter-fire-safety-p414752.aspx','https://en.indotrading.com/product/senter-polisi-p34953.aspx']
		url=f.split('\n')
		#url=['https://export.indotrading.com/product/legging-pants-0614-p90635.aspx']
		nnnn=1
		for i in url:
			r=s.get(i)
			soup=BS(r.content,'html.parser')
			data=[]

			path = soup.find(attrs={'itemprop':'breadcrumb'})
			if path:
				data.append(path.text.replace('   ','--->'))
			else:
				data.append('Not given')

			title = soup.find('div','col-xs-8 nopad-left')
			if title:
				data.append(title.text)
			else:
				data.append('Not Given')

			desc = soup.find('div','jm-table-desc')
			if desc:
				data.append(desc.text)
			else:
				data.append('Not Given')



			cominfo = soup.find(attrs={'id':'cphBody_ctl00_company_info'})	
			if cominfo:
				data.append(cominfo.text)
			else:
				data.append('Not Given')
				

			product_detail = soup.find(attrs={'id':'tab-1'})	
			if product_detail:
				data.append(product_detail.text)
			else:
				data.append('Not Given')




			company_detail = soup.find(attrs={'id':'tab-2'})	
			if company_detail:
				data.append(company_detail.text)
			else:
				data.append('Not Given')

			address = soup.find_all('div','media-body')
			if address:
				if len(address)>1:
					data.append(address[1].text)
				else:
					data.append(address[0].text)
			else:
				data.append('Not Given')

			token=soup.find(attrs={'id':'hdToken'}).get('value')
			#print('Token ',token)			
			productid = soup.find('span','hidden hiddenProdId')
			if productid:
			#if pro
			#print('Product ',productid)
				compid = re.search(r'var CompanyID = (.*?);',r.text).group(1)
				compid = compid.replace("'",'')
				#compid = re.search(r'var CompanyID = (.*?);',r.text).group(1)
				#print('Comp',compid)
				arg = {'Token':token,'EncCompanyID':compid,'ProductID':productid.text}
				res=s.post(u,arg)
				#print('response : ',res.text)
				phone=re.search(r'{(.*?)}',str(res.text))
				if phone:
					data.append(phone.group(1))
				else:
					data.append('Not Given')	

			data.append(i)
			row.writerow(data)
			print(i+' : '+str(nnnn))
			nnnn+=1

obj=SC()
obj.scrap()

#y3x72u
