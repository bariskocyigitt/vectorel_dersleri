d= open("rehber.txt") # 
print(d.read(5))
print(d.read(9))    
print(d.tell())

d.seek(3)
print(d.read(4))