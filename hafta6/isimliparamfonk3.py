kayitNo=1
def kayit_olustur(ad,soyad,numara):
    global kayitNo
    print(f"\n{kayitNo}. kayıt olusturuldu")
    print(f"Soyad:{soyad}   Ad:{ad}   Numara:{numara}\n")
    kayitNo+=1

kayit_olustur("Erhan","Gun","41")
kayit_olustur("23","Erdinc","DONMEZ")
kayit_olustur("Erdinc",numara="23",soyad="Dönmez")
