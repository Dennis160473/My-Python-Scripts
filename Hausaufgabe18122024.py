# Aufgabe 2

# 2.1 - Aktuelles Datum und Uhrzeit ausgeben im Format TT.MM.JJJJ HH:MM:SS
import datetime


def aktuelles_datum_und_uhrzeit():
    Ausgabe = datetime.today().strftime("%d.%m.%Y, %X")
    print(Ausgabe)


aktuelles_datum_und_uhrzeit()


# 2.2 - Differenz bis zum Jahresende berechnen
from datetime import timedelta


def tage_bis_jahresende(time_interval=day_2 - day_1):
    print(time_difference)


day_1 = datetime.timedelta.today("%d.%m.%Y")
day_2 = datetime.timedelta("31.12.2024")

tage_bis_jahresende()


# 2.3 - Benutzerdefiniertes Datum
def tage_bis_datum():
    result = datetime.datetime().strftime("%d.%m.%Y, %X")
    print(result)


user = input("Please enter the date: ")

tage_bis_datum()


# 2.4 - Wochentag berechnen
def wochentag_berechnen():
    weekday = datetime.datetime("%A")
    print(weekday)


wochentag_berechnen()
