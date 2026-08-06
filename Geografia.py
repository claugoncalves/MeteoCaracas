class Coordenada:
    """
    Clase base que representa una ubicacion espacial mediante latitud y longitud.
    """
    def __init__(self, latitud, longitud):
        self.lat = latitud
        self.lon = longitud 