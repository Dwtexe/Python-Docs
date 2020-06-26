#KUllanıcı için sisteme giriş menüsüne çevrilecek ve düzenlemeler yapılacak.

username = input("Kullanıcı Adınızı giriniz :")
password1 = input("Parolanızı belirleyiniz :")
password2 = input("Parolanızı doğrulayınız :")

approve = password1 == password2

if approve:
    print("Kaydınız onaylanmıştır giriş yapınız. ")
else:
    print("Parolalar uyuşmuyor!")