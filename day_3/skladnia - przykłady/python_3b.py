import math  # import całego modułu
# from math import sin, radians  # import tylko 1 funkcji z modułu


# spytać usera o ilość stopni - funkcja zapisana przez nas
def get_degrees():
    while True:
        try:
            stopnie = float(input("Pdaj nam stopnie do sinusa: "))
            # jeśli user wprowadził poprawną liczbę to koniec
            if 0 <= stopnie <= 360:
                break # przeskoczy do wiersza 16
        except:
            print("Źle wprowadzono wartość stopni.")

    print(f"Wprowadzono {stopnie=}")


# wywołać funkcję pobierania danych od usera
get_degrees()

# obliczyś sin i wyświetlić
radiany = math.radians(stopnie)
sinus = math.sin(radiany)

print(f"Sinus z {stopnie} wynosi {sinus}.")