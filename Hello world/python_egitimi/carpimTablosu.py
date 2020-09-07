# ÇARPIM TABLOSU UYGULAMASI

def carpimTablosu():
    for i in range(1,11):
        for k in range(1,11):
            yield str(i) + "x" + str(k) + "=" + str(i*k)

carp = iter(carpimTablosu())

for i in carpimTablosu():
    print(i)