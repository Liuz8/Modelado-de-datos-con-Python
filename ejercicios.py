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

"""nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

lista = list(map(lambda nombre, apellido: f"{nombre.capitalize()} {apellido.capitalize()}", nombres, apellidos))

print(lista)"""

#8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los 
# jugadores y del equipo en su conjunto. 
# Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

#Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por 
# el equipo en cada partido del campeonato. 
# La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos,
#  el empate 1 punto y la derrota 0 puntos.

#Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual,
#  el equipo empató, y si es menor, el equipo perdió. 
# Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

#Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

#goles_marcados = [2, 1, 3, 1, 0]
#goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"

"""goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

def calcula_puntos(lista1: list, lista2: list):
    puntos = 0
    for gol_marcado, gol_recibido in zip(lista1, lista2):
        if gol_marcado > gol_recibido:
            puntos += 3
        elif gol_marcado == gol_recibido:
            puntos += 1
    promedio = (puntos/15)*100
    return puntos, promedio

puntos, promedio = calcula_puntos(goles_marcados, goles_recibidos)

print(f'La puntuacion del equipo fue {puntos} y su rendimiento fue {round(promedio, 2)}%')"""

#9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, 
# siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

#El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, 
# siendo que el precio de la gasolina es de 5 reales por litro. 
# Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

#Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: 
# la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y 
# alimentación (gasto_paseo).

#Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# Recife costaría [gastos] reales.

dias = int(input('Ingresa los dias que quieres irte de vacaciones: '))
destino = int(input('Ingresa 1: para Salvador, 2: Fortaleza, 3: Natal y 4: Aracaju. '))

def gasto_hotel(dias):
    precio_hotel = dias * 150
    return precio_hotel

def gasto_gasolina(destino):
    if destino == 1:
        precio_gasolina = (850*2/14)*5
    elif destino == 2:
        precio_gasolina = (800*2/14)*5
    elif destino == 3:
        precio_gasolina = (300*2/14)*5
    elif destino == 4:
        precio_gasolina = (550*2/14)*5
    return precio_gasolina

def gasto_paseo(dias, destino):
    if destino == 1:
        precio_paseo = 200*dias
    elif destino == 2:
        precio_paseo = 400*dias
    elif destino == 3:
        precio_paseo = 250*dias
    elif destino == 4:
        precio_paseo = 300*dias
    return precio_paseo

precio_hotel, precio_gasolina, precio_paseo = gasto_hotel(dias), gasto_gasolina(destino), gasto_paseo(dias, destino)

gastos = precio_hotel + precio_gasolina + precio_paseo

if destino == 1:
    destino = 'Salvador'
elif destino == 2:
    destino = 'Fortaleza'
elif destino == 3:
    destino = 'Natal'
elif destino == 4:
    destino = 'Aracaju'

print(f'Con base en los gastos definidos, un viaje de {dias} días a {destino} desde Recife costaría {round(gastos, 2)} reales.')
