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
