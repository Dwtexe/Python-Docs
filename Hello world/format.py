name = 'Çınar'
surname = 'Turan'
age = 45
# print('My name is {} {}' .format(name, surname))
#print('My name is {1} {0}' .format(name, surname)) # Değişken sıralamalarını değiştirebiliriz
#print('My name is {s} {n}' .format(n=name, s=surname)) # Değişkenleri format parantezinde başka bir değişkene atayabiliriz yani kısaltmayı kısaltabiliriz.
#print("My name is {} {} and I'm {} years old. " .format(name, surname, age))

# result = 200 / 700
# print("the result is {r:1.3}" .format(r=result)) #float bilgiyi kısaltmamızı sağladı

print(f'My name is {name} {surname} and I am {age} years old') # parantezin başına 'f' ekleyerek sağında kalan kısmın tamamına sadece süslü parantez ekleyerek süslü parantezlerin içine değişken adını yazmamız yeterlidir. değişken veri türü önemsizdir.
