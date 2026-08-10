class Filtro:
    """
    Herramienta para recorrer la lista de sectores y filtrar resultados validos por consola.
    """

    def explorar_por_distrito(self, array_sectores):
        """
        Navegacion por niveles: Muestra distritos, pide elegir uno y luego pide elegir un sector.
        """
        print("\nEXPLORADOR DE MUNICIPIOS:")
        lista_distritos = []
        for sec in array_sectores:
            if sec.distrito not in lista_distritos:
                lista_distritos.append(sec.distrito)

        for dis in lista_distritos:
            print("- " + dis)

        seleccion = input("\nIngrese el nombre del distrito que desea explorar: ")

        validos = []
        for sec in array_sectores:
            if seleccion.lower() in sec.distrito.lower() and sec.es_valido():
                validos.append(sec)

        if len(validos) == 0:
            print("Distrito invalido o no posee localidades con coordenadas.")
            return None

        print("\nLocalidades habilitados en " + seleccion.upper() + ":")
        for val in validos:
            print("- " + val.zona)

        seleccion_zona = input("Escribe el nombre del sector: ")
        for val in validos:
            if seleccion_zona.lower() in val.zona.lower():
                return val

        print("No se encontro el sector ingresado en la lista.")
        return None
    def buscar_palabra(self, array_sectores):
        """
        Busca coincidencias de texto en todo el arreglo y muestra resultados numerados.
        """
        palabra = input("Nombre localidad:")

        resultados = []
        for sec in array_sectores:
            if palabra.lower() in sec.zona.lower() and sec.es_valido():
                resultados.append(sec)
        if len(resultados) == 0:
            print("No se encontraron resultados.")
            return None

        print("\nCoincidencias:")
        idx = 1
        for res in resultados:
            print(str(idx) + ") " + res.zona + " | Distrito: " + res.distrito)
            idx = idx + 1

        op = input("\nElige el numero")   
        if op.isdigit():
            num = int(op) - 1
            if num >= 0 and num < len(resultados):
                return resultados[num]
        print("Seleccion invalida.")     
        return None
    

            




