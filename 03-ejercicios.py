# 1 - Haz un programa que solicite a la persona usuaria ingresar dos números decimales y 
# calcular la división entre estos números. El código debe incluir un manejo de error, indicando 
# el tipo de error que se generó si la división no es posible.
# Prueba el programa con el segundo valor numérico de la entrada igual a 0. También prueba usando 
# caracteres textuales en la entrada para verificar los tipos de errores que ocurren.

"""try:
    n1 = float(input('Ingresa un valor: '))
    n2 = float(input('Ingresa un valor: '))
    resultado = n1 / n2
    print(f'Resultado: {resultado}')
except ZeroDivisionError as e:
    print(type(e), f'El denominador no puede ser 0: {e}')
except ValueError as e:
    print(type(e), f'El valor debe de ser numerico: {e}')

print('¡Hola Mundo!')"""

# 2 - Haz un programa que solicite a la persona usuaria ingresar un texto que será una clave a buscar en el 
# siguiente diccionario: edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, almacenando el 
# resultado del valor en una variable. El código debe incluir un manejo de error KeyError, imprimiendo la 
# información 'Nombre no encontrado' en caso de error, e imprimir el valor si no ocurre ninguno.
# Prueba el programa con un nombre presente en una de las claves del diccionario y con uno que no esté en el 
# diccionario para verificar el mensaje de error.

"""edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nombre = input('Ingresa un nombre: ')
    edad = edades[nombre]
    print(f'{nombre}: {edad}')
except KeyError as e:
    print(type(e), f'Nombre no encontrado {e}')"""

# 3 - Crea una función que reciba una lista como parámetro y convierta todos los valores de la lista a 
# flotantes. La función debe incluir un manejo de error indicando el tipo de error generado y devolver la 
# lista si no ha ocurrido ningún error. Por último, debe tener la cláusula finally para imprimir el texto: 
# 'Fin de la ejecución de la función'.

"""def enteroAflotante(lista: list):
    try:
        lista_float = list(map(float,lista))
        print(f'valores de lista convertidos a float\n{lista_float}')
        return lista_float
    except Exception as e:
        print('Ocurrio un error: ', e)
        print('Tipo de error: ', type(e))
        print('Nombre del error: ', e.__class__.__name__)
    finally:
        print('Fin de la ejecución de la función')

lista = [1,2, 'a']
enteroAflotante(lista)"""

