Python Dictionary
Python collection veri tiplerinden olan dictionary yani sözlük veri yapısı key ve value şeklinde verileri saklayabileceğimiz bir veri yapısıdır. Dictionary veri yapısı Json veri yapısına oldukça benzerdir.

Dictionary liste elemanlarına key ve value değerlerine göre ulaşıp elemanlar üzerinde güncelleme yapabiliriz. (araç plakası ve il bilgisi gibi. {41: "Kocaeli"})

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

print(ogrenci)  # { "numara": "120", "ad": "Ahmet", "soyad": "Yılmaz" }
Gördüğünüz tek bir sözlük objesi içinde bir öğrencinin numara, ad ve soyad bilgisini taşıyabiliyoruz.

Sözlük veri yapısını kullanmadan tanımlayacağımız iki farklı bilgiyi ayrı ayrı listeler içerisinde tutabiliriz.

Örnek
sehirler = ['kocaeli','istanbul']
plakalar = [41, 34]
Eğer ki; istanbul' un plaka kodunu almak istersek şu şekilde yapabiliriz;

Örnek
print(plakalar[sehirler.index('istanbul')]) # 34
sehirler.index('istanbul') ile istanbul' un liste içindeki konumunu bulup o konum bilgisi ile (indeks) diğer listeden 34 bilgisini alabiliriz.

Burada 2 farklı liste tanımlamak yerine tek bir sözlük veri yapısı tanımlamış olsak işimiz çok daha kolay olur.

Örnek
plakalar = { 'kocaeli' : 41, 'istanbul': 34 }
print(plakalar['kocaeli'])   # 41
print(plakalar['istanbul'])  # 34
Dictionary Elemanlarına Erişim
Dictionary elemanlarının value bilgisine köşeli parantezler içerisine yazdığımız key ile ulaşabiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

print(ogrenci["numara"]) # 120
print(ogrenci["ad"])     # Ahmet
print(ogrenci["soyad"])  # Yılmaz
Ayrıca köşeli parantez yerine get() metodunuda kullanabiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

numara = ogrenci.get("numara")
ad = ogrenci.get("ad")
soyad = ogrenci.get("soyad")

print(numara,ad,soyad)  # 120 Ahmet Yılmaz
Dictionary Elemanlarına Döngü ile Erişim
Sözlük veri yapısında her bir eleman key ve value birleşiminden oluştuğundan dolayı key mi, value mu yoksa her ikisini de almak mı istiyorsunuz ?

Örnek
user = {
      username = "sadikturan",
      password = "123456",
      email = "info@sadikturan.com",
      phone = "05320000000"
}

for i in user:
   print(i)
username, password, email, phone bilgileri alt alta key bilgileri gelecektir.

Eğer ki, value bilgilerini almak istiyorsak user[i] şeklinde her bir elemanın value bilgisine ulaşmalıyız.

Örnek
for i in user:
   print(user[i])
Bu durumda ekran çıktısı olarak "sadikturan 123456 info@sadikturan.com 05320000000" bilgileri alt alta gelir.

Ya da aynı şekilde value bilgilerine aşağıdaki gibi de values() ile de ulaşabiliriz.

Örnek
for i in user.values():
   print(i)
items()  metodu ile hem key hem de value bilgilerine ulaşabiliriz.

Örnek
for a,b in user.items():
   print(a,b)
Bu durumda ekran çıktısı olarak key ve value bilgileri aynı anda a ve b değişkenleri içerisine sırasıyla kopyalanır.

username sadikturan

password 123456

email info@sadikturan.com

phone 05320000000

Dictionary Elemanlarını Güncelleme
key bilgisi ile ulaştığınız bir elemanın value değerini değiştirebiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

ogrenci["numara" ] = 220
print(ogrenci)  # { "numara": "220", "ad": "Ahmet", "soyad": "Yılmaz" }
Dictionary' e Yeni Eleman Ekleme
Yeni bir eleman eklemek için olmayan bir key bilgisi eklememiz yeterlidir.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

ogrenci["cinsiyet"] = "E"
print(ogrenci) # { "numara": "220", "ad": "Ahmet", "soyad": "Yılmaz" ,"cinsiyet":"E"}
Dictionary' den Eleman Silme
pop() metodu ile sözlük veri yapısından belirttiğimiz key bilgisi ile veriyi silebiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

ogrenci.pop("numara")
print(ogrenci) # { "ad": "Ahmet", "soyad": "Yılmaz"}
Aynı şekilde del komutunu kullanarak da istediğimiz key bilgisiyle veri silebiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

del ogrenci["numara"]
print(ogrenci) # { "ad": "Ahmet", "soyad": "Yılmaz"}
del komutu ile key bilgisi vermeden dictionary objesini bellekten silebiliriz. 

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

del ogrenci
print(ogrenci) # NameError: name 'ogrenci' is not defined
Sildikten sonra ogrenci objesine ulaşmak istediğimizde NameError alırız çünkü ogrenci objesi bellekte yer almak.

Eğer ki dictionary elemanlarının hersini silmek istiyorsak clear() metodunu kullanabiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

ogrenci.clear()
print(ogrenci) # { }
Sildikten sonra ogrenci objesine ulaşmak istediğimizde boş obje tanımlaması ile karşılaşırız. ({ })

Sözlük verisinin son elemanını silmek için popitem() metodunu kullanabiliriz.

Örnek
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

ogrenci.popitem()
print(ogrenci) # { "numara": "120", "ad": "Ahmet"}
İç içe Dictionary Tanımlama
Tanımlanan bir sözlük verisini bir başka liste elemanı içerisine alabileceğimiz gibi bir başka sözlük veri yapısı içine de alabiliriz.

Örnek
users = {
    'sadikturan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

Burada users objesinin 2 elemanı mevcuttur. 

Örnek
print(users['cinarturan'])
Ekran çıktısı;

{ 'age': 2, 'roles': ['admin','user'], 'email': 'cinar@gmail.com', 'address': 'kocaeli', 'phone': '1231321' } 

Gördüğümüz gibi 'cinarturan' ya da 'sadikturan' ile içteki her bir sözlük verisine ulaşabiliriz ve ulaştığımız 2 sözlük veri yapısı içinde de diğer elemanlara ulaşmak için ise;

Örnek
print(users['cinarturan']['age'])
Bu durumda ekran çıktısı olarak 2 bilgisini alırız.

Ya da;

Örnek
print(users['cinarturan']['roles'])
Dediğimizde ise ['admin', 'user'] bilgisi karşımıza gelecektir.

Python Dictionary Uygulaması
ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

** Henüz döngüleri görmediğimizden dolayı input() ile bilgi alma işlemini 3 öğrenci için tekrarlayabilirsiniz.

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
