#re = Regular Expression = Düzenli ifadeler
import re 
xxx="guzel Ahmet al renkli guzel bir salı hemen aldı"

# tüm ifadelerin listesi
print(re.findall("al",xxx))

#sal ifadesini tara 
print(re.search("sal",xxx))

#al a göre bol 
print(re.split("al",xxx))

#boslukları zzz yap 
print("metındekı guzel ıfadelerı yerıne ıyı yaz " ,re.sub("guzel","ıyı",xxx))

