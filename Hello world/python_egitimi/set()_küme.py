"""
Metodları:

Öğe Ekleme --> add
fark --> difference
öğe sil --> discard
öğe sil --> remove
kesişim --> intersection

İki tane silme yöntemi var.
    Discard kullanılırsa eğer silinmek istenilen öğe kümenin içinde yoksa
    hata vermez bir alt satırdaki komuta geçer.
    Ama remove kullanılırken silinmek istenilen öğe kümede yoksa hata verir ve
    program sonlanır.
Fark
    iki adet kümenin karşılaştırılmasında ilk kümenin ikinci kümeden
    farkını verir.
        örnek:
        a = set([1,2,3,4])
        b = set([3,4,5,6,7])
        print(a.difference(b))
        çıktı:
        {1}
    Bir diğer fark metodu seçilen kümenin diğer kümeye olan farkına
    dönüşmesi.
        örnek
        a = set([1,2,3,4])
        b = set([3,4,5,6,7])
        b.difference_update(a)
        print(b)
        çıktı:
        {5,6,7} yani 'b' artık 5,6,7 değerine sahip
Kesişim
    iki kümenin de içinde tuttuğu aynı değerler
        örnek
        a = set([1,2,3,4])
        b = set([3,4,5,6,7])
        print(b.intersection(a))
        çıktı:
        {3,4}
"""

#Örnekler
"""
1 - Kümelerin içine liste eklenebilir
    kume = set(["liste","liste2",12,45,2,76])
2 - Demetler eklenebilir
    kume = set((12,13,45))
3 - Sözlükler de kullanılabilir
    kume = set({Karakter : "Ahmet"})
AMA 
Sayılar kullanılamaz!!!

kume = set(11) yanlış kullanım
------------------------------
sayı = 23
kume = set(sayı)   yanlış kullanım
"""

#Kümeler hakkında
"""
Küme oluştururken aynı karakterden birden fazla varsa onlar çıktıda
gözükmez ve küme içindeki değerler belirli bir sırada yer almaz

Örnek:

string = "aaddrrtt"
kume = set(string)
print(kume)

Çıktı -->> {'a', 't', 'd', 'r'}

olur.

"""

#Farklı Küme oluşturma yolları

"""
Sözlük oluşturma yöntemi ile küme oluşturulabilir
ama aralarda ':' yoktur. Ve boş küme sadece ve
sadece set() ile oluşturulur.

kume = {"deneme1","deneme2","deneme3",12,23}

"""

#Küme metotları
"""

"""