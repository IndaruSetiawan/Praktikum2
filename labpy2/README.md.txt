Lab 2 : Struktur Kondisi 
	1. Latihan 1
		Program dimulai dengan meminta user memasukan empat bilangan. Bilangan pertama disimpan di variabel a, bilangan kedua di variabel b, bilangan ketiga di variabel c, dan bilangan keempat di variabel d. Program membuat variabel baru bernama terbesar. Variabel terbesar menganggap a sebagai bilangan terbesar sementara. Lalu, program mulai membandingkan terbesar dengan bilangan lainnya. Jika, b lebih besar dari terbesar maka nilai terbesar akan diganti sama dengan b. Jika tidak, nilainya akan tetap dan program akan melakukan pengecekan sampai variabel d. Setelah semua perbandingan selesai,variabel terbesar akan bernilai bilangan yang user masukan yang terbukti paling besar diantara 4 bilangan tersebut. Program akan menampilkan terbesar dan program selesai.

	2. Latihan 2
		Program dimulai dengan meminta user memasukan tiga bilangan. Bilangan pertama disimpan di variabel a, bilangan kedua di variabel b, dan bilangan ketiga di variabel c. Program membuat variabel baru bernama data. Variabel data digunakan oleh program untuk menampung hasil variabel a, b, dan c. Karena data masih belum berurutan, maka program menjalankan perintah .sort untuk membuat data menjadi berurutan. Setelah berurutan, program akan menampilkan data dan program selesai.



Lab 3 : Perulangan
	1. Latihan 1
		Program dimulai dengan menjalankan nested loop atau perulangan bersarang. Perulangan pertama menggunakan variabel row dengan nila 0 sampai 9. Di dalamnya terdapat perulangan kedua menggunakan variabel column dengan nilai yang sama. Setiap perulangan dijalankan,program akan menampilkan penjumlahan row+column pada baris yang sama. Lalu program menjalankan perintah end=" " agar hasilnya tidak berpindah ke baris baru. Setelah perulangan column selesai, program menjalankan print("\n") untuk berpindah ke baris berikutnya. Terakhir, program akan menampilkan hasil semua perulangan dan penjumlahan, kemudian program selesai.
	
	
	2. Latihan 2
		Program dimulai dengan mengimpor modul random yang digunakan untuk menghasilkan bilangan acak. Lalu, program meminta user untuk memasukan sebuah bilangan dan menyimpannya di variabel n. Nilai n akan menentukan berapa banyak bilangan acak yang ingin ditampilkan. Program membuat variabel baru bernama count dengan nilai 0. Kemudian, program menjalankan perulangan for i in range(n) yang akan melakukan pengulangan sebanyak n kali. Di dalam perulangan for, terdapat while True yang akan berjalan  terus menerus sampai kondisi tertentu terpenuhi. Selanjutnya, program akan memeriksa apakah angka < 0.5. Jika kondisi tersebut benar, maka program akan menampilkan nilai angka, menambah nilai count sebanyak 1, dan menghentikan perulangan while dengan perintah break agar Kembali ke perulangan for. Proses akan berulang hingga perulangan for selesai dijalankan sesuai dengan jumlah yang diminta user. Setelah semua bilangan acak ditampilkan, program selesai.