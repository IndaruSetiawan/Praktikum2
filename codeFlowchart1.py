def cari_terbesar_sesuai_flowchart():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    c = float(input("Masukkan bilangan ketiga: "))

    Terbesar = None 

    if a > b and a > c:
        Terbesar = a
    elif b > a and b > c:
        Terbesar = b
    else:
        Terbesar = c

    print(f"Bilangan terbesar adalah: {Terbesar}")

cari_terbesar_sesuai_flowchart()