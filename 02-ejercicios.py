#1 - Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista:

"""lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

lista_suma = [sum(i) for i in lista_de_listas]

print(sum(lista_de_listas[0]))

print(lista_suma)"""

# 2 - Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:

"""lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

tercer_tupla = [i[2] for i in lista_de_tuplas]

print(tercer_tupla)"""

# 3 - A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], 
# crea un código para generar una lista de tuplas en la que cada tupla tenga el primer elemento como la posición del 
# nombre en la lista original y el segundo elemento siendo el propio nombre.

"""lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tupla = [(i, nombre) for i, nombre in enumerate(lista)]

print(lista_tupla)"""

# 4 - Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el valor numérico de 
# cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:

"""alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

alquilerApartamento = [i[1] for i in alquiler if i[0] == 'Apartamento']

print(alquilerApartamento)"""

# 5 - Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las claves estén en la lista 
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
# y los valores estén en 
# gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

"""meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

diccionario = {mes:g for mes, g in zip(meses, gasto)}

print(diccionario)"""

# 6 - Una tienda tiene una base de datos con la información de venta de cada representante y de cada año y necesita 
# filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó una muestra con solo las columnas de los 
# años y los valores de venta para que puedas ayudar a realizar la filtración de los datos a través de un código:
# Crea una lista usando la comprensión de listas para filtrar los valores de 2022 que sean mayores a 6000.

"""ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), 
          ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), 
          ('2021', 9680), ('2022', 5616)]

ventas2 = [i for i in ventas if (i[0] == '2022') and (i[1] >= 6000)]

print(ventas2)

print(ventas[0])"""

# 7 - Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y le gustaría 
# etiquetar los datos de la siguiente manera:

# Glucosa igual o inferior a 70: 'Hipoglicemia'
# Glucosa entre 70 y 99: 'Normal'
# Glucosa entre 100 y 125: 'Alterada'
# Glucosa superior a 125: 'Diabetes'
# La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la comprensión de listas que 
# contenga la etiqueta y el valor de la glucemia en cada tupla.

"""glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

etiqueta = [('Hipoglicemia' if i <= 70 else 'Normal' if i > 70 and i <= 99 else 'Alterada' if i >= 100 and i <= 125 else 'Diabetes', i) for i in glicemia]

print(etiqueta)"""

# 8 - Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto divididos en las siguientes listas:
# La plataforma necesita estructurar estos datos en una tabla que contenga el valor total de la venta, que se obtiene 
# multiplicando la cantidad por el precio unitario. Además, la tabla debe contener un encabezado indicando las columnas: 
# 'id', 'cantidad', 'precio' y 'total'.
# Crea una lista de tuplas en la que cada tupla tenga id, cantidad, precio y valor total, siendo la primera tupla el encabezado de la tabla.

"""id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

ventas = [('id', 'cantidad', 'precio', 'total')] + [
    (i, c, p, p*c) for i,c,p in zip(id, cantidad, precio)
]

for fila in ventas:
    print(f'{fila[0]:<10} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<10}')"""

# 9 - Una empresa tiene sucursales distribuidas en los estados de la región Sudeste de Brasil. 
# En una de las tablas de registro de las sucursales, hay una columna que contiene la información de a qué estado pertenece: 
# estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE'].

# La empresa siempre está abriendo nuevas sucursales, por lo que la tabla está constantemente recibiendo nuevos registros y al 
# gerente le gustaría tener la información actualizada de la cantidad de sucursales en cada estado.

# A partir de la columna con la información de los estados, crea un diccionario utilizando la comprensión de diccionarios 
# (dict comprehension) con la clave siendo el nombre de un estado y el valor siendo la cantidad de veces que aparece el estado en la lista.

# Consejo: Puedes hacer un paso intermedio para generar una lista de listas en la que cada una de las listas tenga el nombre de solo un 
# estado con valores repetidos.

"""estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE','OAX', 'OAX', 'OAX', 'CMX', 'CMX',
          'PUE', 'OAX', 'CMX', 'VER', 'PUE','VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX','PUE']

estados_contados = {estado:estados.count(estado) for estado in list(set(estados))}

print(estados_contados)"""

# 10 - En esa misma tabla de registro de sucursales, hay una columna con la información de la cantidad de personas 
# empleadas y el gerente quisiera tener un agrupamiento de la suma de esas personas para cada estado. Las informaciones contenidas 
# en la tabla son:

# A partir de la lista de tuplas, crea un diccionario en el que las claves son los nombres
#  de los estados únicos y los valores son las listas con el número de empleados referentes al estado. 
# También crea un diccionario en el que las claves son los nombres de los estados y los valores son la suma de empleados por estado.

empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), 
             ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  
             ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]

diccionario = {}

for estado, cantidad in empleados:
    if estado in diccionario:
        diccionario[estado].append(cantidad)
    else:
        diccionario[estado] = [cantidad]

suma_empleados = {estado: sum(cantidades) for estado, cantidades in diccionario.items()}

for estado, cantidades in diccionario.items():
    # Unimos la lista de cantidades en una cadena separada por comas
    lista_empleados = ", ".join(str(c) for c in cantidades)
    print(f"{estado:6} | {lista_empleados}")

print('\n')
print("Estado | Total de empleados")
print("----------------------------")
for estado, total in suma_empleados.items():
    print(f"{estado:6} | {total}")