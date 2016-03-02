__author__ = 'nger'
from math import factorial as f


def fact(n, r):
    return f(n) / f(r) * (f(n - r))


def prob(c1, c2):
    return fact(c1)


if __name__ == '__main__':
    print("""
Cinco microprocesadores se seleccionan al azar de un lote de 1000 entre los cuales 20 son defectuosos.
- Encuentre la probabilidad de no obtener microprocesadores defectuosos.
""", end='\n')
    a = float(input("Ingresa los valores del total de productos: "))
    b = float(input("Ingresa los valores de los defectuosos: "))
    c = 5
    print(fact(a, c))
    print(fact(a, b - c))
