"""In [32]: for i in f:
    ...:     driver.get(i)
    ...:     soup=BS(driver.page_source,'html.parser')
    ...:     t=soup.find_all('a','touchable primary')
    ...:     for j in t:
    ...:         w.write(i+' : '+j.get('href')+'\n')
    ...:         #l.append(j.get('href'))
    ...:     print(i)


add=soup.find('div','_5aj7 _3-8j _20ud').text
phone=soup.find('div','_5aj7 _3-8j').text


title soup.title.text
add = soup.find('div','_2pie').find('div','_3n4n').find('div','_5aj7 _3-8j _20ud').text
ph = soup.find('div','_2pie').find('div','_3n4n').find('div','_5aj7 _3-8j').text
lists=soup.find('div','_2pie').find('div','clearfix').find_all('div','_5aj7 _3-8j')"""


from selenium import webdriver
from bs4 import BeautifulSoup as BS
import sys
class SC:
    def scrap(self):
        #reload(sys)
        #sys.setdefaultencoding('utf8')
        num=1
        f=open("single_link.txt",'r').read().split('\n')
        w=open('new.txt','w')
        #driver=webdriver.Chrome()
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chromeOptions.add_experimental_option("prefs",prefs)
        driver=webdriver.Chrome(executable_path='/home/himrah/Downloads/ch/chromedriver',chrome_options=chromeOptions)
        for i in f:
            driver.get(i)
            soup=BS(driver.page_source,'html.parser')
            main=soup.find('div','_2pie')
            if(main):
                add=main.find('div','_3n4n')
                if(add):
                    add=add.find('div','_5aj7 _3-8j _20ud')
                    if(add):
                        add=add.text

                ph=main.find('div','_3n4n')
                if(ph):
                    ph=ph.find('div','_5aj7 _3-8j')
                    if(ph):
                        ph=ph.text    

                em=main.find('div','clearfix')            
                mm=''
                
                if(em):
                    em=em.find_all('div','_5aj7 _3-8j')
                    if(em):
                        for j in em:
                            mm=mm+'<'+j.text
                t=soup.find('div','_19sz')
                if(t):
                    t=t.find('a').text

                w.write(str(t)+'^'+str(i)+'^'+str(add)+'^'+str(ph)+'^'+str(mm)+'\n')
                print(i+' : '+str(num))
                num=num+1


obj = SC()
obj.scrap()
"""
#b=a.find('div','_3n4n')
if(a):
    add=a.find('div','_3n4n').find('div','_5aj7 _3-8j _20ud').text
else:
    add="Not given"
b=a.find('div','_3n4n')
if(b):
    ph=b.find('div','_5aj7 _3-8j').text
else:
    ph="Not given"
m=a.find('div','clearfix')
#mm=[i.get('href') for i in m]
mm=''
if(m):
    m=m.find_all('div','_5aj7 _3-8j')
    for j in m:
        mm=mm+str(i.get('href'))
    w.write(i+' : '+add+' : '+ph+' : '+mm)"""

