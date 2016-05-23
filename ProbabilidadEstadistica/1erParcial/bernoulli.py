from math import factorial as fact

"""
Ejemplo:
10 bolas en una urna
3 rojas
7 azules

a) ¿Cuál es la probabilidad de obtener 0 bolas rojas y exactamente 10 bolas rojas?
"""


def bernoulli(x, n, p):
    if n is type(int):
        q = 1 - p
        return (fact(n) / (fact(x) * fact(n - x))) * p ** x * q ** (n - x)

a = bernoulli(0, 10, 0.3)
b = bernoulli(10, 10, 0.3)

print(a * b)


"""
b) La probabilidad de obtener en 10 ensayos menos de 4 bolas rojas
"""

for i in range(int(4)):
    print(bernoulli(10, i, 0.3))

