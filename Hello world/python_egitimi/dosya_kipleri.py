"""

'r' --> Okuma

'w' --> Yazma (Önceden yazılanlar varsa siler)
'a' --> Yazma (Önceden yaılanın üstüne yazar)
'x' --> Yazma (Dosya varsa hata verir)

'r+' --> Okuma ve Yazma (Dosyanın var olması gerekir)
'w+' --> Okuma ve Yazma (Önceden yazılan varsa siler ve dosya yoksa oluşturur.)
'a+' --> Okuma ve Yazma
'x+' --> Okuma ve Yazma

"""

dosya = open