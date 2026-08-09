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

        

      
                  
              

                  

              







    
    