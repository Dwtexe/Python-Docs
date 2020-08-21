import random,os
class Dusman():
    def __init__(self):
        self.durum = True
        self.saglik = random.randint(30,70)
        self.kalkan = random.randint(0,10)
        self.güç = random.randint(20,50)

    def vur(self,player):
        damage = self.güç - player.kalkan
        player.saglik -= damage 



class Player():
    def __init__(self):
        self.durum = True
        self.saglik = 250
        self.kalkan = 20
        self.güç = random.randint(40,60)
    def vur(self,dusman):
        damage = self.güç - dusman.kalkan
        dusman.saglik -= damage
        if dusman.saglik <= 0:
            dusman.durum = False
            dusmanlar.remove(dusman)
    

dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman())

player = Player()

while True:
    os.system("clear")
    print(f"Player --->|Sağlık: {player.saglik} |Güç: {player.güç} |Kalkan: {player.kalkan}")
    if player.saglik <= 0:
        player.durum = False
        print("Oyunu kaybettin...")
        quit()
    
    if not dusmanlar:
        print("Tebrikler Kazandın.")
        quit()
    for i in dusmanlar:
        print(f"{dusmanlar.index(i)}. Düşman ---> |Sağlık: {i.saglik} |Güç: {i.güç} |Kalkan: {i.kalkan}")
    
    secim == int(input("Düşman Seçiniz: "))
    dusman = dusmanlar[secim]
    player.vur(dusman)
    if dusmanlar:
        saldırgan = dusmanlar[random.randint(0,len(dusmanlar) -1)]
        saldırgan.vur(player)
        
