import requests
from bs4 import BeautifulSoup
import sqlite3



url = "https://www.haberler.com/"

istek = requests.get(url)

icerik = istek.content

soup = BeautifulSoup(icerik, "html.parser")


print(soup.prettify())

print(soup.find_all("a"))

for i in soup.find_all("a"):
    print (i)
    print("---")


for i in soup.find_all("a"):
    # print(i.get("href"))
    print(i.text)
    print("---")



for i in soup.find_all("p",{"class": "haberler-title"}):
    print(i.text)


print("---")

print (soup.find_all("a",{"title": "Adaylık için 100 bin imza süresi bu akşam doluyor! İşte son rakamlar"}))
