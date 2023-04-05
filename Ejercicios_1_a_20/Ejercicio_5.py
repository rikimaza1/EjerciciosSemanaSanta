# Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.
numeros = [1,50,20,30,2,4]
mayor = numeros[0]
menor = numeros[0]
for x in numeros:
    if mayor < x:
        mayor = x
    if menor > x:
        menor = x
print(f"El mayor y menor de la lista son [{mayor} , {menor}]")