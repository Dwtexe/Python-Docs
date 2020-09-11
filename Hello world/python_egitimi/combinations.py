import itertools
import operator


# COMBINATIONS FONKSİYONU

meyve = ["elma", "armut", "karpuz", "portakal"]

kombin = itertools.combinations(meyve, 2)
# kombin = itertools.combinations_with_replacement(meyve,2)

for i in kombin:
    print(i)

