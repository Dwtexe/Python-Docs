
#Alttaki benim yazdığım
import sqlite3
import time

def ogrenciBilgi(ogrenciAdi):
    bilgi = cursor.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad=?",(ogrenciAdi,))
    a = bilgi.fetchall()
    if len(a) == 0 :
        print("Böyle Bir Öğrenci Bulunmamaktadır!")
        time.sleep(3)
        return 0 # Kayıtsız isim girilirse 0 döndürür
    else:
        for i in a:
            print("Öğrenci Numarası :",i[0],"\nÖğrenci Adı : ",i[1])
            print("*** Öğrenci Bilgileri Yükleniyor... ***")
        time.sleep(2)

def dersNotu(ogrenciAdi):
    numara = cursor.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ? ",(ogrenciAdi,))
    numara = numara.fetchone()[0] # İlk satırda ne varsa onu döndürür ve dizinin 0. elemanı alır
    notlar = cursor.execute("SELECT * FROM dersNotlari WHERE ogrenci_no = ?",(numara,))
    a = notlar.fetchall()
    print("MATEMATİK : ",a[0][1],"FİZİK : ",a[0][2],"KİMYA : ",a[0][3],"BİYOLOJİ : ",a[0][4])
    time.sleep(3)

def yeniOgrenci(ogrenciAdi):
    cursor.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(ogrenciAdi,))
    print(ogrenciAdi,"isimli öğrenci başarıyla eklenmiştir...")
    time.sleep(3)

