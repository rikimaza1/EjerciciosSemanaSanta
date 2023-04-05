# Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

# Entrada
# Con lowee() formatearemos la cadena haciendolas ministcula
# Con replace eliminaremos los espacios de la cadena
cadena = input("Introduce una cadena de texto ").lower().replace(
    " ", "")
# Proceso
esPalindromo = True
cadenaInvertida = ""
# cadenaInvertida1 ="".join(reversed(cadena)) Otra alternativa con menos codigo
for x in cadena:
    cadenaInvertida = x+cadenaInvertida
if cadena != cadenaInvertida:
    esPalindromo = False
# Salida
resultado = "Es palindromo"if esPalindromo else "No es Palindromo"
print(resultado)
