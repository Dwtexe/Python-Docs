import requests
from bs4 import BeautifulSoup

istek = requests.get("https://www.spotify.com/tr/")

icerik = istek.content

soup = BeautifulSoup(icerik, "html.parser")

print(soup.prettify())