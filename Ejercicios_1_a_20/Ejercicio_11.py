# Crea un algoritmo que calcule el factorial de un número entero.
# Entrada
numero = int(input("Introduce un numero entero "))
# Proceso
factorial = 1
for x in range(1, numero+1):
    factorial*=x
# Salida
print(factorial)