def notEkle(ogrenciNo,ders,dersNotu):
    while True:
        bilgi = cursor.execute("SELECT * FROM dersNotlari WHERE ogrenci_no = ?", (ogrenciNo,))
        a = bilgi.fetchall()
        if len(a) == 0:

            if ders == "matematik":

                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,matematik)  VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Matematik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            elif ders == "fizik":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,fizik) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Fizik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "kimya":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,kimya) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Kimya Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            elif ders == "biyoloji":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,biyoloji) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Biyoloji Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            else:
                print("Hatalı Seçim")
                time.sleep(2)
                break


        else:

            if ders == "matematik":

                cursor.execute("UPDATE dersNotlari SET matematik = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
                print("Matematik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break



            elif ders == "fizik":

                cursor.execute("UPDATE dersNotlari SET fizik = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Fizik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "kimya":

                cursor.execute("UPDATE dersNotlari SET kimya = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Kimya Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "biyoloji":

                cursor.execute("UPDATE dersNotlari SET biyoloji = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Biyoloji Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            else:
                print("Hatalı Seçim")
                time.sleep(2)
                break


def devamsizlikEkle(ogrenciNo,tarih):
    cursor.execute("INSERT INTO devamsizlik VALUES (?,?)",(ogrenciNo,tarih))
    print("Devamsızlık Başarıyla Eklenmiştir!")
    time.sleep(3)

def devamsizlikOgren(ogrenciAdi):
    numara = cursor.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ?",(ogrenciAdi,))
    numara = numara.fetchone()[0]

    devamsizlik = cursor.execute("SELECT * FROM devamsizlik WHERE ogrenci_no = ?",(numara,))
    a = devamsizlik.fetchall()
    for i in a :
        print("Gelmediği Tarih : ",i[1])
    time.sleep(3)


print("Öğrenci Bilgi Sistemine Hoşgeldiniz!")
while True:
    baglanti = sqlite3.connect("ogrenciData.db")

    cursor = baglanti.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'ogrenciler' ('ogrenci_no' INTEGER ,'ogrenci_ad' TEXT,PRIMARY KEY ('ogrenci_no'))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'dersNotlari' ('ogrenci_no' INTEGER,'matematik' INTEGER,'fizik' INTEGER,'kimya' INTEGER,'biyoloji' INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'devamsizlik' ('ogrenci_no' INTEGER,'devamsizlik_tarih' TEXT)")

    print('''
    1 - Öğrenci Bilgileri
    2 - Yeni Öğrenci Kayıtı
    3 - Ders Notu Ekle
    4 - Devamsızlık Ekle
    q - Çıkış Yap
    ''')

    secim = input("Seçiminiz : ")

    if secim == "1" :
        isim = input("Öğrencinin Adı : ")
        a = ogrenciBilgi(isim)
        if (a != 0): # Fonksiyonda return 0 olup olmadığını kontrol eder

            print('''
               1 - Not Bilgisi
               2 - Devamsızlık Bilgisi
               q - Çıkış
               ''')
            secim = input("Seçiminiz : ")

            while True:
                if secim == "q":
                    break
                elif secim == "1":
                    dersNotu(isim)
                    break
                elif secim == "2":
                    devamsizlikOgren(isim)
                    break
                else:
                    print("Hatalı Tuşlama !!!")


    elif secim == "2":
        isim = input("Eklemek İstediğiniz Öğrencini Adı :")
        yeniOgrenci(isim)
    elif secim == "3":
        numara = input("Öğrenci Numarasını Giriniz : ")
        print("*****DERSLER*****")
        print('''
        matematik
        fizik
        kimya
        biyoloji''')
        secim = input("Ders Seçiniz : ")
        dersNotu = input("Ders Notunu Giriniz : ")
        notEkle(numara,secim,dersNotu)
    elif secim == "4":
        numara = input("Öğrenci Numarasını Giriniz : ")
        tarih = input("Devamsızlık Tarihini Giriniz : ")
        devamsizlikEkle(numara,tarih)
    elif secim == "q":
        print("Çıkış Yapıldı...")
        baglanti.close()
        break
    else:
        print("Hatalı Tuşlama !!!")

    baglanti.commit()
    baglanti.close()









"""
import sqlite3,os,time

baglanti = sqlite3.connect("ogrenciData.db")
pen = baglanti.cursor()

menu2 = """
#Hangi Dersin Notunu Girmek İstersin
#[1] Matematik
#[2] Türkçe
#[3] Fen

"""

def ogrenciBilgi(ogrenciAdi):
    bilgi = pen.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad=?",(ogrenciAdi,))
    for i in bilgi.fetchall():
        print(f"Öğrenci numarası: {i[0]} Öğrenci Adı: {i[1]}")
    baglanti.commit()

def yeniOgrenci(ogrenciAd):
    pen.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(ogrenciAd,))
    print(f"{ogrenciAd} isimli öğrenci başarıyla kaydedildi..")
    baglanti.commit()

def notEkle(ogrenciNo,ders,dersNotu):
    if ders =="1":
       pen.execute("INSERT INTO ders_not (ogrenci_no,matematik) VALUES (?,?)",(ogrenciNo,dersNotu))
    if ders =="2":
       pen.execute("INSERT INTO ders_not (ogrenci_no,türkçe) VALUES (?,?)",(ogrenciNo,dersNotu))
    if ders =="3":
       pen.execute("INSERT INTO ders_not (ogrenci_no,fen) VALUES (?,?)",(ogrenciNo,dersNotu))
    baglanti.commit()
    print("İşlem başarıyla tamamlandı...")

def devamsizlikEkle(ogrenciNo,tarih):
    pen.execute("INSERT INTO devamsizlik VALUES (?,?)",(ogrenciNo,tarih))
    print("İşlem başarı ile tamamlandı...")
    baglanti.commit()

#FIXME KAFA KALMADI BENDE ÇÖZEMEDİM
def dersNotBilgi(ogrenciAdi):
    numara = pen.execute("SELECT ogrenci_no FROM ogrenciler ogrenci_ad = ? ",(ogrenciAdi,))
    numara = numara.fetchone()[0]

    notlar = pen.execute("SELECT * FROM  ders_not WHERE ogrenci_no = ? ",(numara,))
    a = notlar.fetchall()
    print(f"Türkçe: {a[0][1]}\nMatematik: {a[0][2]}\nFen: {a[0][3]}")

def main():
    while True:
        if os.name =="nt":
            os.system("cls")
        elif os.name =="posix":
            os.system("clear")
        print("Hoşgeldiniz...")
        menu = 
        
        
#       [1] Öğrenci Bilgileri
#       [2] Yeni Öğrenci Ekle
#       [3] Ders Notu Ekle
#       [4] Devamsızlık Ekle
#       [0] Çıkış

        """
"""
        
        secim = input(menu)

        if secim == "1":
            isim = input("Öğrencinin Adı: ")
            ogrenciBilgi(isim)
            secim2 = input("[1] Ders Notları\n[2] Devamsızlık Bilgisi\n")
            if secim2 == "1":
                dersNotBilgi(isim)
            else:
                pass
            
            time.sleep(2)
        elif secim=="2":
            isim = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
            yeniOgrenci(isim)
            secim2 = input()
            time.sleep(2)
        elif secim == "3":
            numara = input("Ders notu girmek istediğiniz öğrencinin numarası: ")
            secim = input(menu2)
            dersNotu = input("Bu derse ait not bilgisini giriniz: ")
            notEkle(numara,secim,dersNotu)
            time.sleep(2)
        elif secim == "4":
            numara = input("Devamsızlık bilgisi girmek istediğiniz öğrencinin numarası: ")
            tarih = input("Devamsızlık yaptığı tarihi giriniz: ")
            devamsizlikEkle(numara,tarih)
            time.sleep(2)
        elif secim == "0":
            print("İyi Günler...")
            break
    baglanti.commit()
    baglanti.close()

if __name__ == "__main__":
    main()

"""