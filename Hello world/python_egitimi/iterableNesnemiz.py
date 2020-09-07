

# SIRA GELDİ KENDİ ITERABLE NESNEMİZİ (MAHALLEMİZİ) OLUŞTURMAYA

class Mahalle():
    def __init__(self,arkadaslar):
        self.arkadaslar = arkadaslar
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if(self.index < len(self.arkadaslar)):
            # return self.arkadaslar[self.index]
            return "Mahallemizin "+str(self.index+1)+".kişisi ziyaret ediliyor. İsmi: "+self.arkadaslar[self.index]
        else:
            self.index = -1
            raise StopIteration



vefa = Mahalle(["mustafa","hasan","kemal","orhan"])

ziyaret = iter(vefa)
print(next(ziyaret))
print(next(ziyaret))

for i in vefa:
    print(i)