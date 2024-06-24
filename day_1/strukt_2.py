alfabet = "abcdefghijklmnoprstuwxyz"

for letter in alfabet:
    print(f"Literka: {letter}")
    if letter == "e":
        print("Znaleziono e")
    if letter in "aeiouy":
        print("to jest samogłoska")