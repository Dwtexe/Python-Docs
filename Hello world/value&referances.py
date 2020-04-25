Python Value Types
Python value yani değer tipindeki veriler ile referans tipindeki veri tipleri belleğin farklı bölümlerinde tutulduklarından dolayı value ve referans tipiyle nasıl çalışmamız gerektiğini biliyor olmamız gerekiyor.

Value tipinde tanımlanan bir veri (örneğin; number,string) tanımlamalarını aşağıdaki gibi yapalım.

x, y = 5, 25
x = y
y = 10

print(x,y) # 25, 10
Burada x, 5 ve y, 25 değerlerini aldıktan sonra y' nin değerini x' e eşitliyoruz ve x, 25 değerine sahip oluyor ve sonrasında y' nin değerini 10 a eşitliyoruz ancak y' nin 10' a eşitlenmesi x' in değerini etkilemiyor çünkü atama sırasında değer ataması yapılıyor dolayısıyla x ve y farklı adreslerde tutulan verilerdir.

Python Reference Types
Referans tipinde tanımlanan veri tipleri (örneğin; list) atanan değeri tutmak yerine değerin tutulduğu adresleri saklarlar. Adreslerin karşılığı olan veriler ise (["apple","banana"]) belleğin farklı bölgesinde tutulur.

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a, b) # ["grape","banana"] , ["grape","banana"]
a ve b listeleri içindeki veriler farklı adres bilgilerini tutan veri tipleridir. a = b dediğimizde b' nin adresi a' ya atanır ve sonuçta a ve b, aynı adresleri tutarlar. Dolayısıyla a ya da b' de yapılan bir değişiklik aynı adreste yapıldığından dolayı a ve b ' nin içeriği de aynı olmuş olur.

a ve b 'nin içerikleri ["grape","banana"] , ["grape","banana"] olur.