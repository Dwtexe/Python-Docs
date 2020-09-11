import itertools
import operator

# CHAİN FONKSİYONU

renkler = ["kırmızı", "mavi", "sarı" ,"yeşil", "mor"]
sekiller = ["kare", "dikdörtgen", "daire", "üçgen"]

zincir = itertools.chain(renkler, sekiller)

for i in zincir:
    print(i)
