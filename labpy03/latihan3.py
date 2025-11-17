saldo = 1000000

print("Saldo saat ini: Rp", saldo)

while True:    
    print("1. Tarik Uang")
    print("2. Keluar")

    pilih = input("Pilih menu (1/2) : ")
    
    if pilih == '1':
        penarikan = int(input("Masukan jumlah penarikan: "))
        print("Penarikan berhasil!")
        print()
        sisa_saldo = saldo - penarikan
        print("Saldo saat ini :", sisa_saldo)

    else:
        print("Terima kasih telah menggunakan atm ini!")
        break