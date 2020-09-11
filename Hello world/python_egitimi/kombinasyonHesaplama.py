import itertools
import operator


# KOMBİNASYON HESAPLAMA UYGULAMASI
adet = input("Kombinasyonda kaç adet değer olacak?")
sayi = input("Kaçlı olarak kombinasyon yapacağız?")

liste = []

for i in range(1, int(adet) + 1):
    liste.append(i)

print("Kombinasyon oluşturuluyor... \n")

kombin = itertools.combinations(liste,int(sayi))

kListe = list(kombin)

for i in kListe:
    print(i)

print(adet, ",", sayi, "kombinasyonu:", len(kListe), "adettir ve yukarıda listelenmiştir.")

