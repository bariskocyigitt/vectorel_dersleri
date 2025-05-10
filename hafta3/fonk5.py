def topla(a,b):
    return a+b

def carp(a,b=1): #default parametre sonda olur 
    if a==0 or b==0:
        print("0 ile carpma")
    else: return a*b

x= topla(7,4)
print(topla(4,x))





def kereyaz(aa,bb=1):
    return aa*bb

print(kereyaz("Ankara ",5))