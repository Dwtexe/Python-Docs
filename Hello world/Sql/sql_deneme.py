import sqlite3

veriler = [
    ("Ahmet Ümit","İstanbul Hatırası"),
    ("Paulo Coelho","Simyacı"),
    ("Paulo Coelho","Aldatmak")]

db = sqlite3.connect("kitaplar.sqlite")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS  kitaplik (yazar,kitap)") #if not exists eğer dosya varsa oluşturma demek

for veri in veriler:
    imlec.execute("INSERT INTO kitaplik VALUES (?,?)",veri)
db.commit() #dataya girilen veriyi işliyor

db.close()