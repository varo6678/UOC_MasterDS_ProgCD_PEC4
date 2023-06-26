# pylint: skip-file
import unittest
# from utils import *
import sys
import os
# Obtener la ruta absoluta del directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta absoluta del directorio que contiene main.py
main_dir = os.path.join(script_dir, "..")

# Añadir el directorio al PYTHONPATH
sys.path.append(main_dir)
import main_new as main
from HTMLTestRunner import HTMLTestRunner
from pandas.testing import assert_frame_equal


# Para el ejercicio 1.
class PrivateTestsPec4Ejercicio1(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.path_to_data = "../data"

    # Ejercicio 1.1.
    def test_private_ejercicio_1_1_pec4(self):
        main.ejercicio1()
        zip_file_path = os.path.join(self.path_to_data, 'twitter_reduced.zip')
        csv_file_name = 'twitter_reduced.csv'
        # Obtener el nombre del archivo sin la extensión .zip.
        zip_file_name = os.path.splitext(os.path.basename(zip_file_path))[0]
        # Comprobar que el nombre del archivo sin zip es igual al descomprimido sin csv.
        self.assertEqual(zip_file_name, os.path.splitext(csv_file_name)[0])

    # Ejercicio 1.2.
    def test_private_ejercicio_1_2_pec4(self):
        datos_dict = main.ejercicio_1_2()
        self.assertEqual(len(datos_dict), 160000)
        self.assertIn('sentiment', datos_dict[0])
        self.assertIn('id', datos_dict[0])
        self.assertIn('date', datos_dict[0])
        self.assertIn('query', datos_dict[0])
        self.assertIn('user', datos_dict[0])
        self.assertIn('text', datos_dict[0])

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