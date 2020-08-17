def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi-1)

print(faktoriyel(4))

"""

Faktöriyel işlemi nedir

yukarda gerçekleşen işlem 4*3*2*1 = 24 = 4!

"""