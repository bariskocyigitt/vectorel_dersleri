
degisken=11

def fonksiyon1():
    degisken=22
    print("Yereldeki: ",degisken)
    def ictekiFonksiyon():
        degisken=33
        print("İcteki fonksiyon",degisken)
    print("Yereldeki_2: ",degisken)
    ictekiFonksiyon()
    
fonksiyon1()
print("Globaldeki: ",degisken)

