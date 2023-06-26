# pylint: skip-file
import unittest
# from utils import *
from main import *
from HTMLTestRunner import HTMLTestRunner
from pandas.testing import assert_frame_equal
import os

# import sys
# # Obtener la ruta absoluta del directorio del script actual
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Obtener la ruta absoluta del directorio que contiene main.py
# main_dir = os.path.join(script_dir, "..")

# # Añadir el directorio al PYTHONPATH
# sys.path.append(main_dir)

DATA = "../data"

# Para el ejercicio 1.
class PrivateTestsPec4Ejercicio1(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.path_to_data = DATA

    # Ejercicio 1.1.
    def test_private_ejercicio_1_1_pec4(self):
        zip_file_path = os.path.join(self.path_to_data, 'twitter_reduced.zip')
        csv_file_name = 'twitter_reduced.csv'
        # Obtener el nombre del archivo sin la extensión .zip.
        zip_file_name = os.path.splitext(os.path.basename(zip_file_path))[0]
        # Comprobar que el nombre del archivo sin zip es igual al descomprimido sin csv.
        self.assertEqual(zip_file_name, os.path.splitext(csv_file_name)[0])

    # Ejercicio 1.2.
    def test_private_ejercicio_1_2_pec4(self):
        # Llamar a main() para ejecutar el código
        resultado = main(args.input, args.stopwords, args.output)

        # Comprobación de longitud
        self.assertEqual(len(resultado), 160000)

        # Comprobación de las claves en cada diccionario
        claves_esperadas = ['sentiment', 'id', 'date', 'query', 'user', 'text']
        for registro in resultado:
            self.assertCountEqual(claves_esperadas, registro.keys())

        # Mostrar los 5 primeros registros del dataset
        print("Los 5 primeros registros del dataset:")
        for i, registro in enumerate(resultado[:5]):
            print(f"Registro {i+1}: {registro}")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PrivateTestsPec4Ejercicio1))

    runner = HTMLTestRunner(log=True, 
                            verbosity=2, 
                            output='reports',
                            title='PAC4', 
                            description='PAC4 private tests',
                            report_name='Private tests',
                            tested_by="Alvaro Monforte Marin"
                            )
    runner.run(suite)