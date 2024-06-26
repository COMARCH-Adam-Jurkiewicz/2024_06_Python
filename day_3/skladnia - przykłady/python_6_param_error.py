# przeróbka na 2 parametry + pętla for z losowymi wartościami

# importy
from secrets import token_urlsafe
# choice - funkcja losująca element z kolekcji
# randint - losuje liczbę całkowitą
from random import choice, randint


# definicja funkcji
def my_file(extension: str, num_bytes=15) -> str:
    return token_urlsafe(num_bytes) + "." + extension


# błędne wywołanie funkcji
sercure_file = my_file(4, 3) # tu error!!!!
print(f"Bezpieczna nazwa pliku to: {sercure_file}")

# kod programu
# sercure_file = my_file("txt", 3)
# print(f"Bezpieczna nazwa pliku to: {sercure_file}")
# sercure_file = my_file("txt")
# print(f"Bezpieczna nazwa pliku to: {sercure_file}")

# zdefiniujemy pulę rozszerzeń do losowania
extensions = ("txt", "pdf", "docx", "xlsx", "odt", "jpeg")

# wykonujemy działania w pętli for

for _ in range(20):
    ext = choice(extensions)
    nb = randint(5,25)
    print(f"{my_file(ext, nb)=}")