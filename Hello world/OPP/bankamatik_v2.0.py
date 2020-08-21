from os import system as cmd

class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,ID,PAROLA,ISIM):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))

def main():
    banka = Banka()
    while True:
        cmd("clear")
        print("""
        [1] Banka Müşterisiyim 
        [2] Banka Müşterisi Olmak İstiyorum
        [0] Çıkış
        """)

        secim = input("Seçiminiz: ")

        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            """
            Yukarıda yapılan şey:

            for i in banka.musteriler:
                ids += [i.id]
            """
            ID = input("ID:")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id: # müşteri bulundu
                        print(f"Hoşgeldiniz {musteri.isim}")
                        parola = input("Parolanız: ")
                        if parola == musteri.parola:
                            print("Giriş Başarılı ")
                            while True:
                                cmd("clear")
                                print("""
                                [1] Bakiye Sorgula
                                [2] Para Yatır
                                [3] Para GÖnder
                                [4] Para Çek
                                [0] Çıkış
                                """)

                                secim2 = input("İşleminiz: ")

                                if secim2 =="1":
                                    print(f"Bakiyeniz: {musteri.bakiye}")
                                    input("Ana menüye dönmek için 'enter'a basınız.")
                                
                                elif secim2 =="2":
                                    miktar = int(input("Miktar: "))
                                    onay = input(f"Kendi hesabınıza {miktar} TL para yatırma işlemini onaylıyor musunuz?: E/H\n")
                                    if onay == "e" or onay == "E":
                                        musteri.bakiye += miktar
                                        input("Para yatırma işlemi tamamlandı.\nAna menüye dönmek için 'enter'a basınız.")
                                    
                                    elif onay == "h" or onay == "H":
                                        input("İşlem iptal edildi.\nAna menüye dönmek için 'enter'a basınız.")
                                    
                                    else:
                                        input("İşlem iptal edildi.\nAna menüye dönmek için 'enter'a basınız.")

                                elif secim2 =="3":
                                    araID = input("Müşteri ID: ")
                                    if araID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if araID == digerMusteri.id:
                                                miktar = int(input("Miktar: "))
                                                if miktar <= musteri.bakiye:
                                                    onay = input(f"{digerMusteri.isim} adlı müşterimize  {miktar} TL para gönderme işlemini  onaylıyor musunuz? E/H: ")
                                                    onay = onay.lower
                                                    if onay == "e" or onay == "E":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        input("Para gönderildi!\nAna menüye dönmek için 'enter'a basınız.")
                                                    elif  onay == "h" or onay == "H":
                                                        input("İşlem iptal edildi.\nAna menüye dönmek için 'enter'a basınız.")
                                                    else:
                                                        input("Hatalı giriş!\nAna menüye dönmek için 'enter'a basınız.")
                                                else:
                                                    input("Bakiyeniz Yetersiz!\nAna menüye dönmek için 'enter'a basınız.")
                                    else:
                                        input("Müşteri Bulunamadı!\nAna menüye dönmek için 'enter'a basınız.")

                                elif secim2 == "4":
                                    miktar = int(input("Miktar: "))   
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        input("İşlem tamamlandı, paranızı alınız!\nAna menüye dönmek için 'enter'a basınız.")
                                    else:
                                        input("Bakiyeniz yetersiz!\nAna menüye dönmek için 'enter'a basınız.")
                                
                                elif secim2 == "0":
                                    break

        elif secim == "2":
            ID = input("ID: ")
            ISIM = input("İsminiz: ")
            parola1 = input("Şifreniz: ")
            parola2 = input("Şifrenizi tekrar girin: ")
            if parola1 == parola2:
                PAROLA = parola1
                print("Bizi Tercih Ettiğiniz İçin Teşekkürler...")
                input("Kaydınız tamamlandı, giriş  yapabilirsiniz!\nAna menüye dönmek için 'enter'a basınız.")
            banka.musteri_ol(ID,PAROLA,ISIM)
        elif secim == "0":
            print("İyi Günler...")
            quit()

if __name__ == "__main__":
    main()