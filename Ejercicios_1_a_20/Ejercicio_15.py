# Crea un algoritmo que determine si un número es positivo, negativo o cero.
# Entrada
numero = float(input("Introduce un numero"))
# Proceso
resultado= ""
if numero > 0:
    resultado = "Positivo"
elif numero < 0:
    resultado = "Negativo"
else:
    resultado = "cero"
# Salida
print(f"El numero introducio {numero} es {resultado}")