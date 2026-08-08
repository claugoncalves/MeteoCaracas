from Meteorologia import Meteorologia
class OpenMeteo:
    """
    Se encarga de realizar las peticiones web a los servidores de Open-Meteo para obtener datos.
    """
    def __init__(self):
        self.enlace_vivo = "https://api.open-meteo.com/v1/forecast"
        self.enlace_pasado = "https://archive-api.open-meteo.com/v1/archive"
    def obtener_clima_vivo (self, lat, lon):
        """
        Pide el clima actual a la API y devuelve un objeto de tipo ReporteEnVivo.
        """
        params = {
        "latitude" : lat,
        "longitude" : lon, 
        "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
         }
        

