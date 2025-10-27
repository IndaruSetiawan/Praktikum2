a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan kedua: "))
c = int(input("Masukan bilangan ketiga: "))
d = int(input("Masukan bilangan keempat: "))


terbesar = a

if b > terbesar :
    terbesar = b
if c > terbesar :
    terbesar = c
if d > terbesar :
    terbesar = d

print("Bilangan terbesar adalah", terbesar)