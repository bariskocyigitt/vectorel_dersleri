xx=11

def fonksiyon1():
    global xx
    xx=22
    print("Yereldeki: ",xx)
    def ictekiFonksiyon():
        global xx
        xx=33
        print("İcteki fonskiyon: ",xx)
    ictekiFonksiyon()
    print("Yereldeki_2: ",xx)

fonksiyon1()
print("Globaldeki: ",xx)