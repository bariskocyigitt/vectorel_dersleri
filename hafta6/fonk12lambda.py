# sayilar= [11,22,3]
# def carp(xx):
#     return xx*2
# yeniDizi= list(map(carp,sayilar))
# print(yeniDizi)

sayilar=[11,22,3]
print(list(map(lambda a:a*2,sayilar)))

# def fonksiyon(x):
#     return x*2
# print(fonksiyon("Merhaba "))

print((lambda x:x*2)("Merhaba "))
