# Dado un número entero, crea un algoritmo que determine si es primo o no.
# Entrada
numero = int(input("Introduce un numero entero "))
# Proceso
divisores = 0
resultado = ""
for x in range(1, numero+1):
    if (numero % x) == 0:
        divisores += 1
if divisores == 2:
    resultado= "Es primo"
else:
    resultado= "No es primo"
# Salida
print(f"{numero} {resultado}")