Python Operatörler
Pythonda operatörleri, aritmetik operatörler, atama operatörleri, karşılaştırma operatörleri ve mantıksal operatörler şeklinde gruplayabiliriz.

Aritmetik Operatörler
Pythonda aritmetik operatörleri matematiksel işlemler için kullanırız.

 	 	 	x = 20 y = 5	sonuc
+	Toplama	 	
sonuc = x + y

25
-	Çıkarma	 	
sonuc = x - y

15
*	Çarpma	 	
sonuc = x * y

100
/	Bölme	 	sonuc = x / y	4.0
%	Mod Alma	 	sonuc = y % x	0
//	Tam Bölme	 	sonuc = x // y	4
**	Üs alma	 	sonuc = 2 ** 3	8
Atama Operatörleri
Pythonda değişkenlere veri ataması yaparken atama operatörlerini kullanırız.

Operatör	Kısa kullanım	Uzun kullanım	 
 	x = 20 y = 5	 
=	x = y	
x = y

x= 5 

+=	x += y	
x = x + y

x= 25
-=	x -= y	
x = x - y

x= 15
*=	x *= y	
x = x * y

x= 100
/=	x /= y	x = x / y	x= 4.0
%=	x %= y 	x = x % y	x= 0
**=	x **= y	x = x ** 2	x= 400
//=	x //= y	x = x // y	x= 4
Karşılaştırma Operatörler
En basitiyle 2 değişkenin aldığı verileri karşılaştırmak için karşılaştırma operatörlerini kullanırız.

Operatör	Açıklama	
Kullanım

Sonuç
==	eşit mi ?	
10 == 10

True
 	5 == 4	False
 	
x = 5 y = 5

x == y

True
!=	eşit değil mi?	
10 != 9

True
 	10 != 10	False
>	Büyük mü ?	10 > 5	True
<	Küçük mü ?	10 < 5	False
>=	Büyük eşit mi ?	5 >= 5	True
<=	Küçük eşit mi ?	5 <= 5	True
Mantıksal Operatörler
Pythonda mantıksal operatörleri birden fazla koşulu beraberce değerlendirmek için kullanırız.

Örneğin; Ehliyet almak için en az lise mezunu olmak ve aynı zamanda yaş bilgisinin en az 18 olması gibi 2 koşulun aynı anda doğruluğunu mantıksal operatörler yardımıyla değerlendirebiliriz.

Operatör	Açıklama	
Kullanım

Sonuç
and	ve operatörü	
(8 < 10) and (6 > 5)

True
or	veya operatörü	
(5 == 5) or (6 == 5)

True
not	değil operatörü	not(5 == 5)	False