

def hesapla(a,b,c):
    
    def topla(a,b):
        print("Toplam: ",a+b)

    def carpma(a,b):
        print("Carpma:",a*b)
    
    if c=="+": topla(a,b)
    elif c=="*": carpma(a,b)
    else :
        print("böyle bir islem tanınmadı")
        exit()
        print("-----")
    

hesapla(4,5,"+")