import requests
from Meteorologia import ReporteEnVivo, ReporteDiario 
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
        try:
            peticion = requests.get (self.enlace_vivo, params=params, timeout=10)
            if peticion.status_code == 200:
                json_resp = peticion.json ()
                temp = json_resp["current"]["temperature_2m"]
                hum = json_resp["current"]["relative_humidity_2m"] 
                viento = json_resp["current"]["wind_speed_10m"]
                cielo = json_resp["current"]["weather_code"]

                return ReporteEnVivo (temp, hum, viento, cielo)
            else: 
                print ("Fallo en la API, codigo:", peticion.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print ("sin internet o error de red:", e)
            return None
    def obtener_clima_pasado (self, lat, lon, inicio, fin):    
        """
        Descarga el archivo historico y retorna un arreglo lleno de objetos ReporteDiario.
        """
        params = {
        "latitude" : lat,
        "longitude" : lon, 
        "start_date" : inicio,
        "end_date" : fin,
        "daily" : "temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean,wind_speed_10m_max",
            "timezone": "auto"
        }
        try:
            peticion = requests.get (self.enlace_pasado, params=params, timeout=15)
            if peticion.status_code == 200:
                json_resp = peticion.json ()
                historial_objetos = []
                if "daily" not in json_resp:
                    print("No existe datos para el rango de fechas solicitado.")
                    return historial_objetos
                #Extraemos los datos a variables locales 
                arr_fechas = json_resp["daily"]["time"]
                arr_temp = json_resp["daily"]["temperature_2m_mean"]
                arr_lluvia = json_resp["daily"]["precipitation_sum"]
                arr_hum = json_resp["daily"]["relative_humidity_2m_mean"]
                arr_viento = json_resp["daily"]["wind_speed_10m_max"]

                i = 0
                while i < len(arr_fechas):
                    obj_dia = ReporteDiario(
                        arr_fechas[i],
                        arr_temp[i],
                        arr_lluvia[i],
                        arr_hum[i],
                        arr_viento[i]
                    )
                    historial_objetos.append(obj_dia)
                    i = i + 1
                return historial_objetos
            else:
                print ("Fallo en la API, codigo:", peticion.status_code)
                return []
        except requests.exceptions.RequestException as e:
            print ("sin internet o error de red:", e)
            return []
        
            


        

