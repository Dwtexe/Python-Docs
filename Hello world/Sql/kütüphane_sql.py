import sqlite3

# deepcode ignore missing~close~sqlite3.connect: <çünkü...>
baglanti = sqlite3.connect("database.db")

if baglanti:
    print("Başarılı...")
else:
    print("Başarısız...")

pen = baglanti.cursor()

pen.execute("""
CREATE TABLE IF NOT EXISTS kitaplar(
    kitap_no INTEGER PRIMARY KEY,
    kitap_adi VARCHAR(50),
    kitap_kategori INTEGER(2) )
""")
pen.execute("""
CREATE TABLE IF NOT EXISTS calisanlar(
    calisan_no  INTEGER PRIMARY KEY,
    calisan_adi VARCHAR(50),
    calisan_maas INTEGER(5))
""")
pen.execute("""
CREATE TABLE IF NOT EXISTS kategoriler(
    kategori_no INTEGER PRIMARY KEY,
    kategori_adi VARCHAR(50)
)
""")

pen.execute("""
INSERT INTO calisanlar(calisan_adi,calisan_maas) VALUES ("Anastacio Cruickshank",4500)
""")
baglanti.commit()
baglanti.close()