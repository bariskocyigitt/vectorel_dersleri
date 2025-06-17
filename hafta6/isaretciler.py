a=[2,4,1,6]
b=[3,2,5,1]
c=a #c dizisi bir isaretci a nın yerine isaret eder 
d=c[:]

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)

c[1]="h"
print('\nc[1]="h" sonrası ')
print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)