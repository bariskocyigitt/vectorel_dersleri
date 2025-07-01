try:
    s1= int(input("1. Sayıyı giriniz(0-100): "))
    s2= int(input("2. Sayıyı giriiniz(0-100): "))
    if s1>100 or s2>100:
        raise TypeError("Sayılar 0-100 araasında olmalı ")


    else: 
        islem= input("Yapılacak islem nedir? (+,-,*,/) \n")
    
    if islem=="+":print("Sonuc: ",s1+s2)
    elif islem=="/":print("Sonuc: ",s1/s2)
    
except Exception as xx:
    print("Hata mesajı ",xx)