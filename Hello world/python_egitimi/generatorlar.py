
#GENERATOR OLAYI

def semt():
    print ("Kapı çalınıyor...")
    yield "Ahmet"

    print("Kapı çalınıyor...")
    yield "Mahmut"

    print("Kapı çalınıyor...")
    yield "Ömer"

    print("Kapı çalınıyor...")
    yield "Faruk"

    print("Kapı çalınıyor...")
    yield "Hasan"

    print("Kapı çalınıyor...")
    yield "Mustafa"

huzur = semt()
ziyaret = iter(huzur)
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))

ziyaret2 = iter(huzur)
print(next(ziyaret2))  # DEMEK Kİ GENERATOR SADECE BİR KEZ ÜRETİP KAYBOLUYOR


def semt2():
    liste = ["ahmet","mahmut","ömer","faruk","hasan","mustafa"]
    for i in liste:
        print ("Kapı çalınıyor")
        yield i

for i in semt2(): # ARTIK ITERABLE OLDUĞUNA GÖRE FOR DÖNGÜSÜ KULLANABİLİRİZ
    print (i)


def kare():
    for i in range(1,20):
        yield i**2

generator = kare()

print(generator)

kareal = iter(generator)

print(next(kareal))
print(next(kareal))
print(next(kareal))
