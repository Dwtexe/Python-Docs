dosya = open("dosya_yazma.txt","r")

okunan = dosya.readlines()
print(okunan)
dosya.close()