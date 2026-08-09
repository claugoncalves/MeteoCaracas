from App import Aplicacion

if __name__=='__main__':
    """
    Script de ejecucion inicial. Importa la clase principal y la arranca
    """
    sistema=Aplicacion('zonas_caracas.json')
    sistema.resumen_arranque()
    sistema.iniciar()