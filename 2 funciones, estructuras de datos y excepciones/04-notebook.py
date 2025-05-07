"""dictionary = {'1° Trimestre':9.5,'2° Trimestre':8,'3° Trimestre':7}

sumaDictionary = sum(dictionary.values())

promedio = round((sumaDictionary/len(dictionary)), 1)

print(promedio)"""

def sumar(a: int, b: int) -> int:
    '''Función que suma dos números.

    a: int
        Primer número a sumar.
    b: int
        Segundo número a sumar.
    return: int
        La suma de a y b.
    '''
    return a + b

sum = sumar(1, 7)

print(sum)

help(sumar)