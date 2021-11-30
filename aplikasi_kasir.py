# 1. Nama program
print("="*50)
print("===== Program Kasir =====".center(50))
print("="*50)

# 2. Login user
print("Silahkan login terlebih dahulu..!!".center(50))
def login():
  user = input("\nUsername \t = ")
  sandi = input("Password \t = ")
  # Masukkan username dan password yang anda ingnkan untuk login ke aplikasi di bawah ini (didalam tanda petik.!)
  if (user == "admin" and sandi == "admin"):
    print("\n","Selamat datang Admin...!".center(50))
  else:
    print("\nUsername atau Password yang anda masukkan salah.\nMasukkan kembali..!!")
    login()
login()

# 3. Data barang di toko
print("="*50)
print("===== Data Barang dan Harga =====".center(50))
print("="*50)

# 3.1 Isikan data makanan disini
data_makanan = [
  [1,"Gorengan",500],
  [2,"Nasi Telur",7000],
  [3,"Nasi Ayam",9000]
  ]

# 3.2 Isikan data minuman disini
data_minuman = [
  [11,"Air Putih",0],
  [12,"Es Teh",2500],
  [13,"Es Susu",3000],
  [14,"Es Teh Susu",4000]
  ]

# 3.3 Menampilkan data makanan dan minuman di terminal
print("Makanan".center(50))
print("=========".center(50))
for makanan in data_makanan:
  print(f"{makanan[0]}. {makanan[1]} = {makanan[2]}".center(50))

print(("="*25).center(50))

print("Minuman".center(50))
print("=========".center(50))
for minuman in data_minuman:
  print(f"{minuman[0]}. {minuman[1]} = {minuman[2]}".center(50))

print("="*50)

# 3.4 Menggabungkan semua menu

data_makanan.extend(data_minuman)
menu = data_makanan
total_menu = len(menu)

# 4. Merekap pesanan

pesanan = []
jumlah_pesanan = []
def pesan():
  pilih = int(input("Masukkan nomor menu satu persatu --> "))
  if 0 < pilih <= total_menu:
    pesanan.append(pilih)
    print(f"Anda memesan '{(menu[pilih - 1])[1]}'")
    jumlah = input("Jumlah --> ")
    jumlah_pesanan.append(jumlah)
    pesan()
  elif pilih < 0 or pilih > total_menu or " ":
    print(f"=== Pesanan Anda ===".center(50))
    print(pesanan)
    total_pesanan = len(pesanan)
    print(total_pesanan)
    for x in range(0,total_pesanan):
      harga = (menu[pesanan[x - 1]])[2] * jumlah_pesanan[total_pesanan[x - 1]]
      print(f"{(menu[pesanan[x - 1]])[1]} = {(menu[pesanan[x - 1]])[2]} x {jumlah_pesanan[total_pesanan[x - 1]]} = {harga}") 
pesan()
