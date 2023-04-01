# Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene.

#El programa debe utilizar un bucle while para recorrer la cadena y contar las palabras.

cadena = input("Introduce una cadena ")
contadorPalabras=0
i = 0
while (i<len(cadena)):
    if(cadena[i]==' ' or i==len(cadena)-1):
        contadorPalabras+=1
    i+=1
print(f"Hay {contadorPalabras} palabras")    