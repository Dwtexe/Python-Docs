Pythonda While Döngüsü
While döngülerinde belirttiğimiz bir koşul doğru olduğu sürece while bloğu içerisinde tanımladığımız kod satırlarını tekrarlatabiliriz.

Örnek
i = 1
while i < 5:
  print(i)
  i += 1
Ekran Çıktısı:

1
2
3
4
Belirttiğimiz koşul i' nin 5 den küçük olması ve bu koşul devam ettiği sürece (True) ekrana i değeri yazdırılmaya devam eder. Ancak burada dikkat etmemiz gereken her adımda i değerini değiştirmemiz gerektiği aksi halde sonsuz bir döngüye gireriz.

Dolayısıyla i değeri ekrana yazdırıldıktan sonra i' nin değerini 1 arttırmamız gerekiyor. i' nin değeri 5' e eşit olduğunda while koşulu bize False değer döndürür ve döngüden çıkılır.

Örnek
x = 1
while x <= 100:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1

print('bitti...')
x değerini 1 den başlatırız ve 100' den küçük mü kontrol ederiz. x, 100' den küçük olduğu sürece while bloğundaki kodlar işletilir ve her adımda x' i 1 arttırırız ki sonsuz döngüye girmeyelim. 

Her adımda x%2==1 mi diye kontrol ediyoruz eğer bu ifade bize True bilgisi getirirse demek ki sayı tek olduğundan sayı tek aksi halde sayı çift mesajını yazdırıyoruz. Özetle 1-100 arasındaki her sayı için tek ya da çift mesajlarını yazdırmış oluyoruz. En sonda ise bitti mesajı bir kere yazdırılır çünkü while döngüsünün dışında.

Break ve Continue 
break komutu döngüyü sonlandırır, continue ise döngünün o turunu sonlandırır ve bir sonraki turdan devam eder.

Örnek
x = 0
while x < 5:    
   x+=1
   if x == 2:
       continue
   print(x)
x, 5' den küçük olduğu sürece ekrana yazdırılır ancak x' in 2 olduğu turda continue komutu çalışınca x ekrana yazdırılmaz ancak döngü sonraki turdan devam eder.

Ekran çıktısı;

1
3
4
Peki aynı örnekte continue yerine break yazarsak ne olur ?

Örnek
x = 0
while x < 5:    
   x+=1
   if x == 2:
       break
   print(x)
x, 5' den küçük olduğu sürece ekrana yazdırılır ancak x' in 2 olduğu turda break komutu çalışınca döngü biter ve ekrana sadece 1 yazdırılır.

Ekran çıktısı;

1

Örnek
1- 100 e kadar tek sayıların toplamını hesaplayalım.

x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'toplam: {result}')
x%2==0, True değer döndürdüğünde sayının çift olduğunu anlarız ve continue ile x değerini result içerisine eklemeyiz ancak sonraki turdan devam ederiz.

Python While Döngü Örnekleri
sayilar = [1,3,5,7,9,12,19,21]

1- Sayilar listesini while ile ekrana yazdırınız.

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırınız.

baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangic

while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)
3- 1-100 arasındaki sayıları azalan şekilde yazdırınız.

i = 100
while i > 0:
    print(i)
    i -= 1
4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.

numbers = []
i = 0
while i<5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.

   ** ürün sayısını kullanıcıya sorun.

   ** dictionary listesi yapısı (name, price) şeklinde olsun.

   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')