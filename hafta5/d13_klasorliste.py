#klasordekıler listesi 
import os


mevcutlar= os.listdir()
for a in mevcutlar:
    # print(a)
    # print(a,a.endswith(".txt"))
    
    if a.endswith(".txt"):
        print(a)
        
    