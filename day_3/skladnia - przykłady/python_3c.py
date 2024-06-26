import math  # import całego modułu
# from math import sin, radians  # import tylko 1 funkcji z modułu


# spytać usera o ilość stopni - funkcja zapisana przez nas
def get_degrees():
    while True:
        try:
            stopnie = float(input("Pdaj nam stopnie do sinusa: "))
            # jeśli user wprowadził poprawną liczbę to koniec
            if 0 <= stopnie <= 360:
                # teraz funkcja zwróci wartość i zakończy działanie
                return stopnie # nie musi być na końcu bloku kodu
        except:
            print("Źle wprowadzono wartość stopni.")


# wywołać funkcję pobierania danych od usera
# przypiszemy to do zmiennej pobrane_stopnie
pobrane_stopnie = get_degrees()

# obliczyś sin i wyświetlić
radiany = math.radians(pobrane_stopnie)
sinus = math.sin(radiany)

print(f"Sinus z {pobrane_stopnie} wynosi {sinus}.")