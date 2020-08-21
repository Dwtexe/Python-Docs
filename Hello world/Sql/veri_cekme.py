import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

imlec.execute("SELECT * FROM kitaplik WHERE yazar = 'Paulo Coelho'")

veriler = imlec.fetchmany()

print(veriler)
#veriler = imlec.fetchall()
#for veri in veriler:
#    print(veri)


db.close()