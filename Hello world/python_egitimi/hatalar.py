bolunen = float(input("Bölünen : "))
bolen = float(input("Bölen : "))

try:
    print("Sonuç : ",bolunen/bolen)

except ZeroDivisionError as hata:  #as hata normalde oluşan hatayı hata değişkenine aktardık
    print("0'a bölüm tanımsızdır!")
    print("Gerçek hata :")
    print(hata)

except ValueError:
    print("Veri tipi desteklenmiyor.")  # Sayı olmayan karakterler girilirse bu hata verilir

finally: # Her durumda çıktı olarak basılır
    print("Kullandığınız için teşekkürler.") 