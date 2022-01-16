from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import webbrowser



def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

session = HTMLSession()
link_address = "http://192.168.1.106/mutillidae/index.php?page=login.php"
# get all form tags
response = session.get(link_address)
soup = BeautifulSoup(response.html.html, "html.parser")
forms = soup.find_all("form")
print(forms[0])
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)

# iteratte over forms
for i, form in enumerate(forms, start=1):
    form_details = get_form_details(form)
    print("="*50, f"form #{i}", "="*50)
    print(form_details)

first_form = forms[0]

form_details = get_form_details(first_form)
data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        # if it's hidden, use the default value
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["type"] != "submit":
        # all others except submit, prompt the user to set it
        value = input(f"Enter the value of the field '{input_tag['name']}' (type: {input_tag['type']}): ")
        data[input_tag["name"]] = value

# join the url with the action (form request URL)
url = urljoin(link_address, form_details["action"])



# write the page content to a file
open("page.html", "w").write(str(soup))

# open the page on the default browser
webbrowser.open(url)