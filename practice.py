import requests
from bs4 import BeautifulSoup
res= requests.get("http://v.media.daum.net/v/20170615203441266")
soup = BeautifulSoup(res.content, 'html.parser')
print(res.content)
mydata =soup.find('title')
print(mydata.get_text())



