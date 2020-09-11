import itertools
import operator

# ACCUMULATE FONKSİYONU

veri = [1, 2, 3, 4, 5]

def topla(sayi1, sayi2):
    return sayi1 + sayi2

def carp(sayi1, sayi2):
    return sayi1 * sayi2

sonuc = itertools.accumulate(veri, carp)
# sonuc = itertools.accumulate(veri, operator.add)  Toplama Yapar
# sonuc = itertools.accumulate(veri, operator.mul)  Çarpma Yapar
# sonuc = itertools.accumulate(veri, operator.truediv)  Normal Bölme
# sonuc = itertools.accumulate(veri, operator.floordiv) Sadece Tam Sayılı Bölme

for i in sonuc:
    print(i)
