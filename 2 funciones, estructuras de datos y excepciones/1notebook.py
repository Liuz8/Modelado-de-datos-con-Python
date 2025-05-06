from matplotlib import pyplot as plt

alumnos = ["juan", 'maria', 'jose']
notas = [9, 8.5, 6.5]

plt.bar(x=alumnos, height=notas)
plt.show()