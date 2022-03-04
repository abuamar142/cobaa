a = float(input("Masukkan alas segitiga: "))
t = float(input("Masukkan tinggi segitiga: "))

def check_number(func):
    "untuk check alas dan tinggi, jika kurang dari 5 akan diganti dengan 5"
    def inner(a, t):
        if a < 5:
            print("Alas kurang dari 5, maka diganti dengan 5")
            a = 5
        if t < 5:
            print("Tinggi kurang dari 5, maka diganti dengan 5")
            t = 5
        return func(a, t)
    return inner

@check_number
def hitung_luas(a, t):
    "function untuk menghitung luas dari segitiga"
    luas = 1/2 * a * t
    return luas

segitiga = hitung_luas(a, t)

print(f"Luas dari segitiga : {round(segitiga)}")