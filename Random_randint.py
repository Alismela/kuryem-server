import random

sayilar = [random.randint(1, 100) for _ in range(10)]

# Çift sayıları filtreleme
cift_sayilar = list(filter(lambda x: int(str(x)) % 2 == 0, sayilar))

# Karelerini alma ve yeni listeye ekleme işlemi
karecift = [num ** 2 for num in cift_sayilar]

print(karecift)