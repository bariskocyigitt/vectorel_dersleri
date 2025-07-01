#1. Basit fonksiyonlar 
# def selamla():
#     print("="*10,"Merhaba","="*10)
#     print(" "*10,"nasılsın")
# selamla()


# 2. Parametre alan fonksiyonlar 
# def selamla(xx): #basit fonksiyon örneği
#     print("="*10,xx,"="*10)
#     print(" "*10,"nasılsın \n")

# selamla("Selam")
# selamla("Merhaba")

#3. Deger donduren fonksiyonlar 
def selamla(xx):
    return f"{'='*10} {xx} {'='*10} \n{' '*10}nasılsın\n"

selamla("Selam") #calısmaz/calısır fakat goruntulenmez
print(selamla("Merhaba"))