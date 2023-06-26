
"""
Script constructuor de un analizador de tweets. Mediante la creacion
de una clase.
"""

# Libreria de DataFrames.
import pandas as pd

# Libreria de Sistemas.
import os

# Libreria de expresiones regulares.
import re

# Apoyo a diccionarios.
from collections import Counter
from collections.abc import Set

# Nube de palabras.
from wordcloud import WordCloud

# Apoyo a Hints.
from typing import List, Dict, Tuple

# Graficos.
import matplotlib.pyplot as plt

# Test > produccion > personal.
import unittest

# Tratamiento de .csv.
import csv

# Numeros aleatorios para ayudar en el testeo.
import random


ruta_datos = "./data/twitter_reduced.csv"

stopwords_pec = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
    'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
    'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
    'itself', 'they', 'them', 'their', 'theirs', 'themselves','what',
    'which', 'who', 'whom', 'this', 'that', 'these',
    'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of',
    'at', 'by', 'for', 'with', 'about', 'against',
    'between', 'into', 'through', 'during','before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
    'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
    'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
    'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
    ] 


class TwitterAnalizador:
    """
    Esta clase se encarga de analizar los tweets de un fichero csv.
    Los valores de la variable sentimient se encuentran descritos en:
    https://www.kaggle.com/datasets/kazanova/sentiment140
    """

    def __init__(self, directorio_datos: str) -> None:
        """
        Inicializa el analizador.
        """
        self.directorio_datos = directorio_datos
        self.datos = []
        self.sentimiento = {
            'positivo': 0, 
            'negativo': 4,
        }

    def cargar_datos_de_csv(self) -> Tuple[pd.DataFrame, Dict]:
        """
        Carga los datos del fichero csv tanto como un DataFrame como
        un diccionario, para que el usuario los pueda usar como crea.
        """
        assert os.path.splitext(self.directorio_datos)[1] == '.csv', \
            "El archivo no es un archivo CSV."

        self.datos = pd.read_csv(self.directorio_datos) # Como DataFrame.
        self.datos_dict = self.datos.to_dict('records') # Como diccionario.
        return self.datos, self.datos_dict

    @staticmethod
    def validacion_longitud(tweet):
        """
        Comprueba que la longitud del tweet sea menor
        o igual a 280 caracteres.
        """
        return len(tweet['text']) <= 280

    def informacion(self, df) -> None:
        """
        Imprime información sobre el DataFrame.
        """
        print(f"El DataFrame tiene {df.shape[0]}\
                    filas y {df.shape[1]} columnas.")

    def print_columnas(self, num_cols=5) -> None:
        """
        Imprime las columnas del DataFrame.
        """
        for columna in self.datos.columns[:num_cols]:
            print(columna)

    def preprocesamiento_de_texto(self, datos_dict : Dict) -> None:
        """
        Realiza el preprocesamiento del texto en cada registro del dataset.
        Elimina URLs, caracteres especiales no ASCII y símbolos, 
        y convierte el texto a minúsculas.

        """
        for registro in datos_dict:
            texto = registro['text']
            # Eliminar URLs
            texto = re.sub(r'http\S+', '', texto)
            # Eliminar caracteres especiales no ASCII y símbolos
            texto = re.sub(r'[^\x00-\x7F]+', ' ', texto)
            texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
            # Convertir a minúsculas
            texto = texto.lower()
            registro['text'] = texto
        
        # Verificar si hay rastros de URLs
        sample_registro = random.choice(datos_dict)
        assert 'http' not in sample_registro['text'], \
            "Se encontró una URL después del preprocesamiento."
        
        print("\nPreprocesamiento de texto completado.")

    def quitar_stopwords(self, datos_dict, stopwords: List[str]) -> None:
        """
        Elimina las stopwords de los textos en cada registro del dataset.

        Args:
            stopwords (list): Lista de palabras stopwords a eliminar.

        """
        assert len(stopwords) != stopwords_pec, \
                "La lista de stopwords no es correcta."

        for record in datos_dict:
            text = record['text']
            words = text.split()
            # Eliminar stopwords
            words = [word for word in words if word not in stopwords]
            text = ' '.join(words)
            record['text'] = text
        
        print("Stopwords eliminados.")

    def obtener_frecuencias(self, datos_dict) \
        -> Tuple[List[Dict[str, int]], List[str]]:
        """
        Calcula las frecuencias de términos en el dataset
        y devuelve una lista de diccionarios que
        representan las frecuencias de cada término 
        en cada registro, junto con el vocabulario ordenado.

        Returns:
            term_frequencies (list): Lista de diccionarios que contienen
                            las frecuencias de términos para cada registro.
            sorted_vocabulary (list): Lista ordenada que representa 
                            el vocabulario único del dataset.
        """
        term_frequencies: List[Dict[str, int]] = []
        vocabulary: Set[str] = set()
        for record in datos_dict:
            text: str = record['text']
            words: List[str] = text.split()
            freq: Dict[str, int] = {}
            for word in words:
                freq[word] = freq.get(word, 0) + 1
                vocabulary.add(word)
            term_frequencies.append(freq)
        sorted_vocabulary: List[str] = sorted(list(vocabulary))

        print("\nFrecuencias de términos obtenidas.")

        return term_frequencies, sorted_vocabulary
    
    def adhesion_frecuencias(self, datos_dict) -> None:
        """
        Agrega las frecuencias de términos al dataset.

        """
        term_frequencies, _ = self.obtener_frecuencias(datos_dict)
        for i, record in enumerate(datos_dict):
            record['term_frequencies'] = term_frequencies[i]

        print("\nFrecuencias de términos agregadas al dataset.")

    def guardar_dataset_en_csv(self, datos_dict, output_path: str):
        """
        Guarda el dataset procesado en un archivo CSV.

        Args:
            output_path (str): Ruta del archivo de salida.

        """
        fieldnames = datos_dict[0].keys()
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datos_dict)

        print("Dataset guardado en CSV.")

    # def generar_wordclouds(self, datos_dict, all_clusters = True) -> None:
    #     """
    #     Genera una nube de palabras para un cluster específico.

    #     Args:
    #         cluster (str): Sentimiento del cluster.

    #     """
    #     texts = [record['text'] for record in datos_dict if record['sentiment'] == cluster]
    #     wordcloud = WordCloud().generate(' '.join(texts))
    #     plt.imshow(wordcloud, interpolation='bilinear')
    #     plt.axis('off')
    #     try:
    #         plt.show()
    #         print("WordClouds generados.")
    #     except Exception:
    #         print("generar_wordclouds.")

    def get_clusters(self, datos_dict) -> int:
        """
        Obtiene el número de clusters en el dataset.

        Returns:
            int: Número de clusters.

        """
        clusters = set()
        for record in datos_dict:
            clusters.add(record['sentiment'])
        return len(clusters)
    
    # def generar_wordclouds_para_sentimientos(self, datos_dict, all_clusters=True, cluster=None):
    #     """
    #     Genera una nube de palabras para un cluster específico o todos los clusters, 
    #     dependiendo de la bandera all_clusters.

    #     Args:
    #         datos_dict (dict): Diccionario con los datos.
    #         all_clusters (bool): Bandera para generar wordclouds para todos los clusters.
    #         cluster (str, optional): Sentimiento del cluster para el cual generar la nube de palabras.

    #     """
    #     if all_clusters:
    #         clusters = set()
    #         for record in datos_dict:
    #             clusters.add(record['sentiment'])

    #         for cluster in clusters:
    #             self.generar_wordclouds(datos_dict, cluster)

    #     elif cluster is not None:
    #         self.generar_wordclouds(datos_dict, cluster)

    #     else:
    #         print("Debe proporcionar un valor para 'cluster' o establecer 'all_clusters' en True.")


    def generar_wordclouds(self, datos_dict, cluster) -> None:
        """
        Genera una nube de palabras para un cluster específico.

        Args:
            cluster (str): Sentimiento del cluster.

        """
        texts = [record['text'] for record in datos_dict if record['sentiment'] == cluster]
        wordcloud = WordCloud().generate(' '.join(texts))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        try:
            plt.show()
            print("WordCloud generado!.")
        except Exception:
            print("Error al generar wordcloud!.")

    def generar_wordclouds_para_sentimientos(self, datos_dict, all_clusters=True, cluster=None):
        """
        Genera una nube de palabras para un cluster específico o todos los clusters, 
        dependiendo de la bandera all_clusters.

        Args:
            datos_dict (dict): Diccionario con los datos.
            all_clusters (bool): Bandera para generar wordclouds para todos los clusters.
            cluster (str, optional): Sentimiento del cluster para el cual generar la nube de palabras.

        """
        if all_clusters:
            clusters = set(record['sentiment'] for record in datos_dict)
            for cluster in clusters:
                self.generar_wordclouds(datos_dict, cluster)
        elif cluster is not None:
            self.generar_wordclouds(datos_dict, cluster)
        else:
            print("Debe proporcionar un valor para 'cluster' o establecer 'all_clusters' en True.")

    def has_empty_text_entries(self, datos_dict) -> bool:
        """
        Verifica si hay entradas de texto vacías en el dataset.

        Returns:
            bool: True si hay entradas de texto vacías, False en caso contrario.

        """
        empty_entries = [record for record in datos_dict if record['text'] == '']
        return len(empty_entries) > 0

    def get_empty_text_percentage(self, datos_dict) -> float:
        """
        Obtiene el porcentaje de entradas de texto vacías en el dataset.

        Returns:
            float: Porcentaje de entradas de texto vacías.

        """
        empty_entries = [record for record in datos_dict if record['text'] == '']
        return (len(empty_entries) / len(datos_dict)) * 100
    
    def get_all_frequencies(self, datos_dict):
        all_frequencies = []
        for record in datos_dict:
            print(f"Type: {type(record['term_frequencies'])}, Value: {record['term_frequencies']}")
            try:
                all_frequencies.extend(record['term_frequencies'].values())
            except AttributeError:
                print(f"Error: record['term_frequencies'] is not a dictionary as expected. It is a {type(record['term_frequencies'])}")
        return all_frequencies
    
    def plot_histograma(self, datos_dict):
        all_frequencies = self.get_all_frequencies(datos_dict)
        
        plt.figure(figsize=(10,5))
        plt.hist(all_frequencies, bins=50, alpha=0.5, color='g', edgecolor='black')
        plt.title('Histograma de Frecuencias de Términos')
        plt.xlabel('Frecuencia')
        plt.ylabel('Cantidad de Términos')
        plt.grid(True)
        try:
            plt.show()
            print("El histograma se ejecutó correctamente.")
        except Exception:
            print("Error al ejecutar plot_histograma.")

    def plot_histograma_por_sentimiento(self, datos_dict):
        # Creamos un diccionario que almacenará las frecuencias por sentimiento
        freqs_por_sentimiento = {}
        for record in datos_dict:
            sentimiento = record['sentiment']
            if sentimiento not in freqs_por_sentimiento:
                freqs_por_sentimiento[sentimiento] = []
            freqs_por_sentimiento[sentimiento].extend(record['term_frequencies'].values())

        # Generamos un histograma por cada sentimiento
        for sentimiento, frecuencias in freqs_por_sentimiento.items():
            plt.figure(figsize=(10,5))
            plt.hist(frecuencias, bins=50, alpha=0.5, color='g', edgecolor='black')
            plt.title(f'Histograma de Frecuencias de Términos para el sentimiento: {sentimiento}')
            plt.xlabel('Frecuencia')
            plt.ylabel('Cantidad de Términos')
            plt.grid(True)
            try:
                plt.show()
                print(f"El histograma para el sentimiento {sentimiento} se ejecutó correctamente.")
            except Exception:
                print(f"Error al ejecutar plot_histograma para el sentimiento {sentimiento}.")

