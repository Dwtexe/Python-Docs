with open("WithOpenAs.txt","w",encoding="utf-8") as dosya:
    dosya.write("Python Öğreniyorum")
    dosya.write("Python Eğlenceli")
    dosya.write("\nPython'ı sevdim")


with open("WithOpenAs.txt","r",encoding="utf-8") as dosya:
    liste = dosya.readlines()
    print(liste)

"""
With sayesinde dosya kapama işlemini sürekli yapmamız gerekmiyor.
with in girintisine o dosya ile ilgili tüm kodlar yazıldıktan sonra dosya kapanır.
as o dosyayı isimlendirmeyi sağlar.
"""

with open("WithOpenAs.txt","r",encoding="utf-8") as dosya:
    for i in dosya:
        print(i)

with open("WithOpenAs.txt","r",encoding="utf-8") as dosya:
    print(dosya.tell()) #imlec konumu
    dosya.seek(10) #imlecin yer değiştirmesi
    print(dosya.tell()) #imlec konumu
    print(dosya.read(10)) #imlecin o anki konumundan sonraki 11 karakteri alır