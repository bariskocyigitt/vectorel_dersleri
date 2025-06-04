import os

mevcutlar=os.listdir()
dosyasayisi=0
dizinsayisi=0

for a in mevcutlar:
    # print(f"{a}\t{a.isfile()}")
    
    print(f"{ "Dosya" if os.path.isfile(a)==True else "Dizin"}\t{a}")
    if os.path.isfile(a): dosyasayisi+=1
    
    else: dizinsayisi+=1
    
print(f"{dosyasayisi} adet dosya, {dizinsayisi} adet klasor var")