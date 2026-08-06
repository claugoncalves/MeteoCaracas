class RegistroBase:
    """
    Clase padre que almacena las variables climaticas en comun. 
    """
    def __init__(self, temp_celsius, hum_porcentaje, vel_viento):
        self.celsius = temp_celsius
        self.porcentaje_humedad = hum_porcentaje
        self.viento_kmh = vel_viento 
        