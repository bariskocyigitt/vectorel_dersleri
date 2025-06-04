# a modunda acınca append/ekleme önceki verilere zarar gelmez 
# w modunda acılınca dosya yeniden olusturuldugu için önceki veriler silinir 
for a in range(10,20):
    d=open(f"deneme{a}.txt","a")
    d.write(f"{a}numaralı dosya. ")
    