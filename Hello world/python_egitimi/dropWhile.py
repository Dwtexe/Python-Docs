import itertools
import operator



# DROPWHILE FONKSİYONU ( ÇOK KARAMSAR BİR ARKADAŞ :) )

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3]

sonuc = itertools.dropwhile(lambda x: x<5, sayilar)

for i in sonuc:
    print(i)

def bestenBuyuk(x):
    return x > 5

sonuc = itertools.dropwhile(bestenBuyuk, sayilar)

for i in sonuc:
    print(i)
