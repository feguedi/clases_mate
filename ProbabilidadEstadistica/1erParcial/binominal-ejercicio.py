from math import factorial as fact

problema = """\
Todos los días se seleccionan de manera aleatoria 15 unidades de un proceso de manufactura con el
propósito de verificar el porcentaje de unidades defectuosas en la producción. Con base en
información pasada, la probabilidad de tener una unidad defectuoso es de 0.05. La gerencia ha decidido
detener la producción cada vez que una muestra de 15 tenga dos más defectuosas.

¿cuál es la probabilidad de que en cualquier día, la producción se detenga?
"""

def bernoulli(x, n, p):
    q = 1 - p
    return (fact(n) / (fact(x) * fact(n - x))) * p ** x * q ** (n - x)
    
print("  x   | ", end='')
print("P(x)")

for j in range(26):
    print("_", end='')
    
print("_")
    
for i in range(16):
    i = int(i)
    if i >= 10:
        print(" ", i, " | ", end='')
    else:
        print(" ", i, "  | ", end='')
    print(bernoulli(i, 15, 0.05))

print("Probabilidad de que se detenga la producción en cualquier día")
print("")