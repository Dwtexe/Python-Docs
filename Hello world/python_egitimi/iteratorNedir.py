mahalle = ["ahmet"]


ziyaret = iter(mahalle)
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))

print("\nMeyveler:")
sepet = ["elma","armut","karpuz","portakal","muz"]

meyve = iter(sepet)
print(next(meyve))
print(next(meyve))
print(next(meyve))




for i in mahalle:
    print(i)

# FOR DÖNGÜSÜ ASLINDA NEDİR?
ziyaret = iter(mahalle)

while True:
    try:
        print(next(ziyaret))
    except StopIteration:
        break


# ITERATION -> ZİYARET ETMEK
# ITERATOR -> HERKESİ ZİYARET EDEN ARKADAŞ
# ITERABLE -> EVİ OLAN (ZİYARET EDİLEBİLEN) ARKADAŞLARIN MAHALLESİ

