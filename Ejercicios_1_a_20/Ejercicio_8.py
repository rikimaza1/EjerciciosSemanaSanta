# Crea un algoritmo que determine si un año es bisiesto o no.
# Entrada
anyo = int(input("Introduce un año "))
# Proceso
resultado = ""
resto = anyo % 4
divisible100 = anyo % 100
divisible400 =anyo % 400
if ((resto == 0) and ((divisible100!=0) or (divisible400==0)) ):
    resultado = "Es bisiesto"
else:
    resultado = "No es bisiesto"
# Salida
print(f"{resultado}")