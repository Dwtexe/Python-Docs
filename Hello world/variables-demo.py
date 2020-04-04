



# projede hatalar var düzeltilmesi gerek!!!!!!!!!!




"""
    1- Bir müşterinin ağağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik no
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı

"""

müsteriAdi = "Ali"
müsteriSoyadi = "Yılmaz"
müsteriIsimSoyisim = müsteriAdi +' '+ müsteriSoyadi # değişken kullanmak yerine direk isim soyisim de yazılabilir.
müsteriCinsiyet = 'Erkek'
müsteriTcKimlik = "12345678910"
müsteriDogumTarihi = 1998
müsteriAdresi = "Ahmet Vefik Paşa Mah. Değirmen Cad. No/21 Akbaş Holding Kestel/Bursa TÜRKİYE"  # Konum rastgele verilmiştir.
müsteriYasi = 22

print(" Aşağıda sisteme kaydolan kişilerin bilgilerini göreceksiniz")
print("Müşteri adı : " + müsteriAdi)
print("Müşteri Soyadı : " + müsteriSoyadi)
print("Müşteri İsim Soyisim : " + müsteriIsimSoyisim)
print("Müşteri cinsiyeti : " + müsteriCinsiyet)
print("Müşteri Tc kimlik numarası: " + müsteriTcKimlik)
print("Müşteri doğum yılı : " + str(müsteriDogumTarihi))
print("Müşteri adresi : " + müsteriAdresi)
print("Müşteri Yaşı : " + str(müsteriYasi))

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""

siparis1 = 110
siparis2 = 1100
siparis3 = 356
siparisSayisi = "3"
print("Marketimize hoşgeldiniz aşağıda verdiğiniz siparişler hakkında bilgiler vardır.")
print("Sipariş adedi : ",siparisSayisi)
print("Verdiğiniz siparişlerin toplam fiyatı : ", siparis1+siparis2+siparis3)

#Alttaki üstte yaptığım hatayı sorduğum kişinin verdiği cevap ikiside alternatifler

siparis1 = 110
siparis2 = 1100
siparis3 = 356
siparisSayisi = "3"
print("Marketimize hoşgeldiniz aşağıda verdiğiniz siparişler hakkında bilgiler vardır.")
print(f"Sipariş adedi : {siparisSayisi}")
print(f"Verdiğiniz siparişlerin toplam fiyatı : {siparis1+siparis2+siparis3}")