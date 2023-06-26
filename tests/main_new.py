import argparse
import os
from tratador_twitters import TwitterAnalizador

from utils import descomprimir_zip
from utils import cargar_stopwords
from utils import RegistroPropiedadIntelectual
from utils import final_script
from utils import buscar_archivo_csv


DATA = "./data/"
DATA_IN = DATA + "twitter_reduced.zip"
DATA_CSV = DATA + "twitter_reduced.csv"
DATA_STOPWORDS = "./" + "stopwords.txt"
DATA_OUT = DATA + "twitter_processed.csv"

# stopwords_pec = [
#     'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
#     'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
#     'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
#     'itself', 'they', 'them', 'their', 'theirs', 'themselves','what',
#     'which', 'who', 'whom', 'this', 'that', 'these',
#     'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
#     'being', 'have', 'has', 'had', 'having', 'do', 'does',
#     'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
#     'or', 'because', 'as', 'until', 'while', 'of',
#     'at', 'by', 'for', 'with', 'about', 'against',
#     'between', 'into', 'through', 'during','before', 'after', 'above',
#     'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
#     'off', 'over', 'under', 'again', 'further',
#     'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
#     'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
#     'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
#     's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
#     ] 
    
# Registro y propieadad intelectual.
RegistroPropiedadIntelectual()

# Ejercicio 1.1. (descomprimir zip)
def ejercicio_1_1():
    descomprimir_zip(DATA_IN, DATA)

archivo_csv = buscar_archivo_csv(DATA)
analizador = TwitterAnalizador(archivo_csv)

# Ejercicio 1.2.
def ejercicio_1_2():
    datos = analizador.cargar_datos_de_csv()
    datos_dict = datos[1]
    return datos_dict

# Ejercicio 2.1.
def ejercicio_2_1():
    datos_dict = ejercicio_1_2()
    analizador = TwitterAnalizador(archivo_csv)
    analizador.preprocesamiento_de_texto(datos_dict)
    return datos_dict

# Ejercicio 2.2.
def ejercicio_2_2():
    datos_dict = ejercicio_2_1()
    stopwords = cargar_stopwords(DATA_STOPWORDS)
    analizador.quitar_stopwords(datos_dict, stopwords)
    return datos_dict

# Ejercicio 3.
def ejercicio_3():
    datos_dict = ejercicio_2_2()
    analizador.obtener_frecuencias(datos_dict)
    return datos_dict

# Ejercicio 4.1.
def ejercicio_4_1():
    datos_dict = ejercicio_3()
    analizador.adhesion_frecuencias(datos_dict)
    return datos_dict

# Ejercicio 4.2 
def ejercicio_4_2():
    datos_dict = ejercicio_4_1()
    analizador.guardar_dataset_en_csv(datos_dict, DATA_OUT)
    return datos_dict

analizador_procesados = TwitterAnalizador(DATA_OUT)

# Ejercicio 5.    analizador = TwitterAnalizador(archivo_csv)
def ejercicio_5():
    datos_procesados = analizador_procesados.cargar_datos_de_csv()
    datos_procesados_dict = datos_procesados[1]
    analizador_procesados.generar_wordclouds_para_sentimientos(datos_procesados_dict)
    return datos_procesados_dict

# Ejercicio 6.
def ejercicio_6():
    datos_procesados_dict = ejercicio_5()
    analizador_procesados.plot_histograma_por_sentimiento(datos_procesados_dict)
    return datos_procesados_dict

# Ejercicio 7.

final_script()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercise", type=float, help="Es el numero de ejercicio a ejecutar")
    args = parser.parse_args()

    if args.exercise:
        exercise_number = args.exercise
        if exercise_number == 1.1:
            ejercicio_1_1()
        elif exercise_number == 1.2:
            ejercicio_1_2()
        elif exercise_number == 2.1:
            ejercicio_2_1()
        elif exercise_number == 2.2:
            ejercicio_2_2()
        elif exercise_number == 3:
            ejercicio_3()
        elif exercise_number == 4.1:
            ejercicio_4_1()
        elif exercise_number == 4.2:
            ejercicio_4_2()
        elif exercise_number == 5:
            ejercicio_5()
        elif exercise_number == 6:
            ejercicio_6()
        else:
            print("Numero de ejercicio invalido")
    else:
            # Registro y propieadad intelectual.
        RegistroPropiedadIntelectual()

        # Ejercicio 1.1. (descomprimir zip)
        descomprimir_zip(DATA_IN, DATA)

        # Ejercicio 1.2.
        archivo_csv = buscar_archivo_csv(DATA)
        analizador = TwitterAnalizador(archivo_csv)
        datos = analizador.cargar_datos_de_csv()
        datos_dict = datos[1]

        # Ejercicio 2.1.
        analizador.preprocesamiento_de_texto(datos_dict)

        # # Ejercicio 2.2.
        stopwords = cargar_stopwords(DATA_STOPWORDS)
        # analizador.quitar_stopwords(datos_dict, stopwords_pec)
        analizador.quitar_stopwords(datos_dict, stopwords)

        # Ejercicio 3. (Crear el diccionario)
        analizador.obtener_frecuencias(datos_dict)

        # # Ejercicio 4.1.
        analizador.adhesion_frecuencias(datos_dict)

        # # Ejercicio 4.2 
        analizador.guardar_dataset_en_csv(datos_dict, DATA_OUT)

        # Ejercicio 5.    analizador = TwitterAnalizador(archivo_csv)
        analizador_procesados = TwitterAnalizador(DATA_OUT)
        datos_procesados = analizador_procesados.cargar_datos_de_csv()
        datos_procesados_dict = datos_procesados[1]
        analizador_procesados.generar_wordclouds_para_sentimientos(datos_procesados_dict)

        # Ejercicio 6.
        datos_procesados_dict = datos_procesados[1]
        analizador_procesados.plot_histograma(datos_procesados_dict)

        # Ejercicio 7.

        final_script()
