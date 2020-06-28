#bankamatik demo
'''
    Eklenebilecek özellikler:

    1- Dışarıdan oluşturalan admin paneline giriş yapılır ve yeni kullanıcılar eklenir.
    2- Kullanıcı adı şifre istedikten sonra para çekme yada yatırma seçeneği sunulur.Yapmaya çalıştım ama olmadı...
    3- Daha çok bilgi edirisem faiz oranı vs eklenebilir. Tam bir panel haline getirilebilir.
'''


DwtExe = {
    'ad': 'Ahmet Kaan',
    'hesapNo': '1325678383',
    'bakiye': 300000,
    'ekHesap': 20000
}

SelaxG = {
    'ad': 'Seyid Vurver',
    'hesapNo': '2144949409',
    'bakiye': 60000,
    'ekHesap': 100000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı Alabilirisniz...')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullan = input('Çekmek istediğiniz miktar bakiyenizi aşıyor.\nEk hesap kullanılsın mı? (e/h)')
            if ekHesapKullan == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranı çekebilirsin.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır.")
        else:        
            print('Üzgünüz bakiyeniz yok.')

# userName = input('Hesap kullanıcı adınızı giriniz :')
# cekimIstek = input(f"Bakiyeniz: {userName['bakiye']}\nEk hesap bakiyeniz: {userName[ekHesap]}\nÇekmek istediğiniz miktar nedir :")
paraCek(DwtExe, 30000)