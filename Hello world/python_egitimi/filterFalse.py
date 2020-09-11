import itertools
import operator

# FİLTERFALSE FONKSİYONU

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3]

sonuc = itertools.filterfalse(lambda x: x<5, sayilar)

for i in sonuc:
    print(i)

