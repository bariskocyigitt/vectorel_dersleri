with open("rehber.txt","r") as d:
    print("-------------Arama Yap---------")
    aranan=input("Aranan: ")
    
    for sn,a in enumerate(d,1):
        if aranan.lower() in a.lower():
            print(f"{sn} .satırda bulundu \n Adı: {a.strip().split("#")[0]}, Numarası: {a.strip().split("#")[1]} " )
                  
            