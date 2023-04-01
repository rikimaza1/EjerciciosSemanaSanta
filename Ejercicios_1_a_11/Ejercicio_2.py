from datetime import datetime
from pytz import timezone
import pytz

# Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona.

# El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

zonaHoraria = input("Introduce tu zona horaria Continente/Ciudad ")
listaZonasHorarias = pytz.all_timezones
try:
    indiceZonaHoraria = pytz.all_timezones.index(zonaHoraria)
    try:
        print(datetime.now(timezone(listaZonasHorarias[indiceZonaHoraria])))
    except:
        print("No se ha podido escribir la fecha actual de la {zonaHoraria}")
except:
    print("Zona horaria no reconocida")
