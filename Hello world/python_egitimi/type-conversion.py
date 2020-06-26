# # Veri tipi dönüşümleri

# x = input('1.sayı: ')
# y = input('2.sayı: ')

# toplam = x + y
# print(toplam)          #sonuç bekleniği gibi x+y olmaz xy olarak çıkar çünkü girilen değerler string'dir.

# print(type(x))    # <class 'str'> şeklinde bir çıktı ile karşılaşırız.
# print(type(y))    # <class 'str'> şeklinde bir çıktı ile karşılaşırız.

# toplam = int(x) + int(y)    # İki değeride sayısal (int(integer)) hale getirelim.
# print(toplam)               # sonuç istediğimiz gibi çıkar. (x+y)




# # Diğer veri tipi dönüştürme metodları.

# x = 10 
# y = 20.5
# isOnline = True

# # int to float (int den float a çevirme)


# x = float(x)     # int to float
# print(x)         # 10.0 
# print(type(x))   # <class 'float'>


# # float to int (float tan int e çevirme)

# y = int(y)     # float to int 
# print(y)       # 20 
# print(type(y)) # <class 'int'> 


# # int to str

# result = str(x) + str(y)   # int to string
# print(result)              # 1020.5
# print(type(result))        # <class 'str'>



# # bool to str

# result = str(x) + str(y)   # int to string
# print(result)              # 1020.5
# print(type(result))        # <class 'str'>



# #bool to int

# isOnline = int(isOnline)   # bool to int
# print(isOnline)            # 1 (True için 1, False için 0)
# print(type(isOnline))      # <class 'int'> 