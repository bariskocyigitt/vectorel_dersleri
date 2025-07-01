try: 
    s1=int(input("1. sayıyı giriniz: "))
    s2=int(input("2. sayıyı giriniz: "))

    islem= input("Yapılacak islem nedir? (+,-,*,/)")
    
    if islem=="+": sonuc=s1+s2
    elif islem=="/": sonuc=s1/s2
 
# except: print("Hata olustu ")   
# except Exception as xx: print("Hata mesajı  ",xx)   
except ZeroDivisionError as ee: print(f"Bolen sıfır olamaz : {ee}")
except ValueError as aa: print(f"Metin ile sayı toplanamaz: {aa}")
else: print("Hata yok..")
finally: print("İslem bitti")