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

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tupla = [(i, nombre) for i, nombre in enumerate(lista)]

print(lista_tupla)

