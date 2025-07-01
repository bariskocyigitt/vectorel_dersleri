import hashlib
metin="Vektorel"
hash_obj=hashlib.sha256(metin.encode())
hash_str=hash_obj.hexdigest()

print("Veri tabanında kayıtlı sıfre",hash_str)

sifre=input("Sifre girin: ")
hash_obj= hashlib.sha256(sifre.encode())
sifre_hahsi= hash_obj.hexdigest()

print("Girilen sifreden üretilen hash değeri ",hash_str)


if hash_str==sifre_hahsi:
    print("sifre dogru")
else:
    print("Sifre yanlıs")
    