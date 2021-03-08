
import sys
from math import *
#zadanie 1

sport = ["FGC", "koszykówka", "siatkówka"]
sport.reverse()
sport.append('piłka nożna')
sport.append('Większość e-Sportów')
print(sport)

# zadanie 2

słowniczek = {"tłum.": "tłumaczenie", "abp": "Arcybiskup", "ds.": "Do spraw"}
print(słowniczek["ds."])

# zadanie 3

gierki = {"Dziki Gon": "Wiedźmin 3", "HEAVEN OR HELL":"Guilty Gear", "Super Dash":"Dragon Ball Fighterz", "Storm Approaching":"Devil May Cry",
          "The Cycle":"Pillars Of Eternity II: Deadfire", "Dovakin":"The Elder Scrolls V: Skyrim"}
print(gierki["HEAVEN OR HELL"])
print(len(gierki))


# zadanie 4

zdanie = input("Napisz jakieś zdanie:\n")
a = zdanie.count("a")
A = zdanie.count("A")
print(a+A)

# zadanie 5

sys.stdout.write('Podaj trzy liczby całkowite: ')
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
wynik = a ** b + c
print(wynik)

# zadanie 6

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
if a >= b:
    if a >= c:
        print('Największa liczba to: %d' % a)
if b >= a:
    if b >= c:
        print('Największa liczba to: %d' % b)
if c >= a:
    if c >= b:
        print('Największa liczba to: %d' % c)
