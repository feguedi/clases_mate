from math import fsum as sm

"""contraseña campus virtual: 3st&pr0b4"""

"""¿Cuál es la probabilidad de que, el elegir un diputado que no es sindicalista, seal del PRD o del verde?"""

porc = {
    'PRI': 0.63,
    'PAN': 0.2,
    'PRD': 0.06,
    'VERDE': 0.11
}

sind = {
    'PRI': 0.1,
    'PAN': 0.15,
    'PRD': 0.09,
    'VERDE': 0.03
}


def form(a, b):
    return (sind[a] + porc[b]) / (porc[a] * porc[b])

if __name__ == '__main__':
    """for i in sind.items():
        for j in porc.items():
            print(form(i, j))"""
    for i in porc.items():
        print(sm(sind[i]))
