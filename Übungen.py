# Aufgabe 3: Programmierübungen vom Vormittag


# Aufgabe 1
def calc_area(width, height):
    return width * height


width = float(input("Please enter a number? "))
height = float(input("Please enter a number? "))

if calc_area(width, height):
    print(f"Das Ergebnis der Fläche ist {width * height}.")
else:
    print()


# Aufgabe 2
print("Meilen <-> Kilometer")
faktor = 1.60934

print("(1) Meilen -> Kilometer")
print("(2) Kilometer -> Meilen")
print("(3) Beenden")
auswahl = int(input("Deine Wahl: "))

if auswahl == 1:
    s = float(input("Strecke in Meilen: "))
    s = s / faktor
    print(f"Das sind {s}= Kilometer")
elif auswahl == 2:
    s = float(input("Strecke in Kilometern: "))
    s = s * faktor
    print(f"Das sind {s}= Meilen")
else:
    print("Diese Eingabe war nicht vorgesehen")

print("Ende des Programms")


# Hit import statements
from datetime import datetime
import random

now = datetime.now()
print(now)
print(random.randint)


# Vorgefertigte Pakete in Python
import datetime

date_str = "2024-12-24"
date = datetime.datetime(2024, 12, 24)
date.year


# Algorithmus anwenden
def kaffee_kochen():
    print("Wasser erhitzen")
    print("Kaffeepulver in die Maschine geben")
    print("Wasser einfüllen")
    print("Maschine einschalten")
    print("Kaffee genießen")


kaffee_kochen()


zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
