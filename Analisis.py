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

    def procesar_historico(self,arreglo_diario,nombre_zona):
        """
        Calcula records historicos y medias mensuales/generales.
        """
        print('\nREPORTE HISTORICO DE' + nombre_zona.upper())
        if len(arreglo_diario)==0:
            print('Arreglo sin datos')
            return None

        matriz=[]
        for dia in arreglo_diario:
            temp=dia.celsius if dia.celsius != None else 0
            lluv = dia.precipitacion if dia.precipitacion != None else 0
            hum = dia.porcentaje_humedad if dia.porcentaje_humedad != None else 0
            vi = dia.viento_kmh if dia.viento_kmh != None else 0
            matriz.append([dia.fecha,temp,lluv,hum,vi])

        columnas =['Calendario', 'Temp','Lluvia', 'Hum', 'Viento']
        df_clima = pd.DataFrame(matriz, columns= columnas)

        # Extraccion de indices para los records
        idx_calor = df_clima['Temp']. idxmax()
        idx_frio = df_clima['Temp'].idxmin()
        idx_lluvia= df_clima['Lluvia'].idxmax()
        idx_hum = df_clima['Hum'].idxmax()

        # Anos
        yr_calor = df_clima['Calendario']['idx_calor'][0:4]
        yr_frio = df_clima['Calendario']['idx_frio'][0:4]
        yr_lluvia = df_clima['Calendario']['idx_lluvia'][0:4]
        yr_hum = df_clima['Calendario']['idx_hum'][0:4]

        print('\nRECORDS:')
        print('- Mayor calor:' + yr_calor + '('+ str(df_clima['Temp'][idx_calor]) + 'C)')
        print('- Mayor frio:' + yr_frio + '('+ str(df_clima['Temp'][idx_frio]) + 'C)')
        print('- Mayor lluvia:' + yr_lluvia + '('+ str(df_clima['Lluvia'][idx_lluvia]) + 'mm)')
        print('- Maxima humedad:' + yr_hum + '('+ str(df_clima['Hum'][idx_hum]) + '%)')

       # Agrupacion por mes
        df_clima['Mes']= df_clima['Calendario'].str.slice(0,7)
        medias_mensuales=df_clima.groupby('Mes'),[['Calendario', 'Temp','Lluvia', 'Hum', 'Viento']].mean()

        print('\nPROMEDIO POR MES:')
        pd.set_option('display.max_rows', None)
        print(medias_mensuales.round(2))
        pd.reset_option('display.max_rows')

       # Promedios absolutos
        matriz_np = np.array(df_clima[['Calendario', 'Temp','Lluvia', 'Hum', 'Viento']])
        medias_absolutas = np.mean(matriz_np, axis=0)

        print('\nPROMEDIOS GLOBALES:')
        print('-Temperatura global:' + str(round(medias_absolutas[0], 2))+ 'C')
        print('-Lluvia global:' + str(round(medias_absolutas[1], 2))+ 'mm')
        print('-Humedad global:' + str(round(medias_absolutas[2], 2))+ '%')
        print('-Viento global:' + str(round(medias_absolutas[3], 2))+ 'kh/h')

        return medias_mensuales

    def generar_graficas(self,df_mensual,nombre_zona):
        """
        Despliega 4 graficos distintos para cada magnitud
        """
        if df_mensual is None:
            return
        fechas=list(df_mensual.index)
        val_temp = list (df_mensual['Temp'])
        val_lluvia= list (df_mensual['Lluvia'])
        val_hum = list (df_mensual['Hum'])
        val_viento = list (df_mensual['Viento'])

        total_meses=len(fechas)
        salto= total_meses// 20
        if salto ==0:
            salto=1

        puntos_x=[]
        textos_x=[]
        for i in range(0, total_meses,salto):
            puntos_x.append(i)
            textos_x.append(fechas[i])

        # Grafico de temperatura 
        plt.figure(num='Temperatura de' + nombre_zona, figsize=(10,4)) 
        plt.plot(fechas, val_temp, color='red', marker='o') 
        plt.title('Evolucion de temperatura') 
        plt.xticks(puntos_x, textos_x, rotation=45, fontsize=8)
        plt.ylabel('Celsius') 
        plt.grid(True,linestyle=':', alpha=0.6) 
        plt.tight_layout() 

        #Grafico de lluvia
        plt.figure(num='Lluvia de' + nombre_zona, figsize=(10,4)) 
        plt.bar(fechas, val_lluvia, color='blue') 
        plt.title('Acumulado de lluvias') 
        plt.xticks(puntos_x, textos_x, rotation=45, fontsize=8)
        plt.ylabel('Milimetros') 
        plt.grid(axis='y',linestyle=':', alpha=0.6) 
        plt.tight_layout() 

        #Grafico de humedad
        plt.figure(num='Humedad de' + nombre_zona, figsize=(10,4)) 
        plt.plot(fechas, val_hum, color='green', marker='s') 
        plt.title('Humedad Relativa') 
        plt.xticks(puntos_x, textos_x, rotation=45, fontsize=8)
        plt.ylabel('Porcentaje') 
        plt.grid(True,linestyle=':', alpha=0.6) 
        plt.tight_layout() 

        #Grafico de viento
        plt.figure(num='Viento de' + nombre_zona, figsize=(10,4)) 
        plt.plot(fechas, val_viento, color='orange', marker='^') 
        plt.title('Registros de viento maximo') 
        plt.xticks(puntos_x, textos_x, rotation=45, fontsize=8)
        plt.ylabel('km/h') 
        plt.grid(True,linestyle=':', alpha=0.6) 
        plt.tight_layout() 

        plt.show()
