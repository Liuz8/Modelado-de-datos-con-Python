#1 - Escribe un código que lee la lista siguiente y realiza:

# 1. Leer el tamaño de la lista
# 2. Leer el valor máximo y mínimo
# 3. Calcular la suma de los valores de la lista
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.

"""lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

print(f'Tamaño: {len(lista)}')
print(f'maximo y minimo: {max(lista)} {min(lista)}')
print(f'suma {sum(lista)}')
print(f'La lista tiene {len(lista)} números, donde el mayor es {max(lista)} y el menor es {min(lista)}. '
      f'La suma de los valores es {sum(lista)}')

print(lista)"""

#2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. 
# Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:

# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70

"""num = int(input('Ingrese una tabla de multiplicar del 1 al 10: '))

def tabla(a: int) -> int:
    print(f'Tabla del {a}')
    for i in range(0,11):
        print(f'{a} X {i} = {a*i}')

tabla(num)"""


#3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:

"""lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos3(n):
    return list(filter(lambda x: x % 3 == 0, n))

print(multiplos3(lista))"""


#4 - Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.

"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nueva_lista = list(map(lambda x: pow(x, 2), lista))

print(lista)
print(nueva_lista)"""

#5 - Has sido contratado como científico(a) de datos de una asociación de skate. 
# Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un código que calcule la puntuación de los atletas. 
# Para ello, tu código debe recibir 5 notas ingresadas por los jueces.
"""contador = 0.0
for i in range(0, 5):
    puntuacion = float(input('Ingresa una puntuacion: '))
    contador += puntuacion

promedio = contador/5

print(f'El promedio es de: {promedio}')"""

#6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, 
# necesitas crear una función que reciba una lista de 4 notas y devuelva:

# mayor nota
# menor nota
# media
# situación (Aprobado(a) o Reprobado(a))
# Uso de la función
# Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)

"""notas = [10, 9.5, 8.7, 9]

def modificar_lista(lista: list):
    '''
    La funcion analiza los datos de una lista
    analiza la nota maxima, minima, la media y si aprobo o reprobo
    '''
    maximo = max(lista)
    minimo = min(lista)
    media = sum(lista)/len(lista)
    if media >= 7:
        situacion = 'Aprobado'
    else:
        situacion = 'Reprobado'
    
    return maximo, minimo, media, situacion

help(modificar_lista)

maximo, minimo, media, situacion = modificar_lista(notas)

print(f'El estudiante obtuvo una media de {media}, con la mayor nota de {maximo} puntos y la menor nota de {minimo} puntos y fue {situacion}.')"""

#7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos
#  para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# Puedes apoyarte en la función map()

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

lista = list(map(lambda nombre, apellido: f"{nombre.capitalize()} {apellido.capitalize()}", nombres, apellidos))

print(lista)