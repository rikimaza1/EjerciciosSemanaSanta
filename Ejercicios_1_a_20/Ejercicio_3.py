# Determinar la ruta para llegar a una ciudad por avión.
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='API_KEY')
# Peticion de direciones por el medio de avion
now = datetime.now()
directions_result = gmaps.directions(
    "Madrid", "Barcelona", mode="airplane", departure_time=now)
