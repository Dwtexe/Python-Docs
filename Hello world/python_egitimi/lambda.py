"""

Lambda ile basit fonksiyonları yazabiliriz.
def e göre daha hızlı çalışır.

"""

#Normalde
def ucgenmi(a,b,hipotenus):
    if a**2 + b**2 = hipotenus**2:
        return True
    else:
        return False


#Lamba ile
ucgenmi2 = lambda a,b,hipotenus : a**2 + b**2 = hipotenus**2

print(ucgenmi2(3,4,5))