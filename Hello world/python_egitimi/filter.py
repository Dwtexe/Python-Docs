def tek(sayi):
    return sayi%2 ==1

liste = range(1,20)

a = list(filter(tek,liste))    # fonksiyonun çıktısı True ise 'a' listesine sonuç eklenir.
print(a)