import time
import geocoder

def hacer_solicitud_geocoder_osm(address, user_agent):
    headers = {
        'User-Agent': user_agent
    }
    response = geocoder.osm(address, user_agent=user_agent)
    time.sleep(2)  # Espera 2 segundos entre cada solicitud
    return response