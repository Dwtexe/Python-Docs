import itertools
import operator

# ZIP_LONGEST FONKSİYONU

diller = ["Python", "Php", "Kotlin", "Java", "Asp", "C++", "C#", "Javascript"]
kategoriler = ["Her Şey", "Web", "Android", "Android-Masaüstü", "Web"]

zip = itertools.zip_longest(diller, kategoriler, fillvalue="Diğer Kategori")

for i in zip:
    print(i)
