from bs4 import BeautifulSoup as BS
from requests import Session

s=Session()

kk=open('temp.txt','r').read()
w=open('link.txt','w')
kk=kk.split('\n')
m='http://www.esuppliersindia.com'

for i in kk:
#     print(i)
     num=1099
     n='?page_no='+str(num)
     r=s.post(i)
#     print(r)
     soup=BS(r.content,'html.parser')
     
     num=2
     while(soup.find('title').text):
          #if(num==420):
           #    num=766
            #   break;
          ll=soup.find_all('td','bluebg')
          for j in ll:
             #print(j)
             l=j.find('a')
             #nl.append(r.url+' : '+m+l.get('href'))
             w.write(r.url+' : '+m+l.get('href')+'\n')
          print(r.url)
          n='?page_no='+str(num)
          r=s.post(i+n)
          soup=BS(r.content,'html.parser')
          num+=1



"""r=s.post('http://www.esuppliersindia.com/suppliers/apparel-fashion/fashion-accessories/')
soup=BS(r.content,'html.parser') 
t=soup.find_all('strong','oragne-f12b')
del t[0]

In [124]: for i in t:                                                                              
     ...:     te=i.find('a')                      
     ...:     lll.append(m+te.get('href'))"""
