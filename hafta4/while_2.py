import random
puan=0
while True:
    s1= random.randint(1,100)
    s2= random.randint(1,100)
    cevap= int(input(f"{s1}+{s2} toplamı kac? "))
    #if input(f"{s1}+{s2} toplamı kac? ")==s1+s2:
    if cevap=="":
        print(f"Hoscakal, seni {puan} puan ile ugurluyoruz. ")
        break
    if int(cevap)==s1+s2:
        puan +=10
        print("Bildin puanın: ",puan)
    else:
        puan -=10
        print("Bilemedin puanın", puan) 