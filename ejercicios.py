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

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos3(n):
    return list(filter(lambda x: x % 3 == 0, n))

print(multiplos3(lista))
