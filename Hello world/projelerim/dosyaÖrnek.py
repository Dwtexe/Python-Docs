with open("ayarlar.txt","r+") as dosya:
    liste = dosya.readlines()

    ilkkez = liste[0][:-1]
    ilkkezDeger = ilkkez.split("=")[1]

    if(ilkkezDeger=="True"):
        print("Hoşgeldiniz. Sizi buralarda ilk kez görüyoruz. "
              "Gelin size biraz programı tanıtalım!")
        liste[0]="ilkkez=False\n"
        dosya.seek(0)
        dosya.writelines(liste)
    else:
        print("Yeniden hoşgeldiniz!")

    lisans = liste[1][:-1]
    lisansDeger = lisans.split("=")[1]

    if(lisansDeger=="Trial"):
        print("-> Şu anda deneme sürümü kullanıyorsunuz. Son 20 gün kaldı !")
        a = input("Full sürümü aktifleştirmek için S tuşuna basınız: ")

        if(a=="S"):
            serial = input("Lütfen serial numarasını giriniz: ")
            orjSerial = liste[3][:]
            orjSerialDeger = orjSerial.split("=")[1]

            if(serial==orjSerialDeger):
                isim = input("Serial doğru. Lütfen isminizi giriniz: ")
                liste[2] = "isim="+isim+"\n"
                liste[1] = "lisans=Full\n"
                dosya.seek(0)
                dosya.writelines(liste)
                print("Tebrikler! Artık full sürüm kullanıyorsunuz !")
            else:
                print("HATA ! Geçersiz kod!")


    else:
        print("Tebrikler FULL Sürümdesiniz !")