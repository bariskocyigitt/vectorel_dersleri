#Dosyadan veri alma 

print("Kayıt Islemi")
d= open("rehber.txt") #dosya tipi yazılmazsa r olarak kabul eder 
print("Okunan bilgiler: ")
print(d.read())