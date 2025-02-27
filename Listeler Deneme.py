# sayilar = []
# import random
# for i in range(1000):
#     randoms = random.randint(1,10000)
#     sayilar.append(randoms)
# print(sayilar)
# sart = [num for num in sayilar if str(num).startswith("3") and str(num).endswith("7")]
# print(sart)
# print(len(sart))
# import time
#
# from Listeler import sayilar

from symbol import return_stmt


# sayi = int(input("Lütfen patron: "))
# fakt = 1
# for i in range(1,sayi+1):
#     fakt *= i
# print(fakt)
#
# fakt = 1
# sayi = int(input("Faktoriyel hesaplaması için bir sayı giriniz: "))
# for i in range(2,sayi+1):
#     fakt *= i
# print(fakt)
# n = [0,1]
# sayi = int(input("Fibonacinin kaç terimli olmasını istiyorsun"))
# t1= time.time()
# for i in range(sayi-2):
#     n.append(n[-1]+ n[-2])
# t2 = time.time()
# print(n)
# print(t2-t1)

# kelimeler = ["python", "java", "c", "golang", "ruby", "swift"]
# uzun_kelimeler = [i for i in kelimeler if len(i) >= 5 ]
# print(uzun_kelimeler)

#  1'den 50'ye kadar olan sayılarda:
#
# 3'e bölünenleri "Fizz",
# 5'e bölünenleri "Buzz",
# 3 ve 5'e bölünenleri "FizzBuzz" olarak yazdır


# for i in range(1,51):
#     if i %3 == 0:
#         print(f"3'e bölündüğü için: {i} = fizz")
#     elif i %5 == 0:
#         print(f"5' e bölündüğü için: {i} = buzz")
#     elif i %5 == 0 and i %3 == 0:
#         print(f"3'e ve 5'e bölündüğü için {i} = fizzbuzz")
#     else:
#         print(i)

# for i in range(1,51):
#     if i %3 == 0:
#         print(i)
#
# sayilar = [i for i in range(1,51) if i %3 == 0]
# print(sayilar)
#
# for num in range(2,101):
#     asal = True
#     for i in range(2,int(num**0.5)+1):
#         if num %i == 0:
#             asal = False
#             break
#     if asal:
#         print(num)

# for num in range(2, 101):  # 2'den 100'e kadar olan sayılar
#     asal = True  # Başlangıçta asal kabul edelim
#     for i in range(2, num):  # num'un kareköküne kadar olan sayılarla bölelim
#         if num % i == 0:  # Eğer tam bölünürse, asal değildir
#             asal = False
#             break  # Döngüyü kır
#     if asal:  # Eğer asal ise yazdıralım
#         print(num)

# sayi = int(input("Bir sayı giriniz: "))
#
# asal_sayi = [sayi for sayi in range(2,sayi+1) if all(sayi %i != 0 for i in range(2,int(sayi**0.5)+1))]
# print(asal_sayi)

# 1 ile 100 arasında sayılardan sadece 7'ye bölünebilen sayıları bulup bir listeye ekle.
# Bu listeyi ekrana yazdır.
# liste= []
# sart = [num for num in range(1,101) if num %7 == 0]
# liste.append(sart)
# print(liste)

# def topla(x,y):
#     return print(f"{x} + {y} = {x + y}")
# topla(3,5)

# def topla(x,y,z):
#     return print(f"{x}+{y}+{z} = {z+y+z}")
# topla(5,4,3)

# def iki_kati(liste):
#     return [i*2 for i in liste]
#
# sayilar = [1,2,3,4,5,6]
# sonuc = iki_kati(sayilar)
# print(sonuc)
#
# def toplam_cift(liste):
#     return sum(i for i in liste if i %2 == 0)
#
# liste1= [1,2,3,4,5,6,7,8,9]
#
# print(toplam_cift(liste1))


# Görev 1
# def toplam(x,y,z):
#     return x+y+z
# topla = toplam(2,3,4)
# print(topla)
# Görev 2
# import random
# def tek_sayi(liste):
#     return [i for i in liste if i %2 != 0]
# sayiler = [random.randint(1,100) for i in range(10)]
# tek_sayiler = tek_sayi(sayiler)
# print(tek_sayiler)

# def faktoriyel(liste):
#     return [int(input("bir sayı giriniz: "))]

import os

# Mevcut çalışma dizinini yazdır
print("Mevcut dizin:", os.getcwd())

# Yeni dizini belirt (RAW string veya çift ters çizgi kullan!)
yeni_dizin = r"C:\Users\Alismela\PycharmProjects\PythonProject\DenemeKlasörü"
# yeni_dizin = "C:\\Users\\Alismela\\PycharmProjects\\PythonProject\\DenemeKlasörü"  # Alternatif kullanım

# Çalışma dizinini değiştir
os.chdir(yeni_dizin)

# Yeni çalışma dizinini yazdır
print("Yeni çalışma dizin:", os.getcwd())

# Klasördeki dosyaları listele
for dosya in os.listdir():
    print(dosya)
print(os.listdir())