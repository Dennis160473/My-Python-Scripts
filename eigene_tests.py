from datetime import datetime, date


# Definieren von Funktionen
def kugel_volumen(radius, kommastellen):
    pi = 3.14159
    volumen = (4 / 3) * pi + radius**3
    volumen = round(volumen, kommastellen)
    return pi, radius, volumen


pi, r, vol = kugel_volumen(5, 3)
print(
    "Eine Kugel mit dem Radius "
    + str(r)
    + " hat das Volumen "
    + str(vol)
    + "\nin der Formel benutzt man pi = "
    + str(pi)
)


print(2 > 1)








# Boolsche Variablen
## Vergleichsoperatoren
hund = y > 0
hund = y == 0
hund = y != 0
hund = y < 0
hund = y >= 0
hund = y <= 0
hund = y < x
hund = 1 < 0
## Boolsche Operatoren
and, or, not
### and
hund = y >= 0 and Y != 0               = False
### or
hund = y >= 0 or y != 0                = True
### not
hund = not Y == 0 <-> y != 0         = False
## Identitätsoperatoren
is, in
### is
print(5 is 6) -> False                 print(5 is not 6) -> True
print(5 == 6) -> False                 print(5 != 6) -> True
### in
print(0 in feature) -> True