# Aufgabe 3: Taschenrechner (50 Punkte)
# ● Aufgabenstellung:
# ○ Schreibe zunächst 4 Funktionen: add(x,y), subtract(x,y), mult(x,y) und div(x,y)
# ○ Jede dieser 4 Funktionen soll 2 Argumente annehmen: x und y, und die miteinander addieren, subtrahieren, multiplizieren oder dividieren
# ○ Dann schreibt eine Funktion calculator(), die: ■ Den User fragt, ob er addieren, subtrahieren, multiplizieren oder dividieren will
# ■ Den user nach 2 Zahlen fragt ■ Die entsprechende Funktion aufruft ■ Das Ergebnis auf der Konsole anzeigt
def add(x, y):
    print(x + y)


zahl1 = int(input("Bitte geben Sie eine ganze Zahl an? "))
zahl2 = int(input("Bitte geben Sie eine ganze Zahl an? "))
add(zahl1, zahl2)


def subtract(x, y):
    print(x - y)


zahl1 = int(input("Bitte geben Sie eine ganze Zahl an? "))
zahl2 = int(input("Bitte geben Sie eine ganze Zahl an? "))
subtract(zahl1, zahl2)


def mult(x, y):
    print(x * y)


zahl1 = int(input("Bitte geben Sie eine ganze Zahl an? "))
zahl2 = int(input("Bitte geben Sie eine ganze Zahl an? "))
mult(zahl1, zahl2)


def div(x, y):
    print(x / y)


zahl2 = int(input("Bitte geben Sie eine ganze Zahl an? "))
zahl2 = int(input("Bitte geben Sie eine ganze Zahl an? "))
div(zahl1, zahl2)