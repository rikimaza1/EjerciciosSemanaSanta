from datetime import datetime

# Crea un programa en Python que acepte una fecha como cadena de caracteres en formato "dd/mm/aaaa"

# y devuelva la fecha en formato "aaaa-mm-dd", con el año primero.

try:
    fecha = input("Introduce una fecha tipo dd/mm/aaaa : ")
    fecha = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')
    print(fecha)
except:
    print("Formato de cadena no era el esperado")

