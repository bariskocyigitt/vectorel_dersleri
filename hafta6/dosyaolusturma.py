class Rehber():
    def __init__(self, ad, uzanti):
        self.rehberadi = ad
        self.rehberuzantisi = uzanti
        self.dosyaadi = f"{self.rehberadi}.{self.rehberuzantisi}"
        open(self.dosyaadi, "a").close()

    def rehbereEkle(self, ad, tel):
        with open(self.dosyaadi, "a") as d:
            d.write(f"{ad}#{tel}#\n")


rehber1 = None

def anamenu():
    global rehber1
    print("=======================Ana Menu========================")
    print(" 1- Rehber Olustur")
    print(" 2- Kisi Ekle")
    print(" 3- Listele")
    print(" 9- Cıkıs")
    print(" Seciminiz Nedir?")
    secim = input()

    if secim == "1":
        rehber1 = Rehber("rehbervektorel", "txt")
        
    elif secim == "2":
        if rehber1:
            print("-------------Ekleme-------------")
            adi = input("Ad giriniz: ")
            tlf = input("Telefon no giriniz: ")
            rehber1.rehbereEkle(adi, tlf)
        else:
            print("Önce bir rehber oluşturmalısınız.")
            
            
    elif secim == "3":
        if rehber1:
            try:
                with open(rehber1.dosyaadi, "r") as d:
                    print(d.read())
            except Exception as e:
                print("Rehber okunamadı:", e)
        else:
            print("Önce bir rehber oluşturmalısınız.")
    elif secim == "9":
        print("Programdan çıkılıyor.")
        return
    else:
        print("Geçersiz seçim!")

    anamenu()  # tekrar çağır


anamenu()
