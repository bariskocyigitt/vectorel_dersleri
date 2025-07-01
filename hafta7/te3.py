try:
    a=5000
    b="6000"
    print(a+b)
    
except Exception as aa:
    print("Hata olustu ")
    print("Hata kodu ",aa)
    if str(aa)== "division by zero ": print("bolme ıslemınde bolen 0 ")
    if str(aa)== "unsupported operand type(s) for + : 'int' and 'str' " :
        print("+ islemi icin ikiside string ya da ikiside int olmalı ")