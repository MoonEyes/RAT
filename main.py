import requests
from bs4 import BeautifulSoup as soup
import base64

url = "http://twitter.com/S1mpleCC"
data = requests.get(url)

#print(data.text)

data2 = soup(data.text,"html.parser")
#print(type(data2))

#print(data2.prettify())

print(data2.title)
cmd = data2.find("div", {"class":"tweet"}).find("div",{"class":"js-tweet-text-container"}).find("p").string
print(cmd)
print(type(cmd))
payload = base64.b64decode(cmd)
print(type(payload))
print(payload)
"""

cmd = data2.find("div", {"class":"entry-content"}).find("p").string

payload = str(base64.b64decode(cmd), 'utf-8')
print(payload)
"""
