try: x=10/2
except ZeroDivisionError:
    print("Sıfıra bolme hatası olustu")
else:
    print("Hata olusmadı, islem basarılı !")

#hata kodunu alma 

try: x=10/0
except ZeroDivisionError as e:
    print(f"Hata olustu: {e}")
    