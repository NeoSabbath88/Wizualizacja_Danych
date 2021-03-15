import random
# zad 2
lista1 = [ random.randint(1 , 27) for x in range(10) ]
lista2 = [ x for x in lista1 if x % 2 == 0 ]
print(lista1)
print(lista2)


 #zad 4

def prostokatny(a , b , c):


    if a > b and a > c:
        if a ** 2 == b ** 2 + c ** 2:
            return print('Trójkąt jest prostokątny')
        else:
            return print('Trójkąt nie jest prostokątny')

    elif b > a and b > c:
        if b ** 2 == a ** 2 + c ** 2:
            return print('Trójkąt jest prostokątny')
        else:
            return print('Trójkąt nie jest prostokątny')

    elif c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            return print('Trójkąt jest prostokątny')
        else:
            return print('Trójkąt nie jest prostokątny')

print('Czy podany trójkąt jest prostokątny?')
pa=input('podaj bok a ')
pb=input('podaj bok b ')
pc=input('podaj bok c ')
a=int(pa)
b=int(pb)
c=int(pc)
czyprostokatny = prostokatny(a , b , c)
print(czyprostokatny)
# zad 5


def poletrapezu(a , b , h):
    wynik=((a + b) * h / 2)
    return wynik

trapez=poletrapezu(4,5,6)
print(trapez)

