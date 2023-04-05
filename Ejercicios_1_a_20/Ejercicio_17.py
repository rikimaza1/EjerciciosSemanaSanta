# Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo.
# El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, 
# hasta que el usuario adivine el número correcto.
import random
# Entrada
# Proceso
aleatorio = random.randint(1,100)
adivinado = False
resultado = ""
while not adivinado:
    entrada = int(input("Introduce un numero para adivinar: "))
    if(entrada==aleatorio):
        resultado=f"Has adivinado el numero era {aleatorio}"
        adivinado = True
    elif(entrada>aleatorio):
        print("Has introducido un numero mayor que el aleatorio")
    elif(entrada<aleatorio):
        print("Has introducido un numero menor que el aleatorio")
# Salida
print(resultado)