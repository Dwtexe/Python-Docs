import itertools
import operator

# RENK SEÇİM UYGULAMASI
renkler = ["Kırmızı", "Mavi", "Sarı" ,"Yeşil", "Mor"]
secimler = []

for renk in renkler:
    secim = input(renk + " rengini ister misiniz? (E / H) ")

    if secim == "E":
        secimler.append(True)
    else:
        secimler.append(False)

sonuc = itertools.compress(renkler, secimler)

print("\nSeçtğiniz renkler: \n")
for i in sonuc:
    print(i)
