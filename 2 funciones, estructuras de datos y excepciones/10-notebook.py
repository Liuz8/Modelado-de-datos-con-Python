notas = {'Juan': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Claudia': [5.5, 6.6, 8.0],
         'Ana': [6.0, 10.0, 9.5], 'Jorge': [5.5, 7.5, 9.0], 'Julia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}


"""try:
    nombre = input('Digite el nombre del estudiante: ')
    resultado = notas[nombre]
    print(resultado)
except Exception as e:
    print(type(e), e)"""

#####################################################################################

"""try:
    nombre = input('Digite el nombre del estudiante: ')
    resultado = notas[nombre]
except KeyError:
    print('Estudiante no matriculado en el grupo')
else:
    print(f'Las notas del estudiante son: {resultado}')"""

#####################################################################################

try:
    nombre = input('Digite el nombre del estudiante: ')
    resultado = notas[nombre]
except KeyError:
    print('Estudiante no matriculado en el grupo')
else:
    print(f'Las notas del estudiante son: {resultado}')
finally:
    print('La consulta ha terminado.')