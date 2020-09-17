import requests
from bs4 import BeautifulSoup
import sqlite3

# HABER OKUMA UYGULAMASI
while True:
    print("Lütfen bekleyin... Haberler çekiliyor...\n")

    url = "http://haberler.com"

    istek = requests.get(url)

    icerik = istek.content

    soup = BeautifulSoup(icerik, "html.parser")

    print("BUGÜNKÜ HABERLER ŞU ŞEKİLDE:\n ***")

    sayi = 1

    haberler = soup.find_all("p", {"class": "haberler-title"})

    for i in haberler:
        if sayi == 1:
            sayi += 1
            continue
        print(sayi, "-)", i.text)
        sayi += 1

    sayiGir = input("\nOKUMAK İSTEDİĞİNİZ HABERİN NUMARASINI YAZIP ENTER'A BASIN !\n")

    link = soup.find("a", {"title": haberler[int(sayiGir)-1].text}).get("href")

    istekHaber = requests.get(link)
    soupHaber = BeautifulSoup(istekHaber.content, "html.parser")

    metin = soupHaber.find_all("div", {"class": "haber_metni"})

    for i in metin:
        print(i.text)

    secim = input("Geri dönmek için bir tuşa basın.\n")

