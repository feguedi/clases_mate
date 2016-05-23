from math import factorial as fact

problema = """\
En un estudio se encontró que el 90% de las casas de una colonia de una cierta ciudad tienen piso de cemento.
En una muestra tomada aleatoriamente de 10 casas ¿cuál es la probabilidad de que:
a)a lo más 4 casas tengan piso de cemento?
b)al menos 5 casas tengan piso de cemento?
c)más de dos casas, pero menos de siete tengan piso de cemento?
d)nueve casas tengan piso de cemento?"""

def bernoulli(x, n, p):
    q = 1 - p
    return (fact(n) / (fact(x) * fact(n - x))) * p ** x * q ** (n - x)
        
# a = bernoulli(9, 10, 0.9)

print("  x  | ", end='')
print("P(x)")

for j in range(26):
    print("_", end='')
    
print("_")

for i in range(10):
    i = int(i)
    if i == 10:
        print(i, "|", end='')
    else:
        print(" ", i, " |", end='')
    print(bernoulli(i, 10, 0.9))
