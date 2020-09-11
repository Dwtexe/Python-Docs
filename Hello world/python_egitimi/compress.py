import itertools
import operator


# COMPRESS FONKSİYONU

renkler = ["kırmızı", "mavi", "sarı" ,"yeşil", "mor"]
secimler = [True, False, False, True, False]

sonuc = itertools.compress(renkler, secimler)

for i in sonuc:
    print(i)