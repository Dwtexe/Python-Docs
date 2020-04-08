website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = ' Hello World '.strip()     # baş ve sondaki boşluk karakterleri silinir.
result = ' Hello World '.lstrip()    # baştaki boşluk karakterleri silinir.
result = ' Hello World '.rstrip()    # sondaki boşluk karakterleri silinir.
result =   website.lstrip('/:pth')   # baştan itibaren '/:pth' karakteri silinir. result "www.sadikturan.com" değerini alır.


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip('w.moc')


# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

result = course.lower() # küçük harfe çevrilir.
result = course.upper() # büyük harfe çevrilir.
result = course.title() # her kelimenin baş harfe büyük harfe çevrilir.


# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

result = website.count('a')         # a karakteri sayılır.
result = website.count('www')       # www karakterleri sayılır. 
result = website.count('www',0,10)  # 0 ile 10. indeks arasında www ifadesi sayılır.


# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

result = website.startswith('www')    # website www ile başlıyor mu ? False
result = website.startswith('http')   # website http ile başlıyor mu ? True
result = website.endswith('com')      # website com ile bitiyor mu ? True


# 6- 'website' içinde 'com' ifadesi var mı?

result = website.find('com')          # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
result = website.find('com',0,10)     # 0 ile 10 arasında com ifadesini bulamaz ve exception döndürür.
result = course.find('Python')        # 0.indeksten itibaren bulduğu ilk Python için 0 değeri döner.
result = course.rfind('Python')       # Aramaya sağdan başlayacağından dolayı 2. Python' i 26. indekste bulur.
result = website.index('com')         # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
result = website.rindex('com')        # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
result = website.rindex('comm')       # comm bulunamadığından "ValueError: substring not found" hatası gelir.


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.
result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.
result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir.
result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.


# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = 'Contents'.center(50, '*')    # **** Contents **** şeklinde toplam 50 karakter olur.
result = 'Contents'.ljust(50, '*')     # Contents ********* şeklinde toplam 50 karakter olur.
result = 'Contents'.rjust(50, '*')     # ********* Contents şeklinde toplam 50 karakter olur.


# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

result = course.replace(' ', '-')    # tüm boşluk karakterleri '-' ile değiştirilir.
result = course.replace(' ', '-',5)  # ilk 5 boşluk karakterleri '-' ile değiştirilir.
result = course.replace(' ', '')     # tüm boşluk karakteri silinir.


# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

result = 'Hello World'.replace('World','There')


# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(' ')  # ['Python', 'Kursu:', 'Baştan', 'Sona', 'Python', 'Programlama', 'Rehberiniz', '(40', 'saat)']
result = result[2]          # 'Baştan'
result = result[5]          # 'Programlama'

print(result)
# split metodu ile string ifadeyi her boşluk karakterinden ayırıp bir listeye çevirmiş oluruz ve her bir liste elemanına indeks numarası ile ulaşabiliriz.