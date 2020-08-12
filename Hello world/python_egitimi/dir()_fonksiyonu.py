# dir fonksiyonu ile diğer fonksiyonların metodlarını öğrenebilirsiniz.

liste = ["liste1","liste2"]

for i in dir(liste):
    if "__" not in i: #sadece metodları göstermesini sağladık
        print(i)

"""
ÇIKTI:

append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort

bunların hepsi liste metodudur.
"""