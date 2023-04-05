# Crea un algoritmo que determine si un número es capicúa o no.
import math
# Entrada
numero = int(input("Introduce un numero entero para saber si es capicúa o no "))
# Proceso
esCapicua = True
if numero < 0 :
    esCapicua=False
elif numero > 9:
    numeroIvertido=0
    resto = True
    auxiliar=numero
    auxiliar2=0
    while auxiliar!=0:
        auxiliar2 = auxiliar % 10
        numeroIvertido = numeroIvertido * 10 +(auxiliar2)
        auxiliar=math.trunc(auxiliar/10)
    if numero!=numeroIvertido:
        esCapicua = False       
resultado ="Es capicúa" if esCapicua else "No es capicúa"
# Salida
print(resultado)