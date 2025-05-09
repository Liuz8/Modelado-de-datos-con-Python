"""notas_grupos = ['Juan', 8, 'Luis', 7, 'Carlos', 9, 'Angel', 10]

nombres = []
notas = []

for i in range((len(notas_grupos))):
    if i % 2 == 0:
        nombres.append(notas_grupos[i])
    else:
        notas.append(notas_grupos[i])

print(f'Nombres: {nombres}')
print(f'Notas: {notas}')
"""

from random import randint

nombres = ['Juan', 'Luis', 'Carlos', 'Angel']

def genera_numero():
    return randint(0, 999)

codigo_estudiantes = []

for i in range(len(nombres)):
    codigo_estudiantes.append((nombres[i], nombres[i][0]+str(genera_numero())))

print(codigo_estudiantes)
