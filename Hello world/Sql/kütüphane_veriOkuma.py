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

calisanlar = pen.execute("SELECT * FROM calisanlar")
for calisanlar in calisanlar.fetchall():
    print("Çalışan Numarası : %s || Çalışan İsimi : %s || Çalışan Maaşı : %s" %calisanlar)
print("--"*40) 
# Maaşı 2000 olanları yazdırmak için
calisanlar = pen.execute("SELECT * FROM calisanlar WHERE calisan_maas=2000")
for calisanlar in calisanlar.fetchall():
    print("Çalışan Numarası : %s || Çalışan İsimi : %s || Çalışan Maaşı : %s" %calisanlar)

print("--"*40)
calisan = pen.execute("SELECT * FROM calisanlar ORDER BY calisan_adi LIMIT 2")
for i in calisan:
    print(i[1])
baglanti.commit()
baglanti.close()