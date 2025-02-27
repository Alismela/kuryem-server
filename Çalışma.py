# with open('yazi.txt', 'w') as dosya:
#     dosya.write("Merhaba Python!")
# with open('yazi.txt', 'r') as dosya:
#     icerik1= dosya.read()
#     print(icerik1)
#
# with open("yazi.txt", "a") as dosya:
#     dosya.write("\nBu satır dosyanın sonuna eklendi!")
# with open('yazi.txt', 'r') as dosya:
#     icerik2 = dosya.read()
#     print(icerik2)
# with open('yazi.txt', 'w') as dosya:
#     dosya.write("Merhaba Python!")  # Buraya yazdırma fonksiyonu eklendi
#
# with open('yazi.txt', 'r') as dosya:
#     icerik1 = dosya.read()
#
#
# with open("yazi.txt", "a") as dosya:
#     dosya.write("\nBu satır dosyanın sonuna eklendi!")  # Ek satır eklendi
#
# with open('yazi.txt', 'r') as dosya:
#     icerik2 = dosya.read()
#     print(icerik2)  # Son hali ekrana yazdırıldı
#
#
#
import random


# Kullanıcıdan alınan 3 sayıyı bir dosyaya yazdıran ve daha sonra bu dosyayı okuyarak ekrana yazdıran bir Python programı yaz.
#
# Kullanıcıdan alınan bir metni bir dosyaya yaz ve ardından aynı dosyadan okuduğun metni ekrana yazdır. Bu sefer dosyanın başına yeni bir satır ekleyin.
#
# Mevcut bir dosyaya yeni satırlar ekleyin ve ekledikten sonra dosyayı okuyarak ekrana yazdırın.
# sayilar = []
# for i in range(3):
#     sayi = int(input("Sayı giriniz"))
#     sayilar.append(sayi)
#
# with open('dosya.txt', 'w') as dosya:
#     dosya.write(str(sayilar) +"\n")
#
# with open('dosya.txt', 'a') as dosya:
#     dosya.write(f"{sayilar} 3 adet sayı dosyaya eklendi\n")
#
#
# metin = input("Bir metin giriniz")
# with open('dosya.txt', 'a') as dosya:
#     dosya.write(metin+"\n")
#
# with open('dosya.txt', 'r') as dosya:
#     icerik = dosya.read()
#     print(icerik)

# Kullanıcıdan isim, yaş ve meslek bilgilerini al.
# 2️⃣ Bu bilgileri bir sözlük içine kaydet.
# 3️⃣ Bu sözlüğü JSON formatında bir dosyaya yaz.
# 4️⃣ Dosyadan tekrar oku ve ekrana yazdır.



# import json
# kullanici_bilgileri = {}
# kullanici_bilgileri.update({
#     "İsim" : input("İsminizi giriniz: "),
#     "Yaş"  : input("Yaşınızı giriniz: "),
#     "Meslek": input("Mesleğinizi giriniz: ")
# })
# with open('kullanici_bilgileri','w') as dosya:
#     json.dump(kullanici_bilgileri, dosya)
# with open('kullanici_bilgileri', 'r') as dosya:
#     icerik = json.load(dosya)
#     print(icerik)
# liste = []
# for i in range(5):
#     sayilar = int(input("Sayı giriniz:"))
#     liste.append(sayilar)
# liste = list(reversed(liste))
# print(liste)
#
# import random
def kontrol():
    liste = [random.randint(1,1000) for _ in range(100)]
    print(liste)
    sayi = int(input("Bir sayı giriniz: "))
    for i in liste:
        if sayi not in liste:
            return "Sayı listede mevcut değil"
        else:
            return f"{sayi}'sayısının listedeki indexi = {liste.index(sayi)}"
sayihesapla = kontrol()
print(sayihesapla)

