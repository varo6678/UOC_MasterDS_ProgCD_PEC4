# Mi Proyecto de Twitter

Este repositorio contiene el código fuente para un proyecto que maneja y procesa datos de Twitter. 

[Repositorio del proyecto](https://github.com/varo6678/UOC_MasterDS_ProgCD_PEC4)


## Estructura del Proyecto

El programa principal del proyecto es `main_new.py`, que utiliza una clase contenida en el archivo `tratador_twitters.py` para ayudar a resolver de forma modular los problemas planteados. Este último archivo también proporciona algunas utilidades que facilitan ciertas tareas.

Además, hay un archivo `.txt` que contiene una lista de stopwords que será leída por la clase en `tratador_twitters.py`. 

El directorio del proyecto debe incluir una carpeta llamada `data` que contiene el archivo `twitter_reduce.zip` proporcionado. Este archivo se descomprimirá para revelar un archivo `.csv` que será preprocesado durante la ejecución del programa.

Por último, el proyecto contiene una carpeta `tests` donde se implementan pruebas para verificar la funcionalidad y efectividad del código.

## Cómo Ejecutar el Programa

`main_new.py` se puede ejecutar de dos formas:

1. Ejecutar `python main_new.py` sin proporcionar ningún argumento ejecutará el código de manera sistemática a través de todas las partes de la PEC utilizando la clase Twitter.

2. Ejecutar `python main_new.py --exercise 1.1`, por ejemplo, resolverá y mostrará la salida para el ejercicio especificado.

## Preparación del Entorno

Es recomendable utilizar un entorno virtual para ejecutar este proyecto. Aquí están los pasos para crear uno con Anaconda:

1. Crear el entorno: `conda create --name pec python==3.9`
2. Activar el entorno: `conda activate pec`

Una vez activado el entorno, es necesario instalar el paquete `wordcloud`. Este puede ser un poco complicado de instalar, por lo que se recomienda instalarlo a través del canal conda-forge:

```conda install -c https://conda.anaconda.org/conda-forge wordcloud```

## Datos

Los datos necesarios para este proyecto deben ser colocados en la carpeta `data`. En particular, el archivo `twitter_reduce.zip` debe ser descomprimido en esta carpeta. Durante la ejecución del programa, los archivos `.csv` resultantes también se colocarán en esta carpeta.

## Pruebas

Las pruebas se pueden ejecutar desde la carpeta `tests`. Estas pruebas verifican la funcionalidad y la capacidad de resolución del código.

Por favor, haga referencia a las instrucciones de ejecución de la prueba proporcionadas para obtener más detalles.

## Contribución

Las contribuciones son bienvenidas. Por favor, haga una solicitud de extracción con sus cambios.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.