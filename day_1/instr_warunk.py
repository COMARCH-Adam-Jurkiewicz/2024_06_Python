name = "Adam"
birth = int(input(f"{name} - podaj swój rok urodzenia: "))
age = 2024 - birth

# https://peps.python.org/pep-0008/#code-lay-out

if age >= 18:
    print("dorosłym być ciekawie")
    print("OK")
else:
    brakuje = 18 - age
    print(f"Brakuje ci jeszcze {brakuje} lat")