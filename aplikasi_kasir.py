# 0 import
import os

# 0.1 lebar program
lebar = 50

# 0.2 data toko
nama_toko = "Toko Bagus"
alamat_toko = "Jl. Ahmad Yani No. 145, Karangkidul"
alamat_toko_2 = "Kec. Semarang Tengah, Kota Semarang"
nomor_telepon = "021-00000"

# 1. judul
print("-" * lebar)
print("== Program Kasir ==".center(lebar))


# 2. login
def login():
    print("-" * lebar)
    username = input("Username\t--> ")
    password = input("Password\t--> ")
    # Masukkan username dan password untuk toko dibawah ini. Didalam tanda petik
    if username == "admin" and password == "admin":
        os.system("clear")
    else:
        print("Masukkan salah...!!!".center(lebar))
        login()


# 3. daftar barang
daftar_barang = [
  ["Kertas A4", 50000],
  ["Klip", 7000],
  ["Map", 25000],
  ["Penghapus", 4000],
  ["Penggaris", 11000],
  ["Bolpen", 36000],
  ["Pensil", 12000],
  ["Stapler", 8000],
  ["Serutan", 5000],
  ["Tinta Printer", 45000]
  ]

# 3.1 jumlah total Barang
jumlah_total_barang = len(daftar_barang)


# 3.2 menampilkan daftar barang
def tampilan_daftar_barang():
    print("-" * lebar)
    print("|"," === Daftar Barang === ".center(46),"|")
    print("-" * lebar)
    for x in range(jumlah_total_barang):
      print(f"|{x + 1}.".ljust(4), # nomor barang
      f"{daftar_barang[x][0]}  ".ljust(20,"-"), # nama barang
      "=",
      f"  Rp.{(daftar_barang[x][1]):,}  ".ljust(20,"-"), # harga barang 
      "|")
    print("-" * lebar)
    print("Masukkan '0' untuk merekap pesanan ..!!".center(lebar))

# 4. barang yang dibeli
barang_yang_dibeli = []
jumlah_dari_barang_yang_dibeli = []
total_dari_total_harga_perbarang = []


#def hapus_data():
#    barang_yang_dibeli.clear()
#    jumlah_dari_barang_yang_dibeli.clear()
#    total_dari_total_harga_perbarang.clear()


def byd():
  print("-" * lebar)
  barang = int(input("Masukkan nomor barang --> "))
  if barang in range(1, jumlah_total_barang + 1):
    barang_yang_dibeli.append(barang)
    def jdbyd():
      jumlah = int(input("Masukkan jumlah --> "))
      if jumlah >= 1:
        jumlah_dari_barang_yang_dibeli.append(jumlah)
        print(f"= {daftar_barang[barang - 1][0]} sebanyak {jumlah} =".center(lebar))
        byd()
      else:
        jdbyd()
    jdbyd()
  elif barang == 0:
    print("-" * lebar)
  else:
    byd()

# 5. menampilkan struk belanja
def struk_belanja():
    
    total_jumlah_barang_yang_dibeli = len(barang_yang_dibeli)
    
    print("=" * lebar)
    print(f"== {nama_toko} ==".center(lebar))
    print("-" * lebar)
    print(alamat_toko.center(lebar))
    print(alamat_toko_2.center(lebar))
    print(nomor_telepon.center(lebar), "\n")

    for x in range(total_jumlah_barang_yang_dibeli):

      total_harga_perbarang = (jumlah_dari_barang_yang_dibeli[x]) * (daftar_barang[barang_yang_dibeli[x] - 1][1])

      total_dari_total_harga_perbarang.append(total_harga_perbarang)
        
      print(f"{daftar_barang[barang_yang_dibeli[x] - 1][0]}".ljust(20),
      f"{jumlah_dari_barang_yang_dibeli[x]} x {daftar_barang[barang_yang_dibeli[x] - 1][1]}".ljust(12),"=",
      f"{(total_harga_perbarang):,}".rjust(14))
    
    print("Total  ".ljust(37,"-"),
      f"{(sum(total_dari_total_harga_perbarang)):,}".rjust(12))


# 6. pembayaran
def pembayaran():
    uang = int(input("Masukkan uang --> "))
    if uang > sum(total_dari_total_harga_perbarang):
        print(f"Kembalian --> Rp.{(uang - sum(total_dari_total_harga_perbarang)):,}".center(lebar))
    elif uang == sum(total_dari_total_harga_perbarang):
        print("Uang anda PAS".center(lebar))
    else:
        pembayaran()

# 7. penutup
def terima_kasih():
    print("-" * lebar)
    print("Terima kasih atas kunjungan Anda".center(lebar))
    print("Selamat datang kembali".center(lebar))
    print("=" * lebar)


# 8. run program
login()
tampilan_daftar_barang()
byd()
struk_belanja()
pembayaran()
terima_kasih()
