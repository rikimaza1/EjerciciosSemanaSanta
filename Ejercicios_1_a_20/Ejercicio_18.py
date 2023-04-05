# Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.
# Entrada
cadena1 = input("Introduce la primera cadena de texto ")
cadena2 = input("Introduce la segunda cadena de texto ")
# Proceso
# manipularemos las cadenas para que con lower sean todas minusculas y con replace eliminaremos los expacios
cadena1 = cadena1.lower().replace(" ", "")
# manipularemos las cadenas para que con lower sean todas minusculas y con replace eliminaremos los expacios
cadena2 = cadena2.lower().replace(" ", "")
# manipularemos las cadenas con sorted que devuelve una lista con las letras ordenas junto con join a un carancter vacio crearemos un str ordenado
cadena1Ordenada = ''.join(sorted(cadena1))
# manipularemos las cadenas con sorted que devuelve una lista con las letras ordenas junto con join a un carancter vacio crearemos un str ordenado
cadena2Ordenada = ''.join(sorted(cadena2))
esPalindramo = True
if cadena1Ordenada != cadena2Ordenada:
    esPalindramo = False
resultado = "Es palindramo" if esPalindramo else "No es palindramo"
# Salida
print(resultado)
