




"""

    Bu dersi dinlemye üşendim ileride bu derse ihtiyacım olursa düzenlerim...

"""














Python Collections (Arrays)
Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.

List, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Tuple, elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.

Pythonda Liste
String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanıdır ve her bir elemana indeks numarası ile ulaşabiliriz.

Gene aynı mantıkla list veri tipinde ise tek bir karakter yerine farklı veri tiplerindeki bilgileri gruplayabiliyoruz. Karakter dizilerinde (string) olduğu gibi her bir eleman indekslenebilir.

Örnek
message = 'Hello There. My name is Sadık Turan'.split()
print(message)    # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[0]) # Hello
message ismindeki bir karakter dizisini (string) split() metodu ile bir listeye çevirebiliriz ve listenin 0.indeksindeki elemanı ekrana yazdırırsak karşımıza 'Hello' ifadesi gelir. Çünkü artık elimizde bir list mevcuttur.

Liste Tanımlama
Liste elemanlarından her biri farklı veri tipinde olabilir.

Örnek
list1 = [1,2,3]
list2 = ['bir',2, True, 5.6]
Birinci liste elemanlarının hepsi aynı veri tipindeyken ikinci liste elemanları farklı veri tipinde tanımlanabilir dolayısıyla Python listeleri homojen bir yapıda olmayabilir.,

İki farklı listeyi bir liste içinde gruplayabiliriz.

Örnek
list1 = ['one','two','there']
list2 = ['four','five','six']

numbers = list1 + list2 # ['one','two','there','four','five','six']
Liste içinde farklı listelerde tanımlayabiliriz.

list1 = [[1,2,3],[4,5,6],[7,8,9],10]
Bu durumda list1 içinde 4 eleman var diyebiliriz ilk 3 eleman bir liste 4.eleman ise number türünde bir değer.

Örnek
kullaniciA = ['Sadık', 36]
kullaniciB = ['Çınar', 2]

kullanicilar = [kullaniciA,kullaniciB]
Burada ise ilk olarak her bir kullanici bilgisini ayrı bir liste de tanımlayıp sonrasında kullanicilar isminde bir liste içinde gruplama yapabiliriz.

Listelerde Eleman Sayısı
Python listelerinde eleman sayısını len() metodu ile öğrenebiliriz. Aynı metodu string içinde kullanıp karakter sayısını öğrenebiliriz.

Örnek
list1 = ['one','two','there']
list2 = [[1,2,3],[4,5,6],[7,8,9],10]

print(len(list1)) # 3
print(len(list2)) # 4
Liste Elemanlarına Erişim
Python listelerindeki her bir elemanına soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz. Aynı şekilde sağdan -1. indeks numarasından başlamalıyız.

Örnek
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']

print(message[2])   # My
print(message[4])   # is
print(message[-1])  # Turan
print(message[-3])  # is
Aynı şekilde liste içinde bir başka liste tanımladığımızda ise alt liste elemanı içinde [ ] kullanmamız gerekir. 

Örnek
liste = [[1,2,3],[4,5,6],[7,8,9],10]

print(liste[0])     # [1,2,3]
print(liste[1][2])  # 6
Örnek
names = ['ahmet','mehmet','cenk']
surnames = ['yılmaz','turan','durmuş']

result = names[0] +' '+ surnames[0]  # ahmet yılmaz
result = names[1] +' '+ surnames[1]  # mehmet turan
Liste Elemanlarına Döngü ile Erişim
Liste elamanlarına indeks numaraları ile nasıl erişebileceğimizi öğrendik ancak her bir elemana indeks numarası ile tek tek ulaşmak bazen zor olabilir dolayısıyla liste elemanlarına bazen döngü ile ulaşmak isteriz.

names = ['ahmet','mehmet','cenk']
for name in names:
   print(name)
Burada 3 elemanlı names listesi içindeki her bir eleman sırasıyla name değişkeni içerisine kopyalanır ve print() metodu ile ekrana yazdırılır. 

** Döngü kullanımını ilerleyen derslerimizde göreceğiz.

Liste Parçalama
Listeden tek bir eleman seçmek yerine bir aralık belirtip eleman grubunu seçebiliriz.

Örnek
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[0:2])  # ['Hello', 'There.']
0 ve 2. indeks aralığında elemanlar seçilir ancak 0.indeks dahil 2.indeks dahil değildir.

Sıfırdan başladığımızdan dolayı 0 değerini vermemiş olsak bile aynı sonucu alırız.

Örnek
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[:2])  # ['Hello', 'There.']
Burada [:2] diyerek baştan başla ancak 2. indekse kadar git demiş oluyoruz.

Örnek
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[2:])  # ['My', 'name', 'is', 'Sadık', 'Turan']
Burada ise [2:] diyerek 2.indeksten başla (başlangıç indeksi dahil) ve sona kadar git demiş oluyoruz.

Örnek
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[-3:-1])  # ['is', 'Sadık']
Burada ise -3. indeksten başla (dahil) ve -1. indekse (dahil değil) kadar git demiş oluyoruz.

message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[::])  #  ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
[::] diyerek tüm listeyi seçmiş oluyoruz.

Liste Elemanlarını Güncelleme
Liste elemanlarını güncellemek istediğimizde ilk olarak elemanı seçmemiz gerekiyor.

list1 = ['one','two','there']
list1[1] = 'updated'
print(list1)  # ['one','updated','there']
1.indeksteki elemanı seçip 'updated' bilgisiyle güncelliyoruz.

Python Liste Örnekleri
1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['Bmw','Mercedes','Opel','Mazda']
2- Liste Kaç elemanlıdır ?

result = len(arabalar)  # result = 4
3- Listenin ilk ve son elemanı nedir ?

result = arabalar[0]
result = arabalar[3]
result = arabalar[-1] # tersten -1. indeks en son elemana karşılık gelir.
4- Mazda değerini Toyota ile değiştirin.

arabalar[-1]= 'Toyota'
5- Mercedes listenin bir elemanı mıdır ?

result = 'Mercedes' in arabalar
print(result) # True
6- Listenin -2 indeksindeki değer nedir ?

result = arabalar[-2] 
print(result) # Opel
7- Listenin ilk 3 elemanını alın.

result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]
8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

arabalar[-2:] = ['Toyota','Renault']
9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

result = arabalar + ['Audi','Nissan']
10- Listenin son elemanını silin.

del arabalar[-1]
11- Liste elemanlarını tersten yazdırınız.

result = arabalar[::-1]
12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA: Yiğit Bilgi 2010, (70,60,70)

# studentB: Sena Turan 1999, (80,80,70)

# studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)