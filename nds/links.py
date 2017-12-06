from bs4 import BeautifulSoup as BS
import requests
import re

class SC:
	def __init__(self):
		self.f=open('l.txt','w')
		self.murl = 'https://en.indotrading.com'
	
	def req(self,link):
		r=requests.get(link,verify=False)
		soup=BS(r.content,'html.parser')
		return soup

	def next_page(self,i,soup):
		if str(soup.find('li','active').next.next.next).strip():
		#if nxt:
			nxt = soup.find('li','active').next.next.next.text
			tt=re.search(r'^/(.*?)',i)
			if tt:
				new_url = self.murl+i+nxt
			else:	
				new_url = i+nxt
			print(new_url)
			soup = self.req(new_url)
			for ss in soup.find_all('a','product_title'):
				self.f.write(ss.get('href')+'\n')
			return new_url
			

	def scarap(self):
		#main_url=['https://en.indotrading.com/lampudanpencahayaan_84/','https://en.indotrading.com/kerajinandankesenian_46/','https://en.indotrading.com/makanandanminuman_79/','https://en.indotrading.com/mainandanhobby_92/','https://en.indotrading.com/olahragadanhiburan_684/','https://en.indotrading.com/pakaiandanaksesoris_71/','https://en.indotrading.com/peralatanrumahdantaman_82/','https://en.indotrading.com/peralatankantorsekolahdanalattulis_86/','https://en.indotrading.com/perawatandiridankecantikan_782/','https://en.indotrading.com/taskotakdancasing_74/','https://en.indotrading.com/tekstildankulit_91/']
		#main_url=['https://en.indotrading.com/kerajinandankesenian_46/','https://en.indotrading.com/makanandanminuman_79/','https://en.indotrading.com/mainandanhobby_92/']
		num=3
		if(num>1):
		#for url in main_url:
			#soup = self.req(url)
			#l=soup.find('ul','theme_menu cats el-cats')

			#c=soup.find_all('div','mega_menu clearfix')
			#for i in c:
			#	i.replaceWith('')

			#p=soup.find_all('li','has_megamenu')
			#l=soup.find('ul','theme_menu cats el-cats')
			#links = [i.get('href')  for i in l.find_all('a')]
			links = ['https://en.indotrading.com/peralatankantor_453/', 'https://en.indotrading.com/kerajinankayu_102/', 'https://en.indotrading.com/minuman_340/', 'https://en.indotrading.com/produkhewanpeliharaan_849/', 'https://en.indotrading.com/mainanbayi_501/', 'https://en.indotrading.com/produkperawatanpribadi_783/', 'https://en.indotrading.com/benang_576/', 'https://en.indotrading.com/tangga_4887/', 'https://en.indotrading.com/taman_776/', 'https://en.indotrading.com/bahankulit_575/', 'https://en.indotrading.com/board_4931/', 'https://en.indotrading.com/dompet-dan-holder_4904/', 'https://en.indotrading.com/barangpromosi_114/', 'https://en.indotrading.com/alattuliskantor_3203/', 'https://en.indotrading.com/kerajinankain_112/', 'https://en.indotrading.com/kerajinantanahlist_118/', 'https://en.indotrading.com/koper-dan-tas-travel_4900/', 'https://en.indotrading.com/pembersihruangan_409/', 'https://en.indotrading.com/kuedanmakanankering_747/', 'https://en.indotrading.com/tas-khusus_4902/', 'https://en.indotrading.com/makanantradisional_3556/', 'https://en.indotrading.com/tekstil-kebutuhan-rmah_4940/', 'https://en.indotrading.com/mainanplastik_504/']
			#links[i.get('href') for i in l.find_all('a')]
			#links=['https://en.indotrading.com/lampudarurat_445/']
			#links=['https://en.indotrading.com/senter_450/','https://en.indotrading.com/lampustrobo_898/','https://en.indotrading.com/lampurotari_899/','https://en.indotrading.com/lampu-dalam-ruang_4877/','https://en.indotrading.com/lampudownlight_446/','https://en.indotrading.com/lampudinding_447/','https://en.indotrading.com/lampumeja_448/','https://en.indotrading.com/lampuhias_449/','https://en.indotrading.com/lampugantung_1860/','https://en.indotrading.com/lampu-bohlam-dan-tabung_4878/','https://en.indotrading.com/lampuhematenergi_440/','https://en.indotrading.com/lampuhalogen_441/','https://en.indotrading.com/bolalampulainnya_443/','https://en.indotrading.com/lampu-tl_2029/','https://en.indotrading.com/lampuultraviolet_4418/','https://en.indotrading.com/pencahayaan-profesional_4879/','https://en.indotrading.com/lampublitz_900/','https://en.indotrading.com/lampupar_3554/','https://en.indotrading.com/jual-lampu-laser/','https://en.indotrading.com/jual-lampu-plafon/','https://en.indotrading.com/jual-lampu-proyektor/','https://en.indotrading.com/jual-lampu-baca/']
			for i in links:
				#print(i)
				tt=re.search(r'^/(.*?)',i)
				if tt:
					soup = self.req(self.murl+i)
				else:
					soup = self.req(i)	
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


main_url=['https://en.indotrading.com/kerajinandankesenian_46/','https://en.indotrading.com/makanandanminuman_79/','https://en.indotrading.com/mainandanhobby_92/','https://en.indotrading.com/peralatanrumahdantaman_82/','https://en.indotrading.com/peralatankantorsekolahdanalattulis_86/','https://en.indotrading.com/perawatandiridankecantikan_782/','https://en.indotrading.com/taskotakdancasing_74/','https://en.indotrading.com/tekstildankulit_91/']


618647717
9y5b3d

r=requests.get('https://en.indotrading.com/jual-kap-lampu')
soup=BS(r.content,'html.parser') 

Next page link =  soup.find('li','active').next.next.next.text 

Product links = soup.find('div','two-lines-elipsis').find('a').get('href')



url='https://en.indotrading.com/lampudanpencahayaan_84/'
l=soup.find('ul','theme_menu cats el-cats')

links [i.get('href') for i in l.find_all('a')]"""

