class Coordenada:
    """
    Clase base que representa una ubicacion espacial mediante latitud y longitud.
    """
    def __init__(self, latitud, longitud):
        self.lat = latitud
        self.lon = longitud 
    
    def es_valido(self):
        """
        Retorna True si el punto tiene coordenadas reales, o False si son nulas.
        """
        if self.lat != None and self.lon != None:
            return True 
        return False  