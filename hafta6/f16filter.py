# sayilar=[11,22,3,6,7]

# yeniDizi= list(filter(lambda x:x%2==0,sayilar))

# print(yeniDizi)

# sayilar=[11,20,3,6,7,45,40]

# def tekMi(xx):
#     return xx%2==1
# yeniDizi=list(filter(tekMi,sayilar))

# print(yeniDizi)

# -------------filtersiz1

# sayilar=[11,22,3,6,8]

# def tekMi(xx):
#     if xx%2==0 : return False
#     else: return True

# yeniDizi=[]
# for a in sayilar:
#     yeniDizi.append(tekMi(a))

# print(yeniDizi)


# filtersiz1

sayilar=[11,22,3,6,8]

def tekMi(xx):
     if xx%2==0 : return True
   
     
yeniDizi= list(filter(tekMi,sayilar))

print(yeniDizi)
