import requests
from bs4 import BeautifulSoup
import shutil


# url = "https://jsonplaceholder.typeicode.com/postes"

# data = {
#     "title" : "foo",
#     "body" : "bar",
#     "userId" : 1
#   }
# headers = {
#     "Content-type" : "application/json; charset=UTF-8"
#   }

# response = requests.get(url, headers=headers, json=data)
# print(response.text)
# # shutil.copy(response.text, "web.html")


url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all("h2"):
  print(heading.text)

