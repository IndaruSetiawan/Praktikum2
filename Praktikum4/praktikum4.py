def daftar_nilai():
    data_mahasiswa = [ ]
    
    while True:
        nama = input("Nama : ")
        nim = input("NIM : ")
        tugas = int(input("Nilai Tugas : "))
        uts = int(input("Nilai UTS : "))
        uas = int(input("Nilai UAS : "))

        data_siswa = {
            "nama": nama,
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas
        }
    
        data_mahasiswa.append(data_siswa)

        pilih = input ("Tambah Data(Y/T)?")
        if pilih.upper() != "Y":
            break

    return data_mahasiswa


def cetak_tabel(data_list):
    print("\n" + "="*78)
    print(f"| {'No':^3} | {'Nama':^15} | {'NIM':^10} | {'Tugas':^7} | {'UTS':^7} | {'UAS':^7} | {'Akhir':^7} |")
    print("="*78)

    for i, data in enumerate(data_list):
        print(f"| {i+1:^3} | {data['nama']:<15} | {data['nim']:^10} | {data['tugas']:^7} | {data['uts']:^7} | {data['uas']:^7} | {data['akhir']:^7.2f} |")
    print("="*78)

list_data = daftar_nilai()

for siswa in  list_data:
    nilai_akhir = (0.30 * siswa['tugas']) + (0.35 * siswa['uts']) + (0.35 * siswa['uas'])

    siswa['akhir'] = nilai_akhir

if list_data:
    cetak_tabel(list_data)
else:
    print("\nTidak ada data yang ditemukan.")