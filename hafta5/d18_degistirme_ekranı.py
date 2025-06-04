#degistirme ekranı 
d=open("rehber.txt")
print("----------Degistirme Ekranı ---------")

aranan= input("Aradıgınız: ").upper()
yeni= input("Yenisi: ")

okunan=d.readlines()
durum=True
yeniveri=""

for a in okunan:
    satir= a.split("#")
    if satir[0].upper()==aranan or satir[1].upper()== aranan:
        print(f"\033[1;32;40mBulundu: \n Ad: {satir[0]}, Numara: {satir[1]}")
        durum=False 
        yeniveri+= f"{yeni}# {satir[1]}#\n"
    else:
        yeniveri +=a  
        
ydosya= open("rehber.txt","w")
ydosya.write(yeniveri
             )
if durum : print("\033[1;31;40m Kayıt Bulunamadı. \033[1;37;40m ")