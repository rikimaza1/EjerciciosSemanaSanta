# Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh").

# El programa debe utilizar un bucle for para recorrer la cadena y construir la cadena invertida.

cadena = input("Introduce una cadena de caracteres ")
cadenaInvertida=""
for x in cadena:
  cadenaInvertida = x+cadenaInvertida

print(cadenaInvertida)