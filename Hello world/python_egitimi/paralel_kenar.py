cap = int(input("Paralel kenar büyüklüğü (çift sayı giriniz) "))

def sagSlas(adet):
    for i in range(int(adet)):
        print("/", end="")

def solSlas(adet):
        for i in range(int(adet)):
           print("\\", end="")

def satirAtla(adet):
        for i in range(int(adet)):
                print()

def bosluk(adet):
        for i in range(int(adet)):
                print(" ", end="")

def araCizgi(cap):
    cizgi = "-"
    print(cizgi*int(cap/2),end="")
    dikeyCizgi(1)
    print(cizgi*int(cap/2),end="")
    satirAtla(1)

def dikeyCizgi(sayi):
        dikey = "|"
        print(dikey,end="")


def ustKisim(cap):
    baslangicBosluk = cap / 2-1
    for i in range(int(cap/2)):
        bosluk(baslangicBosluk-i)
        sagSlas(1)
        bosluk(i)
        dikeyCizgi(1)
        bosluk(i)
        solSlas(1)
        satirAtla(1)

def altKisim(cap):
        baslangicBosluk = cap-2
        for i in range(int(cap/2)):
                bosluk(i)
                solSlas(1)
                bosluk((baslangicBosluk - i*2)/2)
                dikeyCizgi(1)
                bosluk((baslangicBosluk - i*2)/2)
                sagSlas(1)
                satirAtla(1)


def paralelKenar(cap):
        ustKisim(cap)
        araCizgi(cap)
        altKisim(cap)

paralelKenar(cap)