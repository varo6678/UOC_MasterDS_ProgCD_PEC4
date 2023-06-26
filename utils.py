"""
Funciones de utilidad para el proyecto.
"""

import zipfile
import os
import datetime

def descomprimir_zip(archivo_zip: str, directorio_destino: str) -> None:
    """
    Descomprime un archivo ZIP en el directorio de destino especificado,
    verificando si los archivos ya existen en el directorio antes de la extracción.
    
    Args:
        archivo_zip (str): Ruta del archivo ZIP a descomprimir.
        directorio_destino (str): Ruta del directorio donde se extraerán los archivos.
    """
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        # Obtener la lista de nombres de archivo en el ZIP
        archivos_en_zip = zip_ref.namelist()
        
        # Verificar si los archivos ya existen en el directorio
        archivos_existentes = []
        for archivo in archivos_en_zip:
            ruta_archivo = os.path.join(directorio_destino, archivo)
            if os.path.exists(ruta_archivo):
                archivos_existentes.append(archivo)
        
        if archivos_existentes:
            print(f"Los siguientes archivos ya existen en el directorio: {archivos_existentes}")
        else:
            zip_ref.extractall(directorio_destino)
            print(f"\nArchivo ZIP descomprimido en: {directorio_destino}\n")


def cargar_stopwords(ruta_stopwords : str) -> list:
    """
    Carga los stopwords desde el archivo stopwords.txt y los devuelve como una lista.
    """
    stopwords = []
    with open(ruta_stopwords, 'r') as archivo:
        for linea in archivo:
            palabra = linea.strip().strip(',').strip("'")
            stopwords.append(palabra)

    print(f"\nStopwords cargados en lista para proceso.\n")

    return stopwords


# def cargar_stopwords(ruta_archivo : str) -> list:
#     """
#     Lee el archivo de stopwords y devuelve una lista de stopwords.
    
#     Args:
#         ruta_archivo (str): Ruta del archivo de stopwords.
    
#     Returns:
#         list: Lista de stopwords.
#     """
#     stopwords = []
#     with open(ruta_archivo, 'r') as archivo:
#         contenido = archivo.read()
#         palabras = re.findall(r"'([^']*)'", contenido) + re.findall(r'"([^"]*)"', contenido)
#         stopwords = [palabra.strip() for palabra in palabras]

#         print(len(stopwords))
#         print(f"\nStopwords cargados en lista para proceso.\n")

#     return stopwords

def RegistroPropiedadIntelectual() -> str:
    """
    Obtiene la fecha, hora y ubicación de ejecución del script.

    Autor:
        Alvaro Monforte Marin
    """

    LONGITUD_CABECERA = 79

    # Constantes > script.
    __author__ = "Alvaro Monforte Marin"
    __script__ = "Tratador de tweets"
    __version__ = "1.0"
    
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.datetime.now()

    # Obtener la ubicación del directorio actual
    ubicacion_actual = os.getcwd()

    # Formatear la fecha y hora como una cadena legible
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    # Devolver la información de ejecución
    # informacion = f"Ejecutado el {fecha_hora_formateada} \nen {ubicacion_actual}"

    # Imprimir información de ejecución
    # Imprimir el cabecero
    print()
    cabecera = f"""
    {'*' * LONGITUD_CABECERA}
    { __script__ + ' (v' + __version__ + ')':^{LONGITUD_CABECERA}}
    { __author__:^{LONGITUD_CABECERA}}
    { fecha_hora_formateada:^{LONGITUD_CABECERA}}
    { ubicacion_actual:^{LONGITUD_CABECERA}}
    {'*' * LONGITUD_CABECERA}
    """

    print(cabecera)

def final_script():
    print()
    cabecera = f"""
    {'*' * 79}
    { "Script finalizado":^{79}}
    {'*' * 79}
    """
    print(cabecera)
    print()

def buscar_archivo_csv(carpeta):
    archivos = os.listdir(carpeta)
    archivo_csv = None

    for archivo in archivos:
        if os.path.isfile(os.path.join(carpeta, archivo)) and archivo.endswith(".csv"):
            archivo_csv = os.path.join(carpeta, archivo)
            break

    return archivo_csv

def imprimir_diccionarios(dict_dict):
    # keys = list(dict_dict.keys())  # convierte las claves a una lista

    # imprimir los primeros cinco diccionarios
    print("Primeros cinco diccionarios:")
    print(dict_dict[:4])

    # imprimir los últimos cinco diccionarios
    print("Últimos cinco diccionarios:")
    print(dict_dict[-5])


