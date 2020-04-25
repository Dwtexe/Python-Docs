Pythonda Koşul İfadeleri
Pythonda koşul durumlar ile bir koşuldan elde ettiğimiz True ya da False değere göre programın farklı yönlerden ilerlemesini sağlayabiliriz.

Örneğin; kullanıcıdan aldığımız bir parolanın ya da email adresinin doğru olup olmadığını kontrol ederek 'uygulamaya giriş yapıldı' ya da 'parolanız yanlış' şeklinde mesajlar verebiliriz.

Ya da 3 sayıdan hangisi büyüktür şeklinde bir karşılaştırmayı kolaylıkla yapıp geriye True ya da False değer döndürmek yerine "en büyük sayı budur" şeklinde mesaj verebileceğiz.

Pythonda If Bloğu
Bir koşulun True ya da False olan sonucuna göre farklı kod blokları oluşturmak için If komutunu kullanırız.

Aşağıda bazı koşul ifadeleri verilmiştir. Bu koşullar bize True ya da False değer üretirler.

Eşit mi : a == b,

Eşit değil mi: a != b

Küçük mü : a < b

Küçük ya da eşit mi: a <= b

Büyük mü: a > b

Büyük ya da eşit mi: a >= b

Örnek
a = 10
b = 20
if b > a:
  print("b, a'dan büyüktür")
Gördüğünüz gibi (b>a) şeklinde oluşturduğumuz koşul bize True değeri üretirse ekrana 'b, a'dan büyüktür' mesajı yazdırılacaktır. Eğer False değer üretilirse ekrana bir şey yazdırılmaz.

** if koşulunun sonuna eklediğimiz iki nokta (:) ile if bloğu oluşturmuş oluyoruz ve sonraki satır mutlaka içeriden başlaması gerekir aksi halde 'IndentationError: expected an indented block' şeklinde bir hata alırız.

Pythonda Elif Bloğu
Bazen birden fazla koşul yazmak isteriz bu durumda eğer ilk if bloğundaki koşul False değer üretirse Elif bloğunda tanımladığımız koşula bakılır.

Örnek
a = 10
b = 10
if b > a:
  print("b, a'dan büyüktür")
elif a == b:
  print("a ile b eşittir")
a ile b eşit olduğundan dolayı if bloğu False değer üretir dolayısıyla sonraki koşul olan elif koşuluna geçilir ve buradaki koşul bize True değer ürettiğinden dolayı ekrana 'a ile b eşittir' mesajı yazdırılır.

elif komutuyla istediğimiz kadar koşul eklemeye devam edebiliriz.

Örnek
a = 15
b = 10
if b > a:
  print("b, a'dan büyüktür")
elif a == b:
  print("a ile b eşittir")
elif a > b:
  print("a, b'den büyüktür")
Burada ise en sondaki elif bloğunda sorduğumuz (a>b) koşulu doğru olduğundan ekrana sadece "a, b'den büyüktür" mesajı yazdırılır.

Pythonda Else Bloğu
Else ve Elif bloklarındaki koşullardan her hangi biri True değilse bir Else bloğu oluşturup Else bloğundaki kodların çalıştırılmasını sağlayabiliriz.

Örnek
a = 15
b = 10
if b > a:
  print("b, a'dan büyüktür")
elif a == b:
  print("a ile b eşittir")
else:
  print("a, b'den büyüktür")
a, b' den büyük olduğu için ilk 2 koşul False üretir ve else bloğu çalıştırılır.

Zaten b, a' dan büyük değil ya da a, b'e eşit değilse bu durumda tekrar (a>b) diye sormamızın anlamı yok ve else bloğuna koşul eklemeden gerekli mesajı yazdırabiliriz.

Örnek
num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')
Kullanıcıdan aldığımız bir sayının pozitif, negatif ya da sıfır olup olmadığını kontrol edebiliriz.

Pythonda Nesned If Blokları
Bir if bloğu içerisinde başka bir if bloğunu başlatabiliriz.

username = 'sadikturan'
password = '1234'

if (username == 'sadikturan'):
    if (password == '12345'):
        print('Hoş geldiniz')
    else:
        print('parola yanlış')        
else:
    print('username yanlış')
Burada iç içe 2 tane if bloğu kullanılmıştır. Eğer ki kullanıcının girdiği username bilgisi doğru değilse ekrana 'username yanlış' mesajı yazdırılacaktır. Ancak username doğru ise bu durumda içteki diğer if bloğundaki koşul kontrol edilecektir. 

İçteki koşulda ise password bilgisi doğruysa 'Hoş geldiniz' yanlış ise 'parola yanlış' mesaj yazdırılacaktır.

Koşul İfadelerinde And ve Or Operatörleri
Koşul ifadelerinde and ve or operatörleri yardımıyla birden fazla durumu aynı anda kontrol edebiliriz.

if (username == 'sadikturan') and (password == '12345'):
        print('Hoş geldiniz')      
else:
    print('username ya da parola yanlış')
username ve parolanın aynı anda doğru oldu durumlarda 'Hoş geldiniz' yanlış olduğu durumda ise 'username ya da parola yanlış' mesajını yazdırabiliriz.

Bir sonraki dersimizde ise pythonda koşullu ifadeler örneklerimizi yapalım.

