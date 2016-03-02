__author__ = 'nger'
import math
# import pyfpdf
"""
1°: obtendremos el valor del producto punto
2°: obtendremos el valor de la norma de la primera ecuación
3°: obtendremos el valor de la norma de la segunda ecuación
4°: dividimos el producto punto entre el resultado de multiplicar la norma de
    ambas ecuaciones.
5°: sacamos el anticoseno del resultado de la operación anterior
"""


def imprimir(a, b, c, d):
    if a > 0:
        if a is 1:
            print("x ", end='')
        else:
            print("{0}x ".format(a), end='')
    if a < -1:
        print("{0}x ".format(a), end='')
    if a is -1:
        print("-x ", end='')
    if b > 0:
        if a is not 0:
            if b is 1:
                print("+ y ", end='')
            else:
                print("+ {0}y ".format(b), end='')
        else:
            if b is 1:
                print("y ", end='')
            else:
                print("{0}y ".format(b), end='')
    elif b < 0:
        if b is -1:
            print("- y ", end='')
        else:
            print("- {0}y ".format(int(math.fabs(b))), end='')
    if c > 0:
        if b is not 0 or a is not 0:
            if c is 1:
                print("+ z = {0}".format(-d))
            else:
                print("+ {0}z = {1}".format(c, -d))
        elif b is 0 and a is 0:
            if c is 1:
                print("z = {0}".format(-d))
            else:
                print("{0}z = {1}".format(c, -d))
    elif c < 0:
        if c is -1:
            print("- z = {0}".format(-d))
        else:
            print("- {0}z = {1}".format(int(math.fabs(c)), -d))
    elif c is 0:
        print("= {0}".format(-d))
    if a is 0 and b is 0 and c is 0:
        print("¡¡¡TU ECUACIÓN NO TIENE SENTIDO!!!")


def obt_prodpunt(a, b, c, d, e, f):
    # prod = (a * d) + (b * e) + (c * f)
    return (a * d) + (b * e) + (c * f)


def obt_norma(a, b, c):
    # norma = math.sqrt((a ** 2) + (b ** 2) + (c ** 2))
    return math.sqrt((a ** 2) + (b ** 2) + (c ** 2))


def comprobacion(a, b, c, d):
    com = False
    if a + b + c is d:
        com = True
    return com


if __name__ == '__main__':
    x1, x2, y1, y2, z1, z2, w1, w2 = 0, 0, 0, 0, 0, 0, 0, 0
    w = []
    x = []
    y = []
    z = []
    contador = {'primer', 'segundo'}
    for i in contador:
        w.append(int(input("Ingresa el {0} valor independiente: ".format(i))))
        x.append(int(input("Ingresa el {0} valor de x: ".format(i))))
        y.append(int(input("Ingresa el {0} valor de y: ".format(i))))
        z.append(int(input("Ingresa el {0} valor de z: ".format(i))))
    for j in range(2):
        if j is 0:
            w1 = int(w.pop())
            x1 = int(x.pop())
            y1 = int(y.pop())
            z1 = int(z.pop())
        elif j is 1:
            w2 = int(w.pop())
            x2 = int(x.pop())
            y2 = int(y.pop())
            z2 = int(z.pop())
    print("\nLas ecuaciones son...\n")
    imprimir(x1, y1, z1, w1)
    imprimir(x2, y2, z2, w2)
    prod = obt_prodpunt(x1, y1, z1, x2, y2, z2)
    norm1 = obt_norma(x1, y1, z1)
    norm2 = obt_norma(x2, y2, z2)
    res = math.degrees(math.acos(prod / (norm1 * norm2)))
    print("\n\nEl ángulo que generan ambos planos es:", res)
