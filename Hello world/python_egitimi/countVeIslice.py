import itertools
import operator

# COUNT FONKSİYONU

say = itertools.count(0,3) # DİKKAT SONSUZ DÖNGÜ

for i in say:
    print(i)
    if i > 20:
        break


# ISLICE FONKSİYONU

renkler = ["kırmızı","yeşil","mavi","mor"]

dilim = itertools.islice(renkler, 4)

for i in dilim:
    print(i)


say = itertools.islice(itertools.count(0,3), 10)

for i in say:
    print(i)

