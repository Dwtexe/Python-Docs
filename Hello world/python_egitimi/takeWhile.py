import itertools
import operator


#TAKEWHILE FONKSİYONU ( ÜRKEK BİR ARKADAŞ )

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3]

sonuc = itertools.takewhile(lambda x: x<5, sayilar)

for i in sonuc:
    print(i)
