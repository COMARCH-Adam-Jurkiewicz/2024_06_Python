# importy - zbędne

# funkcje

def il_miejsc_w_samolocie(a, b):
    # oblicz il. miejsc w samolocie = (a*8 + b*5)
    # jeśli il. miejsc > 100, to zwróc napis "Airbus", w iinym przypadku
    # zwróć napis "Boeing"

def pobieraj_liczby():
    # pobierze od usera 2 liczby: a,b
    # jeśli obie będą > 0, to return a,b

# kod programu

for _ in range(4):
    # pobieraj liczby
    a,b = pobieraj_liczby()
    typ_sam = il_miejsc_w_samolocie(a, b)
    #  wyświetl napis o typie samolotu : A.., B...
