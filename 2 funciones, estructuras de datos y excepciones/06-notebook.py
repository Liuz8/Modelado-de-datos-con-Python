"""notas = [8.0, 9.0, 10.0, 9.0, 7.0, 6.0, 3.4, 7.0, 7.0, 5.5, 6.6, 8.0, 6.0, 10.0, 9.5]

notas_separadas = []

for i in range(0, len(notas),3):
  notas_separadas.append([notas[i],notas[i+1], notas[i+2]])

print(notas_separadas)

def promedio(lista: list=[0]) -> float:
  '''Funcion para calcular el promedio de notas en una lista
  
    lista: list, default [0]
        Lista con las notas para calcular el promedio
    return = calculo: float
        Promedio calculado
    '''
  
  calculo = sum(lista) / len(lista)

  return calculo

promedios = [round(promedio(nota), 1) for nota in notas_separadas]

print(promedios)"""

estudiantes = [9.0, 7.3, 5.8, 6.7, 8.5]

nombres = [('Juan', 'J569'), ('Luis', 'L207'), ('Carlos', 'C215'), ('Angel', 'A646')]

nombres = [nombre[0] for nombre in nombres]
print(nombres)

combinado = list(zip(nombres, estudiantes))

print(combinado)

candidatos = [c[0] for c in combinado if c[1] >= 8]

print(candidatos)