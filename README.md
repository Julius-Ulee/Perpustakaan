# Perpustakaan
Sistem Peminjaman Buku di Perpustakaan

Tampilan Output: 
![image](https://github.com/Julius-Ulee/Perpustakaan/assets/61336116/e7594599-2317-4ec1-8140-451e79a09879)

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

## Support me as a programmer 
<table>
    <tr>
      <th>Rp. 5k Minimum</th>
      <th>Bitcoin</th>
    <tr>
      <td>
        <a href="https://saweria.co/AmeliaBotDiscord"><img title="💵 Saweria" src="https://user-images.githubusercontent.com/26188697/180601310-e82c63e4-412b-4c36-b7b5-7ba713c80380.png" alt="Donate For Amelia" height="41" width="174" /></a>
      </td>
      <td>
        <a href="https://julius-ulee.github.io/Donate/"><img title="🪙 Bitcoin" src="https://img.shields.io/badge/Bitcoin-EAB300?style=for-the-badge&logo=Bitcoin%20SV&logoColor=white" alt="Donate Via Bitcoin" height="41" width="174" /></a>
      </td>
    </tr>
  </table>

  ## Credits
  > make sure to credit me!
