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


# 6 - Estás trabajando con procesamiento de lenguaje natural (NLP) y, en esta ocasión, tu líder te pidió que 
# crees un fragmento de código que reciba una lista con las palabras separadas de una frase generada por 
# ChatGPT.

# Necesitas crear una función que evalúe cada palabra de este texto y verifique si el tratamiento para quitar 
# los símbolos de puntuación (',', '.', '!' y '?') se realizó. De lo contrario, se lanzará una excepción del 
# tipo ValueError señalando el primer caso en que se detectó el uso de una puntuación a través de la frase 
# "El texto presenta puntuaciones en la palabra "[palabra]"". Esta solicitud se centra en el análisis del 
# patrón de frases generadas por la inteligencia artificial.

# Datos para probar el código:

# Lista tratada:

# lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
#                   'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
#                   'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']

# Lista no tratada:

# lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
#                   'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
#                   'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

def verificar_puntuaciones(lista_palabras):
    simbolos = [',', '.', '!', '?']

    for palabra in lista_palabras:
        if any(simbolo in palabra for simbolo in simbolos):
            raise ValueError(f'El texto presenta puntuaciones en la palabra "{palabra}"')
    print('Texto verificado: no se encontraron puntuaciones.')

lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']

lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

verificar_puntuaciones(lista_no_tratada)