try:
    print(10/0)
except Exception as hata:
    print("Hata olustu")
    print("Hata kodu: ",hata)
    
    if str(hata)=="division by zero ": print("Bolme isleminde bolen 0 ")
    
input()