lista_completa = [[('Juan', 'J569'), ('Luis', 'L207'), ('Carlos', 'C215'), ('Angel', 'A646')],
                  [[8.0, 9.0, 10.0,], [9.0, 7.0, 6.0,], [3.4, 7.0, 7.0,], [5.5, 6.6, 8.0,], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprobado(a)', 'Aprobado(a)', 'Reprobado(a)', 'Reprobado(a)', 'Aprobado(a)']]

columnas = ['Notas', 'Promedio final', 'Situacion']

registro = {columnas[i]:lista_completa[i+1] for i in range(len(columnas))}
registro['Estudiante'] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]

print(registro)