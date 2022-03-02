def hitung_luas(a, t):
    luas = 1/2 * a * t
    return luas

def check_number(func):
    def inner(a, t):
        if a < 5:
            print("alas kurang dari 5, maka diganti dengan 5")
            a = 5
        if t < 5:
            print("tinggi kurang dari 5, maka diganti dengan 5")
            t = 5
        func(a, t)
    return inner

segitiga_1 = check_number(hitung_luas(3,10))
segitiga_1()