# urunFıyatları=[100,200,30]

# def yarıyaIndır(xx):
#     return xx//2

# yeniFiyatlar=[]

# for a in range(len(urunFıyatları)):
#     yeniFiyatlar.append(yarıyaIndır(urunFıyatları[a]))

# print(yeniFiyatlar)

urunFıyatları=[100,200,30]

def yariyaIndır(xx):
    return xx//2

yeniFıyatlar=list(map(yariyaIndır,urunFıyatları))

print(yeniFıyatlar) 

#lambda ile yapılmıs halı

# urunFıyatları=[100,200,30]
# yeniFıyatlar=list(map(lambda x:x//2,urunFıyatları))
# print(yeniFıyatlar)
