# Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.
# Entrada
numeros = [1,50,3,35,2,4]
# Proceso
cantidadNumeros= len(numeros)
suma=0
for x in numeros:
    suma+=x
media=suma/cantidadNumeros
# Salida
print(f"La media de la lista es {media}")