#Batarya Bilgileri = /sys/class/power_supply/BAT0

dosya = open("/sys/class/power_supply/BAT0/capacity")

veri = dosya.read()

dosya.close()

print(veri) #Bataryanın doluluk miktarı