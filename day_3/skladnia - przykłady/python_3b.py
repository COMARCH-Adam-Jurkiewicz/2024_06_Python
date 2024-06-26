import math  # import całego modułu
# from math import sin, radians  # import tylko 1 funkcji z modułu


# spytać usera o ilość stopni - funkcja zapisana przez nas
def get_degrees():
    while True:
        try:
            stopnie = float(input("Pdaj nam stopnie do sinusa: "))
        except:
            print("Źle wprowadzono wartość stopni.")
            stopnie = 0



# obliczyś sin i wyświetlić
radiany = math.radians(stopnie)
sinus = math.sin(radiany)

print(f"Sinus z {stopnie} wynosi {sinus}.")