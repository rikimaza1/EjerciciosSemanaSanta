# Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista
# Entrada
numeros = [1, 2, 3, 4, 5, 6, 7, 7, 7, 3, 2]
# Proceso
# Convertiremos la lista numeros a un set ya que este tiene una propiedad que no permite repetidos
numerosSet = set(numeros)
# Salida
print(numerosSet)
