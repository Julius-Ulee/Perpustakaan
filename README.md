# Perpustakaan
Sistem Peminjaman Buku di Perpustakaan


1. Pendefinisian Class `Color`:

Kelas ini digunakan untuk memberikan warna pada teks yang akan ditampilkan di konsol.

2. Cetak Header Program:

Pada bagian ini, program mencetak header program perpustakaan digital yang terdiri dari judul program dan nama universitas.

3. Pendefinisian Class `Library`:

Kelas ini merupakan representasi dari perpustakaan digital. Dalam kelas ini terdapat beberapa metode, antara lain:
- `__init__(self, daftarbuku)`: Metode ini digunakan untuk menginisialisasi objek perpustakaan dengan daftar buku yang tersedia.
- `displaybukuTersedia(self)`: Metode ini digunakan untuk menampilkan daftar buku yang tersedia di perpustakaan.
- `lendbuku(self, permintaan_Buku)`: Metode ini digunakan untuk meminjam buku dari perpustakaan.
- `addbook(self, pengembalianbuku)`: Metode ini digunakan untuk mengembalikan buku ke perpustakaan.

4. Pendefinisian Class `Person` dan `Student`:

`Person` adalah kelas dasar yang memiliki beberapa metode untuk mengatur nama, NIM, dan password pengguna.
`Student` adalah kelas turunan dari `Person` yang memiliki metode khusus untuk meminjam dan mengembalikan buku.

5. Fungsi `tanya()`:

Fungsi ini digunakan untuk menanyakan kepada pengguna apakah ingin kembali ke menu utama atau keluar dari program.

6. Fungsi `main()`:

Fungsi ini adalah tempat dimulainya program. Di dalamnya, objek `Student` dibuat, dan pengguna diminta untuk memasukkan nama, NIM, dan password. Jika password yang dimasukkan sesuai dengan yang diharapkan ("1234"), maka pengguna dianggap berhasil login.

7. Fungsi `main2()`:

Fungsi ini merupakan menu utama program perpustakaan. Di dalamnya, objek `Library` dan `Student` dibuat. Pengguna dapat memilih opsi untuk melihat daftar buku, meminjam buku, mengembalikan buku, atau keluar dari program.

8. Pemanggilan Fungsi `main()` dan `main2()`:

Pada akhir kode, fungsi `main()` dan `main2()` dipanggil untuk menjalankan program.
