# from bs4 import BeautifulSoup
# from urllib.request import Request, urlopen
# import re
# link_address = input('enter your website address       >>   ')
# link_address = "https://www."+ link_address
# print(link_address)
# req = Request(link_address)
# html_page = urlopen(req)
#
# soup = BeautifulSoup(html_page, "html5lib")
#
# links = []
# for link in soup.findAll('a'):
#     links.append(link.get('href'))
#
# print(links)

from bs4 import BeautifulSoup
import requests
link_address = "https://www.varzesh3.com"
print(link_address)
response = requests.get(link_address)
html_page = response.content
soup = BeautifulSoup(html_page, "html5lib")

links = []
# links = soup.findAll("a")
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)