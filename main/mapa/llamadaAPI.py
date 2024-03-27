import time
import geocoder

def hacer_solicitud_geocoder_osm(address, user_agent):
    response = geocoder.osm(address, user_agent=user_agent)
    time.sleep(1)  # Espera 1 segundo entre cada solicitud
    return response