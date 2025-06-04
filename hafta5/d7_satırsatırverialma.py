#Satır satır veri alma 
d=open("rehber.txt")
print("Okunan bilgiler")
okunan=d.readlines()
print(*okunan,sep="")

for a in okunan:
    satir=a.split("#")
    print(f"Ad: {satir[0]}, Numara: {satir[1]}")
    