import sqlite3

# deepcode ignore missing~close~sqlite3.connect: <çünkü...>
baglanti = sqlite3.connect("database.db")

if baglanti:
    print("Başarılı...")
else:
    print("Başarısız...")

pen = baglanti.cursor()

pen.execute("""
    CREATE TABLE kitaplar(
    kitap_no INTEGER PRIMARY KEY,
    kitap_adi VARCHAR(50),
    kitap_kategori INTEGER(2) )
""")