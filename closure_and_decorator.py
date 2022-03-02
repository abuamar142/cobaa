def hitung_luas(a, t):
    luas = 1/2 * a * t
    print(luas)

def check_number(func):
    def inner(a, t):
        if a < 5:
            print("alas kurang dari 5, maka diganti dengan 5")
            a = 5
        if t < 5:
            print("tinggi kurang dari 5, maka diganti dengan 5")
            t = 5
        return func(a, t)
    return inner

hitung_luas(4, 8)
