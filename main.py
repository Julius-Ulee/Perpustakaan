# PERPUSTAKAAN DIGITAL

program = "-----PERPUSTAKAAN DIGITAL-----"
univ = "UNIVERSITAS BINA SARANA INFORMATIKA"
str_program = program.center(70)
str_univ = univ.center(70)

class Color:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(Color.BLUE + '='*70 + Color.END)
print(Color.PURPLE + Color.BOLD + str_program + Color.END)
print(Color.PURPLE + str_univ + Color.END)
print(Color.BLUE + '='*70 + Color.END)
print(Color.BOLD + 'Selamat Datang !' + Color.END)

import sys

class Library:
    def __init__(self, daftarbuku):
        self.bukutersedia = daftarbuku

    def displaybukuTersedia(self):
        print("\n" + Color.BOLD + Color.CYAN + "=" * 50)
        print("<<<<<<<<DAFTAR BUKU PERPUSTAKAAN>>>>>>>>")
        print("=" * 50 + Color.END)
        for buku in self.bukutersedia:
            print(buku)
            print("-" * 50)

    def lendbuku(self, permintaan_Buku):
        if permintaan_Buku in self.bukutersedia:
            print(Color.GREEN + Color.BOLD + ">"*50)
            print("Buku telah berhasil kamu pinjam")
            import datetime
            x = datetime.datetime.now()
            print("Waktu peminjaman: ", x)
            print(">" * 50 + Color.END)
            print(Color.RED + """
+------------------------------------+
| NOTE :                             |
|------------------------------------|
| TOLONG KEMBALIKAN BUKU TEPAT WAKTU |
| DAN DALAM KEADAAN BAIK!            |
+------------------------------------+
                              """ + Color.END)
            self.bukutersedia.remove(permintaan_Buku)
        else:
            print("Maaf buku yang kamu minta sedang tidak tersedia")

    def addbook(self, pengembalianbuku):
        self.bukutersedia.append(pengembalianbuku)
        print(Color.PURPLE + ">" * 50)
        print(Color.BOLD + "Terimakasih kamu telah berhasil mengembalikan buku!")
        import datetime
        x = datetime.datetime.now()
        print("Waktu Pengembalian: ", x)
        print(">" * 50 + Color.END)
        print(Color.GREEN + """
+-----------------------------------+
|                                   |
|  TERIMAKASIH TELAH MEMINJAM BUKU  |
|  DI PERPUSTAKAAN DIGITAL!         |
|                                   |
+-----------------------------------+
                              """ + Color.END)

class Person:
    def setName(self, a):
        self.nama = a

    def setNim(self, b):
        self.nim = b

    def setPassword(self, c):
        self.password = c

    def getPassword(self):
        if self.password == "1234":
            print(Color.YELLOW + "<"*15, "Selamat",
                  self.nama, "Kamu Berhasil Login!", ">"*15 + Color.END)
            print("-"*70)
        else:
            print(Color.RED + "\nERROR! Password Yang Anda Masukan Salah!")
            exit()

class Student(Person):
    def pinjambuku(self):
        print("Ketik Judul Buku yang ingin kamu pinjam: ")
        self.buku = input()
        return self.buku

    def kembalikanbuku(self):
        print("Ketik Judul Buku yang ingin dikembalikan: ")
        self.buku = input()
        return self.buku

def tanya():
    tanya = input('\n'+Color.GREEN + 'Kembali ke Menu Utama? (y/n)>>')
    if tanya == 'y' or tanya == 'Y':
        main2()
    elif tanya == 'n' or tanya == 'N':
        exit()
    else:
        print('Input Salah')
        print('Masukan Input Dengan Benar')
        exit()

def main():
    obj = Student()
    obj.setName(input("Masukan Nama:"))
    obj.setNim(int(input("Masukan NIM:")))
    obj.setPassword(input("Masukan Password:"))
    obj.getPassword()

def main2():
    library = Library([
        Color.PURPLE + "Laskar Pelangi",
        "ANjay", "eaea", "hoo", "18+", "bioskop",
        "Bumi", "Programming", "Akuntansi Dasar",
        "Buku Sastra dan Bahasa" + Color.END
    ])
    student = Student()
    done = False
    while not done:
        print(Color.CYAN + Color.BOLD + """
        +------------------------------+
        |          MENU UTAMA          |
        |------------------------------|
        | [1] Tampilan Daftar Buku     |
        | [2] Pinjam Buku              |
        | [3] Kembalikan Buku          |
        | [4] Exit                     |
        +------------------------------+
        """)

        choice = int(input("Pilih menu: " + Color.END))
        if choice == 1:
            library.displaybukuTersedia()
            tanya()
        elif choice == 2:
            library.lendbuku(student.pinjambuku())
            tanya()
        elif choice == 3:
            library.addbook(student.kembalikanbuku())
            tanya()
        elif choice == 4:
            sys.exit()

    tanya()
    Person()

main()
main2()
