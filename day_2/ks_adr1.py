adrb = [
    ("Adam ", "Jurkiewicz", "662144425"),
    ("Beata", "Jurkiewicz", "454355234"),
    ("Artur", "Jurkiewicz", "754355433"),
]

zmadrb = []

for number in adrb:
    print(f"{number=}")
    print(f"Osoba: {number[0]} o nazwisku {number[1]} ma nr telefonu {number[2]}")
    imie, nazwisko, telefon = number
    print(f"Osoba: {imie} o nazwisku {nazwisko} ma nr telefonu {telefon}")
    zamiana = (nazwisko, telefon, imie) # tworzenie tupli
    print(f"{zamiana=}")
    zmadrb.append(zamiana)

print('-----------------')
print(f"{adrb=}")
print(f"{zmadrb=}")