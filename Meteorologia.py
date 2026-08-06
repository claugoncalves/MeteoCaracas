class RegistroBase:
    """
    Clase padre que almacena las variables climaticas en comun. 
    """
    def __init__(self, temp_celsius, hum_porcentaje, vel_viento):
        self.celsius = temp_celsius
        self.porcentaje_humedad = hum_porcentaje
        self.viento_kmh = vel_viento 
        
class ReporteEnVivo(RegistroBase):
    """
    Clase hija que representa el clima en tiempo real, agregando el estado del cielo.
    """
    def __init__(self, temp_celsius, hum_porcentaje, vel_viento, id_cielo):
        super().__init__(temp_celsius, hum_porcentaje, vel_viento)
        self.id_cielo = id_cielo

    def interpretar_cielo(self):
        """
        Convierte el ID numerico de la API en un texto descriptivo.
        """
        if self.id_cielo == 0: return "Cielo despejado"
        elif self.id_cielo == 1: return "Mayormente despejado"
        elif self.id_cielo == 2: return "Parcialmente nublado"
        elif self.id_cielo == 3: return "Nublado (Cubierto)"
        elif self.id_cielo == 45: return "Niebla"
        elif self.id_cielo == 48: return "Niebla con escarcha"
        elif self.id_cielo == 51: return "Llovizna ligera"
        elif self.id_cielo == 53: return "Llovizna moderada"
        elif self.id_cielo == 55: return "Llovizna densa"
        elif self.id_cielo == 56: return "Llovizna helada ligera"
        elif self.id_cielo == 57: return "Llovizna helada densa"
        elif self.id_cielo == 61: return "Lluvia ligera"
        elif self.id_cielo == 63: return "Lluvia moderada"
        elif self.id_cielo == 65: return "Lluvia fuerte"
        elif self.id_cielo == 66: return "Lluvia helada ligera"
        elif self.id_cielo == 67: return "Lluvia helada fuerte"
        elif self.id_cielo == 71: return "Nieve ligera"
        elif self.id_cielo == 73: return "Nieve moderada"
        elif self.id_cielo == 75: return "Nieve fuerte"
        elif self.id_cielo == 77: return "Granos de nieve"
        elif self.id_cielo == 80: return "Chubascos ligeros"
        elif self.id_cielo == 81: return "Chubascos moderados"
        elif self.id_cielo == 82: return "Chubascos violentos"
        elif self.id_cielo == 85: return "Chubascos de nieve ligeros"
        elif self.id_cielo == 86: return "Chubascos de nieve fuertes"
        elif self.id_cielo == 95: return "Tormenta electrica"
        elif self.id_cielo == 96: return "Tormenta con granizo ligero"
        elif self.id_cielo == 99: return "Tormenta con granizo fuerte"
        else: return "Desconocido"
    
