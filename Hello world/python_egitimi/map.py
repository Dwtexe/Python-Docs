def kare(sayi):
    return sayi*sayi


sayilar = range(1,10)
a = list(map(kare,sayilar)) # 1 den 10  a kadar olan tüm sayıları tek tek fonksiyona göndermek yerine map in içine yazıyoruz bu sayede hepsi teker teker gidiyor

#Bir diğer yöntem:
for i in sayilar:
    print(kare(i))
# Bu daha düzgün ama çok fazla karekterden oluştuğu için dosya boyutu artar
print(a)