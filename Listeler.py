with open('ornek.txt','w') as dosya:
    dosya.write('Merhaba, Python!')
with open('ornek.txt','r') as dosya:
    icerik = dosya.read()
    print(icerik)


# # Dosya yazma
# with open('ornek.txt', 'w') as dosya:
#     dosya.write("Merhaba, Python!")
#
# # Dosya okuma
# with open('ornek.txt', 'r') as dosya:
#     icerik = dosya.read()
#     print(icerik)  # Çıktı: Merhaba, Python!


