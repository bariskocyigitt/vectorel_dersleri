import datetime
saat= int(datetime.datetime.now().strftime("%H"))

def selamla():
    def sabah():
        return "Gunaydın. Saat:"+ str(saat)
    
    def ogle():
        return "İyi günler. Saat: " + str(saat)
    
    print("Merhaba\n", sabah() if  saat<9 else ogle())

selamla()
