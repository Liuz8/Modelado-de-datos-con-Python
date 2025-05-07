dictionary = {'1° Trimestre':9.5,'2° Trimestre':8,'3° Trimestre':7}

sumaDictionary = sum(dictionary.values())

promedio = round((sumaDictionary/len(dictionary)), 1)

print(promedio)