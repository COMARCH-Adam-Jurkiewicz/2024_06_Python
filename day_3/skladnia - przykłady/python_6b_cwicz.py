# importy - zbędne

# funkcje

def il_miejsc_w_samolocie(a, b):
    if (a*8 + b*5) > 100:
        return "Airbus"
    else:
        return "Boeing"

def bierz_liczbe(napis):
    while True:
        try:
            liczba = int(input(napis))
            return liczba
        except:
            print("Wprowadź liczbę całkowitą")

def pobieraj_liczby():
    while True:
        a = bierz_liczbe("Podaj liczbę a:")
        if a > 0:
            break
        else:
            print("Podaj liczbę dodatnią.")  # blok pętli

    while True:
        b = bierz_liczbe("Podaj liczbę b:")
        if b > 5:
            break
        else:
            print("Podaj liczbę dodatnią > 5.")   # blok pętli

    return a, b # koniec, zwracamy wartość


# kod programu

for _ in range(4):
    # pobieraj liczby
    a, b = pobieraj_liczby()
    typ_sam = il_miejsc_w_samolocie(a, b)
    print(f"Dla {a=} i {b=} -> {typ_sam=}")
