__author__ = 'nger'
"""
Programa para sacar el área de un triángulo rectángulo
"""


def calc(x, y):
    print(float((x * y) / 2))


if __name__ == '__main__':
    h = float(input("Dame la base: "))
    b = float(input("Dame la altura: "))
    print(end='\n')
    calc(h, b)
