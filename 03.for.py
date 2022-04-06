#Ejemplo de estructura para iterar utilizando secuencias de cosas
#Listas

drinks = ["mojito", "margarita","piña colada"]
for drink in drinks:
    print(drink)

print("#############################")

#El for tambien funciona con letter
for letter in "tio charli":    
    print(letter)

print("########################")

#El for tambien puede ser usado con el break
for drink in drinks:
    if drink == "margarita":
        break
    print(drink)

print("###########################")

#El for tambien puede ser usado con el break
for drink in drinks:
    if drink == "margarita":
        continue
    print(drink)
else:
    print("berta se termino los margaritas")

print("###############################")

#for anidados
sizes = ("normal","large","tio charli xl")
for size in sizes:
    for drink in drinks:
        print(drink,size)
        

