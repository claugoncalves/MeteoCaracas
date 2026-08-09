import json
from Geografia import SectorCaracas
from Api import OpenMeteo
from Filtrado import Filtro
from Analisis import AnalizadorClima

def cargar_archivo_local(ruta):
    """
    Lee el archivo de texto y convierte cada elemento en un objeto SectorCaracas
    """
    sectores_objetos=[]
    try:
        f = open(ruta,'r', encoding= 'ut f-8')
        datos=json.load(f)
        f.close()

        for distrito_llave, listado_sectores in datos.items():
            for  item in listado_sectores:
                nuevo_obj= SectorCaracas(distrito_llave, item['localidad'], item['latitud'], item['longitud'])
                sectores_objetos.append(nuevo_obj)

        return sectores_objetos
    except FileNotFoundError:
        print('El archivo JSON no se encuentra en el directorio')
        return[]
    except Exception as e:
        print("Falla de lectura:", str(e))
        return[]


class Aplicacion:
    """
    Clase principal que envuelve toda la logica del menu y la integracion de modulos
    """
    def __init__(self,ruta_json):
        self.bd_sectores = cargar_archivo_local(ruta_json)
        self.cliente_api = OpenMeteo()
        self.herramienta_filtro = Filtro()
        self.motor_datos = AnalizadorClima()

    def resumen_arranque(self):
      """
      Imprime un reporte inicial al iniciar la aplicacion
      """
      print('\nREPORTE - CARGA DE DATOS')
      if len(self.bd_sectores)==0:
          print('Sin datos cargados')
          return

      distritos = []
      for sec in self.bd_sectores:
          if sec.distrito not in distritos:
              distritos.append(sec.distrito)
      for dis in distritos:
          contador_total = 0
          contador_buenos = 0
          contador_malos = 0
      for sec in self.bd_sectores:
          if sec.distrito == dis:
              contador_total = contador_total + 1
              if sec.es_valido():
                  contador_buenos = contador_buenos + 1
              else:
                  contador_malos = contador_malos + 1
                
      porc = 0
      if contador_total > 0:
          porc = (contador_buenos/contador_total) * 100
      print('\n - Municipio: ' + dis.uuper())
      print('Total encontrados:' + str(contador_total))
      print('Con datos validos:' + str(contador_buenos))
      print('Sin datos:' + str(contador_malos))
      print('Indice sin validez:' + str(round(porc,1)) + '%')
    print('\n')

        
    def iniciar(self):
        """
        Bucle de vida util del programa principal
        """
        if len(self.bd_sectores)==0:
           print('Aplicacion detenida por falta de datos base')
           return
        
        apagar = False
        while apagar==False:
            print('\n MENU METEOCARACAS')
            print('1) Navegar por municipio')
            print('2) Buscar sector por nombre')
            print('3) Abrir modulo de estadisticas')
            print('4) Generar reporte historico y graficas')
            print('5) Salir del sistema')

            eleccion=input('Ingresa una opcion (1-5):  ')

            if eleccion=='1' or eleccion=='2':
                objetivo=None
                if eleccion=='1':
                   objetivo= self.herramienta_filtro.explorar_por_distrito(self.bd_sectores)
                elif objetivo=='2':
                 objetivo= self.herramienta_filtro.buscar_palabra(self.bd_sectores)

                if objetivo!=None:
                  print('\n CLIMA EN VIVO:')
                  objetivo.imprimir_resumen()

                  respuesta_api=self.cliente_api.obtener_clima_vivo(objetivo.lat,objetivo.lon)

                  if respuesta_api != None:
                     respuesta_api.mostrar_panel()
                     self.motor_datos.registrar_busqueda(objetivo, respuesta_api)

            elif eleccion=='3':
               self.motor_datos.panel_sesion(self.bd_sectores)    

            elif eleccion=='4':
                objetivo_hist=self.herramienta_filtro.buscar_palabra(self.bd_sectores)

                if objetivo_hist != None:
                    print("\n FORMATO REQUERIDO: AAAA-MM-DD ")
                    f_ini=input('Fecha inicial: ')
                    f_fin=input('Fecha final: ')

                    print('Solicitando datos a Open-Meteo...')
                    arr_diario=self.cliente_api.obtener_clima_pasado(objetivo_hist.lat, objetivo_hist.lon, f_ini, f_fin )

                    if len(arr_diario)>0:
                      df_generado=  self.motor_datos.procesar_historico(arr_diario, objetivo_hist.zona)
                      menu_graficos=False
                      while menu_graficos==False:
                        print('\n1)Abrir graficos')
                        print('2)Continuar')

                        op_graf=input('Seleccione una opcion (1-2):  ')

                        if op_graf=='1':
                          print('Abriendo graficos...')
                          self.motor_datos.generar_graficas(df_generado,objetivo_hist.zona)
                          menu_graficos=True

                        elif op_graf=='2':
                           print('Omitiendo graficos...')
                           menu_graficos=True
                        else:
                         print('Error: opcion no valida.Intente de nuevo')    

            elif eleccion=='5':
               print('Apagando...\n')
               apagar=True
            else:
               print('Opcion desconocida')   





      
                  
              

                  

              







    
    