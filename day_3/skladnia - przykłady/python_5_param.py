# napisz program, który wykorzysta : secrets.token_urlsafe
# program ma mieć funkcję o nazwie my_file() która ma pytać usera o
# ilość bitów 4 .. 20 i generować bezpieczną nazwę pliku i zwracać ją

# importy
from secrets import token_urlsafe


# definicja funkcji
def my_file(extension):
    while True:
        try:
            # liczba całkowita, więc funkcja int() - integer
            num_bytes = int(input("Daj ilość bajtów 4..20: "))
            # jeśli liczba bajtów odpowiednia
            if 4 <= num_bytes <= 20:
                # zwracamy nazwę pliku i kończymy działanie funkcji
                # nazwa pliku jako f-string, rozszerzenie z parametru
                return f"{token_urlsafe(num_bytes)}.{extension}"
        except:
            print("Jakiś błąd....")


# kod programu
sercure_file = my_file("txt")
print(f"Bezpieczna nazwa pliku to: {sercure_file}")
