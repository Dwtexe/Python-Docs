"""
tamamlanmalı...
"""


import os
kitapliste = list()

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[0] Çıkış
"""

def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Kitap Eklendi.")
    print("Ana menüye dönmek için 'enter'a basınız.")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in  liste:
        return True
    else:
        return False




while True:
    os.system("clear")
    print(menu)

    secim = input("İşlem numarasını yazınız : ")

    if secim == "1":
        kitap_isim = input("Kitap Adı : ")
        kitap_yazar = input("Yazar Adı : ")
        kitap = (kitap_isim,kitap_yazar)
        kitapEkle(kitap,kitapliste) #Kitap ekleniyor...

    elif secim == "2":
        

    elif secim == "3":
        pass

    elif secim == "0":
        print("Keyifli Okumalar...")
        quit()
    
    else:
        print("Hatalı Yazım!!")