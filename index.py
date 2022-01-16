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
# def get_form_details(form):
#     """Returns the HTML details of a form,
#     including action, method and list of form controls (inputs, etc)"""
#     details = {}
#     # get the form action (requested URL)
#     action = form.attrs.get("action").lower()
#     # get the form method (POST, GET, DELETE, etc)
#     # if not specified, GET is the default in HTML
#     method = form.attrs.get("method", "get").lower()
#     # get all form inputs
#     inputs = []
#     for input_tag in form.find_all("input"):
#         # get type of input form control
#         input_type = input_tag.attrs.get("type", "text")
#         # get name attribute
#         input_name = input_tag.attrs.get("name")
#         # get the default value of that input tag
#         input_value =input_tag.attrs.get("value", "")
#         # add everything to that list
#         inputs.append({"type": input_type, "name": input_name, "value": input_value})
#     # put everything to the resulting dictionary
#     details["action"] = action
#     details["method"] = method
#     details["inputs"] = inputs
#     return details


from bs4 import BeautifulSoup
import requests



link_address = "http://192.168.144.129/dvwa/"
print(link_address)
response = requests.get(link_address)
html_page = response.content
soup = BeautifulSoup(html_page, "html5lib")

links = []
# links = soup.findAll("a")
for link in soup.findAll('form'):
    links.append(link.get('action'))



print(links)



