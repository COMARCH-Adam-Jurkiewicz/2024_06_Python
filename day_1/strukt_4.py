ile = int(input("Podaj ilośc elementów: "))
lista = []
print(f"Start: {lista}")

for number in range(ile):
    adding = input(f"Podaj wartość dla indeksu {number}: ")
    lista.append(adding)
    print(f"Aktualnie: {lista}")

print(f"Koniec: {lista}")
# len(lista) - ilośc elementów

# na końcu jeśli lista > 5 elemntów to info, że duża

