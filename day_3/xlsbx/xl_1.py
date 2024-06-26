# import
from pyxlsb import open_workbook

# do zmiany na plik inny
nazwa_xlsb = "test.xlsb"

# otwieramy arkusz - menadżer kontekstowy:
with open_workbook(nazwa_xlsb) as arkusz_excel:
    # blok kodu z otwartym do odczytu plikiem
    print(f"{arkusz_excel.sheets=}")   # "DANE"
    # otwieramy konkretny arkusz z otwatego pliku xlsb
    with arkusz_excel.get_sheet("DANE") as sheet:
        # iterujemy po wszystkich wierszach arkusza...
        for wiersz in sheet.rows():
            # print(f"{wiersz=}")

            # generator listowy - tworzy listę wartości wiersza z SHEET
            values = [element.v for element in wiersz]
            # generuję statys - kolumna 24 + 25
            status = f"{values[24]}_{values[25]}"
            print(f"{status=}")


# koniec otwarcia - zamknięty plik
print("Koniec")