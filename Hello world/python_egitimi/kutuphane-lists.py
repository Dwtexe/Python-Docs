kitapListesi = list()

menu = """
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitapları Listele
[0] Çıkış

"""

def kitapEkle(kitap,liste):
    liste += [kitap]
    print("Kitap  Eklendi")
    input("Ana menüye dönmek için 'enter'a basınız.")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print(f"Kitap Adı ---->>  {i}")
    print("Ana menüye dönmek için 'enter'a basınız.")

def cik():
    quit()
    
while True:
    print(menu)

    secim = input("Seçiminiz : ")

    if secim == "1":
        kitapAdi = input("Kitap Adı: ")
        kitapEkle(kitapAdi,kitapListesi)

    elif secim == "2":
        kitapCikar()

    elif secim == "3":
        listele(kitapListesi)

    elif secim == "0":
        cik()
    
    else:
        print("Hatalı Yazım!!")
        input("Ana menüye dönmek için 'enter'a basınız.")