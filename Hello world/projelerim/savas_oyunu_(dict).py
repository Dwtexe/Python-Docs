"""
beynim yandı bir ara bakıcam sana güzellik.
kafa kalmadı lan :((
"""
import os
import random
import time
guc1 = random.randint(0,100)
guc2 = random.randint(0,100)

user1 = input("1. Oyuncunun  adı : ")
user2 = input("2. Oyuncunun  adı : ")
os.system("clear")
weapon1 = input("1. Oyuncunun silahı : ")
weapon2 = input("2. Oyuncunun silahı : ")
os.system("clear")
karakter1 = {"ad" : user1,
            "güç" : guc1,
            "silah" : weapon1,
            "can" : 100}
karakter2 = {"ad" : user2,
            "güç" : guc2,
            "silah" : weapon2,
            "can" : 100}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["güç"]
    vurulan["can"] = vurulan["can"] - eksilen

while True:
    vur(karakter1,karakter2)
    if karakter1["can"] <=0:
        print(f"{user1} Tebrikler oyunu sen kazandın...")
        time.sleep(2)
        print("Yine bekleriz.")
        quit()
    elif karakter2["can"] <=0:
        print(f"{user2} Tebrikler oyunu sen kazandın...")
        time.sleep(2)
        print("Yine bekleriz.")
        quit()
    else :
        continue
    print(f"İlk vurma üstünlüğüne sahip olan kişi {user1} oldu")
    print("Veeee")
    time.sleep(5)
    print(f"{guc1} gücünde bir saldırı yaptı")
    os.system("clear")
    print(f"{user2} Sıra sende bileğine kuvvet")
    vur(karakter2,karakter1)
    print("Veeee")
    time.sleep(5)
    print(f"{guc2} gücünde bir saldırı yaptı")
