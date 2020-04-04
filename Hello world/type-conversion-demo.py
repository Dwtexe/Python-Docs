'''
Uygulama: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.

Daire Alanı : πr² 

Daire Çevresi : 2πr 

r: 3.14

Kullanıcıdan aldığımız değerler bize string veri tipinde gelir. 
Gelen ondalıklı değerleri float() metodu ile float değerlere dönüştürmemiz lazım. 
Hesaplama işlemi bittikten sonra da ekranda sonucu string şeklinde göstermeliyiz çünkü 
string birleştirme işlemine sadece string değerler girer.
'''

pi = 3.14
r = float(input("yarı çap: "))

alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan: ", alan, " çevre: ", cevre)

# yada 
#print("alan: "+ str(alan) + " çevre: "+ str(cevre))