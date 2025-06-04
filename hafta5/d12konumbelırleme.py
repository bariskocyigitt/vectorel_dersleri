import os
print(os.getcwd()) #calısılan klasoru gosterır
yol=os.getcwd().split("\\")
print(yol,len(yol))



print(yol[:len(yol)-1],len(yol)-1)
print("\\".join(yol[0:len(yol)-1]))      
