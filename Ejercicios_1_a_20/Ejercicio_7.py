# Dado un número entero, crea un algoritmo que determine si es par o impar.
# Entrada
numero = int(input("Introduce un entero "))
resto = numero % 2
resultado = ""
# Proceso
if (resto) == 0:
    resultado="Es Par"
else:
    resultado="Es Inpar"
# Salida
print(f"{resultado}")