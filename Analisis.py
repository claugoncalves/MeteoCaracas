import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class AnalizadorClima:
    """
    Motor analitico del sistema. Guarda busquedas en vivo y procesa datos usando Pandas y Numpy.
    """
    def __init__(self):
        self.historial_vivo =[]
        self.historial_sectores=[]

    def registrar_busqueda(self, sector, reporte_vivo):
        """
        Almacena temporalmente una busqueda exitosa.
        """
        self.historial_sectores.append(sector)
        self.historial_vivo.append(reporte_vivo)

    def panel_sesion(self, array_sectores_total):
        """
        Despliega un submenu para estionar los reportes de la sesion actual.
        """
        volver=False
        while volver == False:
            print('\nMODULO DE ANALISIS Y ESTADISTICAS')
            print('1)Ver Ranking de temperaturas y promedio')
            print('2)Ver zonas sin datos')
            print('3)Volver al menu principal')
            
            op= input('Selecciona una accion: ')

            if op=='1':
                if len(self.historial_vivo) == 0:
                    print('Aun no hay registros en la seccion actual.')
                else:
                    max_celsius= self.historial_vivo[0].celsius
                    min_celsius= self.historial_vivo[0].celsius
                    lugar_calor= self.historial_sectores[0].distrito + " - " + self.historial_sectores[0].zona
                    lugar_frio=self.historial_sectores[0].distrito + " - " + self.historial_sectores[0].zona

                    acumulador_temp= 0
                    i=0
                    while i < len(self.historial_vivo):
                        rep= self.historial_vivo[i]
                        sec= self.historial_sectores[i]

                        acumulador_temp = acumulador_temp + rep.celsius

                        if rep.celsius > max_celsius:
                            max_celsius = rep.celsius
                            lugar_calor = sec.distrito + '-' + sec.zona
                        if rep.celsius < min_celsius:
                            min_celsius = rep.celsius
                            lugar_frio = sec.distrito + '-' + sec.zona

                        i = i + 1

                    media = acumulador_temp / len(self.historial_vivo)

                    print('\nRESULTADOS:')
                    print('Record maximo: ' + lugar_calor + 'con' + str(max_celsius) + 'C')
                    print('Record minimo: ' + lugar_frio + 'con' + str(min_celsius) + 'C')
                    print('Media de temperaturas consultadas: ' + str(round(media, 2)) + 'C')

            elif op=='2':
                print('\MUNICIPIOS SIN COORDENADAS')
                distritos_unicos=[]
                for sec in array_sectores_total:
                    if sec.distrito not in distritos_unicos:
                        distritos_unicos.append(sec.distrito)

                faltan_datos=False
                for d in distritos_unicos:
                    vacios=[]
                    for sec in array_sectores_total:
                        if sec.distrito == d and sec.es_valido() == False:
                            vacios.append(sec.zona)

                    if len(vacios)>0:
                        faltan_datos=True
                        print('\nMunicipio ' + d.upper() + ':')
                        for vac in vacios:
                            print('-'+ vac)

                    if faltan_datos==False:
                        print("Todos los sectores tienen coordenadas")

            elif op=='3':
                volver=True
            else:
                print('Opcion invalida')


