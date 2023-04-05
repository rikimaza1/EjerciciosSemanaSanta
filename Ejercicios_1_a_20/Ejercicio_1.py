# Calcular la letra del DNI Español
import re
# Entrada
while True:
    dni = input("Introduzca el numero de dni ")
    if re.match(pattern="^\d{8}$", string=dni):
        letrasDNI="TRWAGMYFPDXBNJZSQVHLCKE"
        resto = int(dni)%23
        print(f"La letra del dni{dni} es {letrasDNI[resto]}")
        break
    else:
        print("Numero de DNI no valido introduzca un DNI de 8 digitos ")
# Proceso

# Salida
