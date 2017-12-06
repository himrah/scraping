import re
#from bs4 import BeautifulSoup as BS
from requests import Session
class SC:
	def scrap(self):
		s=Session()
		s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
		s.headers.update({'Referer':"https://dir.indiamart.com/search.mp?ss=logistics+provider&source=autosuggest"})
		link_id='gdlc_cd=100000001&gdmc_cd=200000001'
		url='http://list.qoo10.sg/gmkt.inc/Category/?'
		ajax_url='http://list.qoo10.sg/gmkt.inc/Search/SearchResultAjaxTemplate.aspx'
		#links=[]
		num=1
		f=open('l.txt','w')
		for i in range(1,2000):
			data={"gdlc_cd":"100000001","gdmc_cd":"200000001","keywordArrLength":"1","is_img_search_yn":"N","sortType":"SORT_RANK_POINT","dispType":"UIG5","filterDelivery":"NNNNNANNNNNNNN","is_research_yn":"Y","coupon_filter_no":"0","partial":"on","curPage":i,"pageSize":120,"ajax_search_type":"C","___cache_expire___":"1501371657390"}
			res=s.post(ajax_url,data)
			#re.search('by<a href="(.*?)"',str(ss)).group(1)
			regex=re.compile('by<a href="(.*?)"')
			it = re.finditer(regex, str(res.content))
			for match in it:
				f.write(match.group(1)+'\n')

				#links.append()
			#soup=BS(r.content,'')
			#data={}
			print(ajax_url+" : "+str(num))
			num+=1



obj=SC()
obj.scrap()	

#data={"gdlc_cd":"100000001","gdmc_cd":"200000001","keywordArrLength":"1","is_img_search_yn":"N","sortType":"SORT_RANK_POINT","dispType":"UIG5","filterDelivery":"NNNNNANNNNNNNN","is_research_yn":"Y","coupon_filter_no":"0","partial":"on","curPage":"5","pageSize":1,"ajax_search_type":"C","___cache_expire___":"1501371657390"}