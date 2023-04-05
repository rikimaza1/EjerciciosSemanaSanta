import math
# Calcula el área y perímetro de un círculo dado su radio.

# Entrada
radio = float(input("Introduce radio del circulo "))
# Proceso
area = math.pi * radio * radio
perimetro = 2 * math.pi * radio
# Salida
print (f"La circunferencia con radio: {radio} tiene area {area} y perimetro {perimetro}")
