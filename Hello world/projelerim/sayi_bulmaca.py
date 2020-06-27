import random

print("Sayı tahmin etme oyununa hoşgeldiniz...\nOyunda yapmanız gereken tek şey 1-10 arasında aklımdan tutuğum sayıyı bilmek.\n")

sayi = random.randint(1,10)
can = int(input('Kaç hakkınız olsun istersiniz :'))
hak = can
sayac = 0

while hak >0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahminin nedir? :'))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. denemede bildiniz.\n Toplam puanınız: {100 - (100/can) * (sayac - 1)}\nTekrar oynayalım mı? :)')
        break
    elif sayi > tahmin:
        print('Daha büyük bir sayı tuttum.')
    else:
        print('Daha küçük bir sayı tuttum.')

    if hak == 0:
        print(f'Hakkın bitti...\nAklımdan tuttuğum sayı {sayi}\nTekrar deneyecek cesaretin var mı?')