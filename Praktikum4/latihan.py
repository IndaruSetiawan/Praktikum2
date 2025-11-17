a = [1, 2, 3, 4, 5]

print(f"List awal : {a}" )
print()

#akses list
print(f"Elemen ke 3 : {a[2]}")
print(f"Elemen ke 2-4 : {a[1:4]}")
print(f"Elemen terakhir : {a[-1]}")
print()

#ubah elemen list
a[3] = 19
print(f"Setelah mengubah elemen ke 4 : {a}")

a[3:] = (1, 27)
print(f"Setelah mengubah elemen ke 4 - terakhir : {a}")
print()

#tambah elemen list
b = a[0:2]
print(f"List B : {b}")

b.append("HelloWorld!")
print(f"List B + String : {b}")

b.extend([9,8,7])
print(f"LIST B + 3 nilai : {b}")

gabungan = a + b
print(f"List gabungan(a + b) : {gabungan}")