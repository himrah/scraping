from bs4 import BeautifulSoup as BS
import requests

class SC:
	def __init__(self):
		self.f=open('l.txt','w')

	
	def req(self,link):
		r=requests.get(link)
		soup=BS(r.content,'html.parser')
		return soup

	def next_page(self,i,soup):
		if str(soup.find('li','active').next.next.next).strip():
		#if nxt:
			nxt = soup.find('li','active').next.next.next.text
			new_url = i+nxt
			print(new_url)
			soup = self.req(new_url)
			for ss in soup.find_all('a','product_title'):
				self.f.write(ss.get('href')+'\n')
			return new_url
			

	def scarap(self):
		main_url=['https://en.indotrading.com/kerajinandankesenian_46/','https://en.indotrading.com/makanandanminuman_79/','https://en.indotrading.com/mainandanhobby_92/','https://en.indotrading.com/olahragadanhiburan_684/','https://en.indotrading.com/pakaiandanaksesoris_71/','https://en.indotrading.com/peralatanrumahdantaman_82/','https://en.indotrading.com/peralatankantorsekolahdanalattulis_86/','https://en.indotrading.com/perawatandiridankecantikan_782/','https://en.indotrading.com/taskotakdancasing_74/','https://en.indotrading.com/tekstildankulit_91/']
		for url in main_url:
			soup = self.req(url)
			l=soup.find('ul','theme_menu cats el-cats')
			links = [i.get('href')  for i in l.find_all('a')]
			#links[i.get('href') for i in l.find_all('a')]
			for i in links:
				#print(i)
				soup = self.req(i)
				#soup = self.req(new_url)
				print(i)
				for ss in soup.find_all('a','product_title'):
					self.f.write(ss.get('href')+'\n')
				while(str(soup.find('li','active').next.next.next).strip()):
				#if nxt:
					nn=self.next_page(i,soup)
					soup = self.req(nn)

"""					nxt = soup.find('li','active').next.next.next.text
					new_url = i+nxt
					print(new_url)
					soup = self.req(new_url)
					for ss in soup.find_all('a','product_title'):
						f.write(ss.get('href')+'\n')"""

						

					#product_links=[i.get('href') for i in soup.find_all('a','product_title')]

    
obj=SC()
obj.scarap()

"""main_url=[]







r=requests.get('https://en.indotrading.com/jual-kap-lampu')
soup=BS(r.content,'html.parser') 

Next page link =  soup.find('li','active').next.next.next.text 

Product links = soup.find('div','two-lines-elipsis').find('a').get('href')



url='https://en.indotrading.com/lampudanpencahayaan_84/'
l=soup.find('ul','theme_menu cats el-cats')

links [i.get('href') for i in l.find_all('a')]"""
 
