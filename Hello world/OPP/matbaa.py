import time,os

class Matbaa():


    def __init__(self):
        self.devir = 0
        self.murekkep = 1000
        self.sarj = 1000
        self.dergiler = []
    
    def calis(self):
        while self.devir<=20:
            if(self.murekkep<=0):
                print("Mürekkep bitti...")
                time.sleep(2)
            elif(self.sarj<=0):
                print("Şarj bitti...")
                time.sleep(2)
            else:
                self.devir += 1
                if self.murekkep<3:
                    self.murekkep = 0
                else:
                    self.murekkep -=3
                if self.sarj<6:
                    self.sarj = 0
                else:
                    self.sarj -= 6
                print("Makine çalışıyor...")
                time.sleep(0.2)
                if(self.devir==20):
                    self.devir = 0
                    self.yeniDergi()
                    break
    def yeniDergi(self):
        print("Yeni dergi Basıldı!\nMakine Durduruldu!")
        a = input("Derginin ismi ne olsun: ")
        self.dergiler.append(a) 
        time.sleep(2)
    def sarjDoldur(self):
        if(self.sarj<100):
            self.sarj += 10
            print("Şarj Dolduruldu! Mevcut şarj -->",self.sarj)
            time.sleep(2)
    def murekkepDoldur():
        if(self.murekkep<100):
            self.murekkep += 10
            print("Mürekkep dolduruldu! Mevcut mürekkep -->",self.murekkep)
    def durum(self):
        print("MAKİNENİN DURUMU:")
        print("Kalan Mürekkep -->",self.murekkep)
        print("Kalan şarj -->",self.sarj)
        print("Toplam çıkarılan dergi sayısı -->",len(self.dergiler))
        if(len(self.dergiler)>0):
            print("Çıkarılan Dergiler:")
            for i in self.dergiler:
                print(i)
        print("Yeni çıkacak derginin %",self.devir*5,"kısmı tamamlandı...")
        time.sleep(5)

makine1 = Matbaa()

def main():
    while True:
        print("Matbaamıza Hoşgeldiniz!")

        print("-"*30)

        menu ="""
        [1] Makineyi Çalıştır
        [2] Durum Bilgisi
        [3] Şarj Doldur
        [4] Mürekkep Doldur
        [0] Çıkış

        """

        komut = input(menu)
        os.system("cls")

        if komut=="1":
            makine1.calis()
            input("Ana menüye dönmek için 'enter'a basınız.")
        elif komut=="2":
            makine1.durum()
            input("Ana menüye dönmek için 'enter'a basınız.")
        elif komut=="3":
            makine1.sarjDoldur()
            input("Ana menüye dönmek için 'enter'a basınız.")
        elif komut=="4":
            makine1.murekkepDoldur()
            input("Ana menüye dönmek için 'enter'a basınız.")
        elif komut=="0":
            break
        else:
            input("Hatalı giriş!\nAna menüye dönmek için 'enter'a basınız.")

if __name__ == "__main__":s
    main()