import time 

d=open("ornek.py")
o=d.readlines()
for aa in o:
    #print(a)
    #eval(aa)
    exec(aa)
    time.sleep(2)