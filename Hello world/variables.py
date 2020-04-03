# iki kişinin maaşlarının vergi oranını iki farklı şekilde hesaplayalım. (iki yöntem de aynı işe yarar.)


# 1. yol:

#print("Ahmet'in maaşı : " , 5000 - (5000 * 0.27))
#print("Ali'nin maaşı :" , 4000 - (4000*0.27))

# 2. yol:

#maasAli = 4000
#maasAhmet = 5000
#vergiOranı = 0.27

#print("Ahmet'in maaşı : " , maasAhmet - (maasAhmet*vergiOranı))
#print("Ali'nin maaşı :" , maasAli - (maasAli * vergiOranı))

# Kullandığımız yollardan ilkinde değerleri sürekli tekrar tekrar yazmak zorunda kaldık.
# Kullandığımız ikinci yolda ise bir değişken (variable) atadık ve o değişkene bir değer verdik.
# Büyük projelerde değişken kullanılır. Bu sebepten ötürü değişken kullanmayı alışkanlık edinmek gerekir.

# Değişken tanımlama kuralları:

# 1. kural => Değişken tanımlarken sayı ile başlanmaz örneğin: 1örnek değişkeni kullanılamaz ama değişkenin sonuna sayı gelebilir yada değiken _ - gibi özel karakterlerle başlayabilir.
# 2. kural => Bir değişkeni 2 kere tanımlarsak o değişkeni güncellemiş oluruz örneğin:

variable1 = 20
print(variable1)
variable1 = 30
print(variable1)
# iki güncellemenin sonucunu da terminalde görebiliriz.
variable2 = 30
variable2 = 70
print(variable2)
# Terminalde 70 değeri yazar çünkü variable2 değişkenini 30 değerinden 70 değerine günccelledik.

# Bir değişkenin değerini arttırabiliriz örneğin:

variable3 = 10
print(variable3)
variable3 += 40          # Bu satırda variable3 değişkenini 40 arttırdık değişkenin çıktısını aldığımızda 10+40=50 yani bize 50 değerini vericek.
print(variable3)


# 3. kural => Değişken adı koyarken büyük küçük harf duyarlılığı olduğunu unutmaynız. Örneğin:

AGE = 15
age = 25

print(age , AGE)

# 4. kural türkçe kararkter kullanmamak çok önemlidir. İngiliz alfabesini kullanmaya özen gösterelim.

# Değişken tanımlama türleri tek satırda veya üstte yazdığım gibi alt alta değişken tanımlanabilir.

x = 1                        # Integer veri türüdür.
y = 2.0                      # Float veri türüdür.
name = "Çınar"               # String veri türüdür ve  çift tırnak veya tek tırnak içinde yazılır.
isSutudent = True            # Bool veri türüdür. Sadece True yada False değerini alabilir.

# Bu değişkenleri tek satırda tanımlayalım.

x, y, name, isSutudent = (1, 2.0, 'Çınar', True)

# String bir ifade ile String bir ifadeyi toplarsanız iki ifadeyi de yanyana yazmış olursunuz. Örneğin:

a = '10'
b = '20'
print(a+b)                   # Gördüğünüz gibi sonuç 1020 oldu. Bunu isim soyisim yazarken de kullanabiliriz.

firstName = 'Mahmut'
lastName = " Tuncer"         # Soyismin başına boşluk bırakmalıyız ki MahmutTuncer değil de Mahmut Tuncer olarak çıktımızı alalım.
print(firstName+lastName)
