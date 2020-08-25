import sqlite3

# deepcode ignore missing~close~sqlite3.connect: <çünkü...>
baglanti = sqlite3.connect("database.db")

if baglanti:
    print("Başarılı...")
else:
    print("Başarısız...")

pen = baglanti.cursor()


pen.execute("DELETE FROM calisanlar WHERE calisan_no=2")
# dikkati kullanılmalı maaş üzreinden kullanmış olsaydık aynı maaşa sahip olan herkesi silerdi
pen.execute("INSERT INTO calisanlar(calisan_no,calisan_adi,calisan_maas) VALUES (2,'Randal Mayer',6500)")
baglanti.commit()
baglanti.close()
