import itertools
import operator


# CYCLE FONKSİYONU

renkler = ["kırmızı", "mavi", "sarı" ,"yeşil", "mor"]

sonsuzRenk = itertools.cycle(renkler)

say = 0

for renk in sonsuzRenk:
    say += 1
    print(renk)

    if say > 30:
        break

