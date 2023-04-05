#  Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.
# Entrada
numeros = [1,50,3,35,2,4]
# Proceso
suma = 0
for x in numeros:
    if x % 2 == 0:
        suma+=x
# Salida
print(suma)