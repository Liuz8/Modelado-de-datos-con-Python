estudiantes = [9.0, 7.3, 5.8, 6.7, 8.5]

nombres = [('Juan', 'J569'), ('Luis', 'L207'), ('Carlos', 'C215'), ('Angel', 'A646')]

notas = [8.0, 9.0, 10.0, 9.0, 7.0, 6.0, 3.4, 7.0, 7.0, 5.5, 6.6, 8.0, 6.0, 10.0, 9.5]

situacion = ['Aprobado(a)' if i >= 7 else 'Reprobado(a)' for i in estudiantes]
print(situacion)

registros = [nombres, notas, estudiantes, situacion]

print(registros)