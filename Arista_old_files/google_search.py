import requests
from bs4 import BeautifulSoup

user='2 idayappam calories'
URL = "https://www.google.co.in/search?q=" + user
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
result=''
# try:
#     result = soup.find("div",class_='LGOjhe').get_text()
# except:
#     try:
#         result = soup.find("div",class_='Z0LcW an_fna').get_text()
#     except:
#         try:
#             result = soup.find("div",class_='IZ6rdc').get_text()
#         except:
#             print("Unable to find your result I think there's some problem with your input :) Sorry for that")
result = soup.find("div",class_='webanswers-webanswers_table__webanswers-table')
print(result)
li=[]
for i in result.findAll("td"):
    li.append(i.text)
for i in li:
    if 'cal' in i:
        k=i
        break
print(k[:k.index(' ')])