import itertools
import operator

# STARMAP FONKSİYONU

def carp(sayi1, sayi2):
    return (str(sayi1) + " x " + str(sayi2) + " = " + str(sayi1*sayi2))

sayilar = [ (2,3), (3,5), (5,4) ]

sonuc = itertools.starmap(carp, sayilar)

for i in sonuc:
    print(i)