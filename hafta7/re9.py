import re 

def anaekran():
    telefon= input("Telefon numarasını giriniz")

    #sadece 11 haneli ve 0 ile başlayan telefon numaraları gecerlı

    desen=r"^0[5][0-9]{9}$"

    if re.fullmatch(desen,telefon):
        print("Telfon numarası gecerlı")
    else:
        print("gecersız telefon numarası ")
        print("sadece 11 haneli ve 0 ile başlayan telefon numarası girin")
        
    anaekran()
anaekran()