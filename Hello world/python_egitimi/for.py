Pythonda Döngüler
Pythonda kullanabileceğimiz 2 tane döngü tipi vardır. Bunlar; for ve while döngüleridir.

Pythonda Döngü Nedir ve Döngüler ile Neler Yapabiliriz ?
Örneğin ekrana 10 tane "Merhaba" yazmak istersek yapmamız gereken 10 tane print("Merhaba") yazmak. Ancak sayıyı arttırıp 1000 demiş olsak bu eminim zor olacaktır. Dolayısıyla tekrarlayan bu gibi işlemleri kolaylıkla döngüler yardımıyla yapabiliriz.

Örneğin bir koşul gerçekleşene kadar tekrar eden bir kod yapısını düşünelim. Örneğin, kullanıcıdan istediğimiz bir parola bilgisinin en az 7 karakter olma şartını sağlayana kadar tekrar tekrar parola giriniz şeklinde mesaj yazdırmak isteyebilirsiniz. Bu gibi durumlarda döngü kullanmamız gerekiyor.

Pythonda For Döngüleri
Python for döngülerini bir eleman grubundaki (list, tuple, dictionary, set ya da string) her bir elemana ulaşmak için kullanırız.

Python List
Python list verileri üzerinde for döngüsü ile her bir elemana ulaşabiliriz.

Örnek
sayilar = [1,2,3,4,5]
for sayi in sayilar:
   print(sayi)
for döngüsü ile sayilar listesi üzerindeki her bir elemana ulaşarak sayi değişkeni içerisine kopyalıyoruz ve ulaştığımız her bir sayı print(sayi) ile ekrana yazdırılır.

Ekran çıktısı;

1
2
3
4
5
Örnek

isimler = ['çınar','sadık','sena']
for isim in isimler:
    print(f'my name is {isim}')
for döngüsü ile isimler listesi üzerindeki her bir elemana ulaşarak isim değişkeni içerisine kopyalıyoruz ve ulaştığımız her bir string değer print(isim) ile ekrana yazdırılır.

Ekran çıktısı;

my name is {çınar}
my name is {sadık}
my name is {sena}
Örnek
tuple = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)
list içerisinde tuple verilere ulaştığımızda her bir değer a ve b değişkenlerine sırayla kopyalanır.

Ekran çıktısı;

1 2
1 3
3 5
5 7
Python String
String bir veri bir karakter dizisidir ve string içindeki her bir karaktere ulaşmak için for döngüsünü kullanırız.

Örnek
name = 'Ali'
for n in name:
    print(n)
Ekran çıktısı;

A
l
i
Python Dictionary
Python dictionary verileri üzerinde for döngüsü ile her bir elemanın key ve value bilgilerini alabiliriz. 

Örnek
d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(key, value)
Ekran çıktısı;

k1 1
k2 2
k3 3
Range Fonksiyonu
Peki belli sayıdaki tekrarlayan işlemleri for döngüsü ile nasıl yapacağız ?

Örnek
sayilar = [1,2,3,4,5]
for sayi in sayilar:
   print('Merhaba')
Bu şekilde ekrana 5 kere Merhaba yazdırmak istiyorsak ve elimizde 5 elemanlı bir liste varsa işimizi hallederiz ancak 5 kere değil 5000 kere yazdırmak istersek bu durumda 5000 elemanlı bir listeyi nereden bulacağız ? 

İşte burada range fonksiyonu imdadımıza yetişir ve istediğimiz eleman sayısına sahip bir listeyi bize hazırlar.

Range fonksiyonu ile for döngüsünün dönme sayısı kadar tekrarlayan işlemler yapabiliriz. 

result = list(range(5))
print(result) # [0,1,2,3,4]
Gördüğünüz gibi range(5) dediğimizde bizim için bir object üretilir ve biz bu objeyi list() ile listeye çevirdiğimizde elimize [0,1,2,3,4] listesi gelir. Peki bunu for döngüsünde kullanalım.

Örnek
for i in range(5):
   print(i)
Bu şekilde ekrana 0-5 arasındaki tüm sayılar yazdırılır. 5 dahil değil.

Dolayısıyla 5 defa ekrana Merhaba yazdırmak oldukça kolay hale geldi.

Örnek
for i in range(5):
   print('Merhaba')
Peki 50-100 arasında bir liste üretmek istersek ?

Örnek
for i in range(50,100):
   print(i)
50-100 arasındaki sayılar ekrana yazdırılır.

Peki 50-100 arasında 2 şer 2 şer sayıları yazdırmak istersek ?

for i in range(50,100,2):
   print(i)
50-100 arasındaki sayılar 2 şer 2 şer ekrana yazdırılır. (50,52,54...98)

Python For Döngüsü Uygulamaları
sayilar = [1,3,5,7,9,12,19,21]

1- Sayilar listesindeki hangi sayılar 3' ün katıdır ?

for sayi in sayilar:
   if (sayi%3==0):
       print(sayi)
2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam = 0
for sayi in sayilar:
    toplam += sayi
print('toplam:',toplam)
3- Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
   if (sayi % 2 == 1):
      print(sayi ** 2)
4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for sehir in sehirler:
   if (len(sehir) <= 5):
      print(sehir)
5- Ürünlerin fiyatları toplamı nedir ?

urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]
toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('toplma ürün fiyatı: ', toplam)
6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
  if (int(urun['price']) <= 5000):
     print(urun['name'])s