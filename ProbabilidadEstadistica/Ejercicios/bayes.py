"""¿Cuál es la probabilidad de que, al elegir un diputado que no es sindicalista, sea del PRD o del verde?"""

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


def oper(a, b):
    return a / b

if __name__ == '__main__':
    y = 1.0
    for n in sind.items():
        y -= n

    # Probabilidad de que sea del Verde
    print('x')
