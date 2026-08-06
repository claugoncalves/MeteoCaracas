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
    
    class SectorCaracas(Coordenada):
        """
        Hereda de Coordenada. Representa una zona especifica dentro de la capital.
        """
        def __init__(self, nom_distrito, nom_zona, latitud, longitud):
            super().__init__(latitud, longitud)
            self.distrito = nom_distrito
            self.zona = nom_zona
        
        def imprimir_resumen(self):
            """
            Imprime la informacion basica del sector.
            """
            print("- " + self.distrito.upper() + ": " + self.zona + " (Coordenadas: " + str(self.lat) + "," + str(self.lon) + ")") 
            