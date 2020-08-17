import os
masalar = dict()

for i in range(10):
    masalar[i] = 0


def  hesapEkle():
    masaNo = int(input("Masa no : "))
    gecerli = masalar[masaNo]
    eklenecek = float(input("Eklenecek ücret : "))
    toplam = gecerli + eklenecek
    masalar[masaNo] = toplam

def  hesapSil():
    masaNo = int(input("Masa no : "))
    gecerli = masalar[masaNo]
    eksilecek = float(input("Silinecek ücret : "))
    toplam = gecerli - eksilecek
    if toplam < 0:
        print("Silinecek ücret, ücretten büyük olamaz!")
    else:
        masalar[masaNo] = toplam

def hesapKontrol(dosya_adi):
    veriler = list()
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True

    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close
        print("İlk defa program çalıştırıldığı için kayıt dosyası oluşturuldu.")
        flag = False

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])
    else:
        pass

def kayitGuncelle():
    dosya = open("log.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret,"\n")
    dosya.close()

def main():
    hesapKontrol("log.txt")
    while True:
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [0] Çıkış
        
        """)

        secim = input("İşleminiz : ")

        if secim == "1":
            for i in range(10):
                print(f"Masa {i} için hesap: {masalar[i]} Türk Lirası.")
            print("İşlem Tamamlandı!\nAna menüye dönmek için 'enter'a basınız.")
            input()
            os.system("clear")
            
        elif secim == "2":
            hesapEkle()
            print("İşlem Tamamlandı!\nAna menüye dönmek için 'enter'a basınız.")
            input()
            os.system("clear")
        
        elif secim == "3":
            hesapSil()
            print("İşlem Tamamlandı!\nAna menüye dönmek için 'enter'a basınız.")
            input()
            os.system("clear")

        elif secim == "0":
            
            print("Tekrar bekleriz...")
            quit()
main()