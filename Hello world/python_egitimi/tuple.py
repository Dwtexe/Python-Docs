'''
    Artık özet yazmaya üşeniyorum 2 saat sürüyor bir ders.
'''



Python Tuple
Pythonda tuple listeleri, list' e benzer ancak farkı tuple içindeki elemanlar değiştirilemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.

Örnek
tuple = ("banana", "grape", "cherry")
print(tuple)  # ("banana", "grape", "cherry")
Tuple liste elemanları, parantez ile oluşturulur. Ayrıca parantez kullanmadan da tuple listesi oluşturmuş oluruz ancak okunabilirlik açısından parantez kullanabiliriz.

Tuple Liste Elemanlarını Güncelleme
Tuple liste elemanları değiştirilemez ancak başka bir liste türüne çevrilerek güncelleme yapılabilir.

Örnek
a = ("banana", "grape", "cherry")
b = list(a)
b[0] = "apple"
a = tuple(b)

print(a)  # ("apple", "grape", "cherry")
Burada a ismindeki tuple listesini önce list() metodu ile list objesine çevirip güncellemeyi yapıyoruz ve sonrasında güncellenmiş listeyi tekrar tuple() metodu ile tuple objesine çeviriyoruz.

Tuple Elemanlarına Erişim 
Python tuple listelerindeki her bir elemanına soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz. Aynı şekilde sağdan -1. indeks numarasından başlamalıyız.

Örnek
message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan')

print(message[2])   # My
print(message[4])   # is
print(message[-1])  # Turan
print(message[-3])  # is
Tuple listesinden bir aralık seçmek istediğimizde ise slicing yöntemini kullanabiliriz.

Örnek
message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan')
print(message[0:2])  # ('Hello', 'There.')
0 ve 2. indeks aralığında elemanlar seçilir ve geriye bir tuple listesi döner.

Sıfırdan başladığımızdan dolayı 0 değerini vermemiş olsak bile aynı sonucu alırız.

Örnek
message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan')
print(message[:2])  # ('Hello', 'There.')
Burada [:2] diyerek baştan başla ancak 2. indekse kadar git demiş oluyoruz.

Ayrıca negatif indekslemeyi kullanarak da elemanlara ulaşabiliriz. Listenin en son elamanı -1. indekse karşılık gelirken sola doğru -2,-3 şeklinde ilerlemiş oluruz.

Örnek
message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan')
print(message[-3:-1])  # ('is', 'Sadık')
Tuple Elemanlarına Döngü ile Erişim
Tuple elamanlarına indeks numaraları ile nasıl erişebileceğimizi öğrendik ancak her bir elemana indeks numarası ile tek tek ulaşmak bazen zor olabilir dolayısıyla liste elemanlarına bazen döngü ile ulaşmak isteriz.

Örnek
names = ('ahmet','mehmet','cenk')
for name in names:
   print(name)
Tuple Metotları
Python tuple ile kullanabileceğimiz 2 tane metot vardır. Bunlar count() ve index() metotlarıdır.

Bir tuple içerisindeki tekrarlayan elemanların sayısını almak için count() metodunu kullanırız.

Örnek
numbers = (1, 10, 5, 16, 4, 9, 10)
letters = ('a', 'g', 's', 'b', 'y', 'a', 's')
numbers.count(10)  # 2
letters.count('a') # 2
Bir tuple içerisinde bir elemanın index numarasını almak için index() metodu kullanılır.

Örnek
numbers = (1, 10, 5, 16, 4, 9, 10)
numbers.index(10) # 1
10 elemanının tuple içindeki index numarası 1' dir.