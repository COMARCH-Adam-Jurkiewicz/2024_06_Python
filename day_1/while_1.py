number = 1
while number < 10000000:
    print(f"Kolejny: {number}")
    number += 1
    if number > 20000:
        number = "Koniec"