# *-* coding: UTF-8 *-*
__author__ = 'nger'

"""PROBLEMA
En un determinado grupo de personas, hay rubias, de cabello negro y pelirrojas. El 60% de la gente es de cabello
negro, el 30% rubias y el 10% pelirrojas. El 50% de las rubias tiene ojos claros, el 40% de las pelirrojas tiene ojos
claros y el 25% de cabello negro tiene ojos claros. Si una persona que es elegida al azar tiene ojos claros, cuál es la
probabilidad de que sea rubia."""

# Definimos al grupo de personas
PR = 0.30
PP = 0.10
PN = 0.60

# Definimos al grupo de ojos claros
PRC = 0.50
PPC = 0.40
PNC = 0.10

# Fórmula a elaborar
Ai_por_AiB = PR * PRC
suma1 = PR * PNC
suma2 = PR * PPC
suma3 = PR * PRC

print(Ai_por_AiB, "/", suma1 + suma2 + suma3)

print(Ai_por_AiB / (suma1 + suma2 + suma3))
