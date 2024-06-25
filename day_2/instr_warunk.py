from datetime import datetime
czas = datetime.now()
print(f"{czas=}")
rok = czas.year
name = "Adam"
birth = int(input(f"{name} - podaj swój rok urodzenia: "))
age = rok - birth

# https://peps.python.org/pep-0008/#code-lay-out

if age >= 18:
    print("dorosłym być ciekawie")
    print("OK")
else:
    brakuje = 18 - age
    print(f"Brakuje ci jeszcze {brakuje} lat")