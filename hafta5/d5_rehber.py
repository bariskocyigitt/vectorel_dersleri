# Dosyaya bilgi kaydetme 

print("-"*10, "Kayıt İslemi","-"*10)
ad=input("Lütfen adınızı giriniz: ")
nu=input("Numaranız: ")
d=open(f"rehber.txt","a")
d.write(f"{ad}# {nu}# \n")

