import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

menu = """
[1] Kitap Ara
[2] Yazar Ara
[0] Çıkış
"""

def main():
    while True:
        print(menu)
        secim = input("İşleminiz: ")
        if secim == "1":
            isim = input("Kitap Adı: ")
            sorgu = f"SElECT * FROM kitaplik WHERE kitap = '{isim}'"
            imlec.execute(sorgu)
            veriler = imlec.fetchall()
            for i in veriler:
                print(i)

        elif secim == "2":
            isim = input("Yazar Adı: ")
            sorgu = f"SElECT * FROM kitaplik WHERE yazar = '{isim}'"
            imlec.execute(sorgu)
            veriler = imlec.fetchall()
            for i in veriler:
                print(i)

        elif secim == "0":
            print("İyi Günler...")
            quit()

        else:
            print("Yanlış yazım...")

    db.close()


if __name__ == "__main__":
    main()