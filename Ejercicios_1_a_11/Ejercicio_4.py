# Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "12:30 AM" se convertiría en "19:30").

# La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.


from datetime import datetime
noEsValido = True

while noEsValido:
    try:
        hora12 = input(
            "Introduce una hora en formato 12h indicando AM o PM (Ejemplo: '12:30 AM')")
        hora24 = datetime.strptime(hora12, '%I:%M %p').strftime('%H:%M')
        noEsValido = False
    except:
        print("Se ha introducido datos erroneos en la hora")
print(hora24)
