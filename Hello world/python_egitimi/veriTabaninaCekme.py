import requests
from bs4 import BeautifulSoup
import sqlite3

# HABERLERİ VERİTABANINA ÇEKME UYGULAMASI

url = "http://haberler.com"

istek = requests.get(url)

icerik = istek.content

soup = BeautifulSoup(icerik, "html.parser")

haberler = soup.find_all("p", {"class": "haberler-title"})

sayi = 1

for i in haberler:
    try:
        baglanti = sqlite3.connect('veritabani.db')
        kalem = baglanti.cursor()

        baslik = i.text

        link = soup.find("a", {"title": baslik}).get("href")

        istekHaber = requests.get(link)
        soupHaber = BeautifulSoup(istekHaber.content, "html.parser")

        metin = soupHaber.find("div", {"class": "haber_metni"}).text

        tarih = soupHaber.find("span", {"class": "nav1"}).text.lstrip()

        kalem.execute("INSERT INTO haber (haber_baslik, haber_icerik, haber_tarih) VALUES (?, ?, ?)", (baslik, metin, tarih))

        print("Haber eklendi!")

        sayi += 1

        baglanti.commit()
        baglanti.close()

    except:
        pass


print("\nİŞLEM TAMAM ! VERİTABANINA", sayi, "ADET HABER EKLENDİ !\n")
