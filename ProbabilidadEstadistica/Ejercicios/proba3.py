__author__ = 'nger'
from math import factorial as f


def fact(x):
    return print(1 - (f(365) / 365 ** x))

if __name__ == '__main__':
    print("""
Encuentre la probabilidad de entre n personas, al menos dos hayan nacido el mismo mes y día (pero no necesariamente en
el mismo año). Suponga que todos los meses y días son igualmente probables e ignore los cumpleaños del 29 de febrero.
    """)
    a = float(input("¿Cuántas son en total? "))
    fact(a)
