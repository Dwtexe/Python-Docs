import itertools
import operator

# PERMUTATIONS FONKSİYONU

liste = [1, 2, 3, 4, 5]

per = itertools.permutations(liste, 3)

for i in per:
    print(i)

