# 5 - Como desafío, se te ha asignado la tarea de desarrollar un código que contabiliza las puntuaciones de 
# estudiantes de una institución educativa de acuerdo con sus respuestas en una prueba. Este código debe ser 
# probado para un ejemplo de 3 estudiantes con una lista de listas en la que cada lista tiene las respuestas 
# de 5 preguntas objetivas de cada estudiante. Cada pregunta vale un punto y las alternativas posibles son A, 
# B, C o D.

# Si alguna alternativa en una de las pruebas no está entre las alternativas posibles, debes lanzar un 
# ValueError con el mensaje "La alternativa [alternativa] no es una opción de alternativa válida". El cálculo 
# de las 3 notas solo se realizará mediante las entradas con las alternativas A, B, C o D en todas las pruebas. Si no se lanza la excepción, se mostrará una lista con las notas en cada prueba.

# Datos para la prueba del código:
# Respuestas de la prueba:
# respuestas = ['D', 'A', 'B', 'C', 'A']
# A continuación, hay 2 listas de listas que puedes usar como prueba:
# Notas sin excepción:
# tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
# Copia el código
# Notas con excepción:
# tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

"""respuestas = ['D', 'A', 'B', 'C', 'A']

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calcular_notas(respuestas_correctas, pruebas):
    notas = []
    alternativas_validas = {'A', 'B', 'C', 'D'}

    for prueba in pruebas:
        nota = 0
        for i, respuesta in enumerate(prueba):
            if respuesta not in alternativas_validas:
                raise ValueError(f'La alternativa {respuesta} no es una opcion de alternativa valida.')
            if respuesta == respuestas_correctas[i]:
                nota += 1
        notas.append(nota)
    return notas

try:
    resultado = calcular_notas(respuestas, tests_con_ex)
    print(f"Notas de los estudiantes: {resultado}")
except ValueError as e:
    print('Error', e)"""


