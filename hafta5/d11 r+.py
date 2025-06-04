try:
    with open("deneme44.dat","r+") as d:
        d.write("r+ ile acılan dosya. \n")

except Exception as h:
    print("Hata Olustu",h)
    open("deneme44.dat","w")