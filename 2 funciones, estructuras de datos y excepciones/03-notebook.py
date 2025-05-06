#1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.
# pip install matplotlib = 3.7.1

# 2 - Escribe un código para importar la biblioteca numpy con el alias np.
import numpy as np

#3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.
#lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
from random import choice, uniform, randint, randrange
from math import sqrt, pow, pi

"""lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

num = choice(lista)

print(num)"""

#4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

"""num = randint(1, 99)
print(num)"""

#5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

"""num1 = int(input('Ingresa un numero: '))
num2 = int(input('Ingresa un numero: '))

print(f'El calculo de {num1} a la potencia de {num2} es: {pow(num1, num2)}')"""

#6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. 
# La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. 
# Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

"""num = int(input('Ingresa la cantidad de participantes: '))
ganador = randint(1, num)

print(f'El ganador es: {ganador}')"""

#7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. 
# El token debe ser par y variar de 1000 a 9998. 
# Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

"""nombre_usuario = input('Ingresa tu nombre: ')
def generar_token():
    token = randrange(1000, 9998, 2)
    return token

token_generado = generar_token()

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")"""

#8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". 
# En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. 
# Crea el código que realice esta selección aleatoria según la lista dada.

"""frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

for i in range(1, 4):
    print(f'{i} {choice(frutas)}')"""

#9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

"""numeros = [2, 8, 15, 23, 91, 112, 256]
numerosRaiz = []

print(numeros)

for valor in numeros:
    num = round(sqrt(valor), 2)
    numerosRaiz.append(num)

print(numerosRaiz)

for valor in numeros:
    num = sqrt(valor)
    if num.is_integer():
        print(f'El numero {num} es entero')"""

#10 - Haz un programa para una tienda que vende césped para jardines. 
# Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. 
# Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

cesped = float(input("Ingrese el radio de su cesped: "))

area = pi * pow(cesped, 2)

costo = round((area * 25), 2)

print(f'El costo por el cesped es de: R$ {costo}')