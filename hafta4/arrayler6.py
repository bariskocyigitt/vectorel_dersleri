sozluk={
    
    "fil": "elephant",
    "köpek": "dog",
    "kedi": "cat",   
    
}

print(sozluk["köpek"])

ogrenciler= {
    "ogrenci1":{
        "adi":"Baris",
        "soyadi":"Kocyigit",
        "num":"889",
    },
    
    "ogrenci2":{
        "adi":"Mercan",
        "soyadi":"Kara",
        "num":"123",
    },
    "kullanici_turu":("Ticari","Bireysel"),
    
    "Barış":""
}

#print(ogrenciler)
print(ogrenciler["ogrenci2"])
print(ogrenciler["ogrenci2"]["soyadi"])
print(ogrenciler["kullanici_turu"])
print(ogrenciler["kullanici_turu"][1])

