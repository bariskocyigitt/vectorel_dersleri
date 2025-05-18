renkler= ["al","gok","mor"]
renkler.append("boz")
print(renkler[1])

musteri_turleri= ("Ticari","Bireysel") #tupple tur dızıler degısmez
# append yapamıyoruz
print(musteri_turleri[1])
# musteri_turleri +=musteri_turleri1 yapabiliriz renkler içinde yapabilriz

renkler.pop()
renkler.remove("al")
print(renkler)


kullanici_turu= {"idareci","ogretmen","veli","ogrenci"}
print(kullanici_turu)
print(*kullanici_turu)

kullanici_turu.add("ogretmen")
print(kullanici_turu)