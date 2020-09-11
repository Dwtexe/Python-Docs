import itertools
import operator

# GROUPBY FONKSİYONU

yazilimDilleri = [
    ('Python', 'Her Yer'),
    ('Php', 'Web Geliştirme'),
    ('Asp', 'Web Geliştirme'),
    ('Kotlin', 'Android Geliştirme'),
    ('Java', 'Android Geliştirme'),
    ('Swift', 'İos Geliştirme')
]


grup = itertools.groupby(yazilimDilleri, lambda x: x[1])

for alan, dil in grup:
    print (alan)

    for i in list(dil):
        print (i[0])

    print("")

