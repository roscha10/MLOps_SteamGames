![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas) ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib) ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn) ![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn) ![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi) ![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker) ![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>
  
# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>


# <h1 align=center>Steam Game Recommender 

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

**`Autor: Roberto Schaefer`**

[LinkedIn](www.linkedin.com/in/roberto-schaefer-506567264)

## Introducción

Este proyecto representa una simulación del rol de un MLOps Engineer, que engloba las responsabilidades de un Data Engineer y un Data Scientist, dentro del contexto de la plataforma internacional de videojuegos Steam. El objetivo principal de este proyecto es desarrollar un Producto Mínimo Viable (MVP) que no solo demuestre la capacidad de implementar una API en un servicio en la nube, sino que también presente la aplicación práctica de dos modelos de Machine Learning.



## Un Vistazo a la Plataforma de Videojuegos Steam


Steam, lanzada en 2003 por Valve Corporation, inicialmente como una plataforma de actualización de juegos, ha evolucionado para ser una distribuidora líder de videojuegos y contenido multimedia. Ofrece servicios de protección contra la piratería, emparejamiento de servidores, streaming de video y funciones sociales. Se utiliza tanto por desarrolladores independientes como grandes corporaciones. En 2016, Steam contaba con más de 7300 juegos y más de 142 millones de cuentas de usuarios activas. Su sistema de revisiones personalizadas ha mejorado la experiencia del usuario, destacándose como un referente en la industria de juegos de PC.


## Datasets

**user_reviews.json.gz:**
Este dataset incluye comentarios de usuarios sobre juegos en Steam. Cada revisión contiene detalles como emoticones "graciosos," fechas de publicación y edición, ID del juego, estadísticas de utilidad, y recomendaciones. Los usuarios también están identificados por su ID y URL de perfil.

**users_items.json.gz:**
En este dataset, se registran los juegos jugados por los usuarios de Steam, junto con el tiempo acumulado en cada juego. Proporciona información sobre la cantidad de juegos que ha consumido cada usuario, su ID único, URL de perfil y los juegos que han jugado en términos de ID, nombre y tiempo de juego.

**steam_games.json.gz:**
Este dataset contiene datos detallados sobre juegos, incluyendo la empresa publicadora, géneros, nombre del juego, título, URL, fecha de lanzamiento, etiquetas, URL de reseñas, especificaciones, precio y acceso temprano (True/False). Cada juego está identificado con un ID único y el nombre del desarrollador.

# Camino recorrido al MVP:

## ETL (Extract, Transform and Load)
En el proceso de transformación de datos para este proyecto, realizamos la extracción, transformación y carga (ETL) de los tres conjuntos de datos proporcionados. Esto implicó descomprimir archivos y leerlos línea por línea. Abordamos la complejidad de conjuntos de datos con estructuras anidadas, como diccionarios o listas de diccionarios en columnas, utilizando estrategias para convertir estas estructuras en columnas separadas. Además, rellenamos valores nulos en variables esenciales, eliminamos columnas con una alta cantidad de nulos y duplicados, y descartamos columnas que no eran relevantes para el proyecto. Estas acciones se llevaron a cabo considerando las restricciones de almacenamiento y para optimizar el rendimiento de la API. El uso de la biblioteca Pandas facilitó estas transformaciones, garantizando la integridad y eficiencia de los datos finales para su implementación en el proyecto.

## Detalles de ETL:
- [SteamGames_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1A_SteamGames_ETL.ipynb)
- [UserReviews_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1B_UserReviews_ETL.ipynb)
- [UserItems_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1C_UserItems_ETL.ipynb)

# Desarrollo de la API
****Endpoints* propuestos***</h4>

Se proponen 6 *endpoints* iniciales. Para cada uno de los *endpoint* se desarrollo una función en Python mediantes el uso del *FrameWork* FastAPI y librerias asociadas.
Funciones propuestas:

+ **PlayTimeGenre( genero : str )**: Se ingresa un genero y se retorna el año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

+ **UserForGenre( genero : str )**:  Se ingresa un genero y se retorne el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

+ **UsersRecommend( año : int )**: Se ingresa un año y retorna el top 3 de juegos MÁS recomendados por usuarios para el año dado.
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ **UsersNotRecommend( año : int )**: Se ingresa un año y retorna el top 3 de juegos MENOS recomendados por usuarios para el año dado.
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ **sentiment_analysis( año : int )**: Se ingresa un año (año de lanzamiento), y retona una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
  
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

+ **recomendacion_juego( id de producto )**: Se ingresa el id de producto y deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

# Implementación de la API

Las funciones propuestas se desarrollaron de la mano de **python** y **FastAPI**, testeando su funcionamiento en el entorno local mediante **uvicorn**. En el ['main.py'](https://github.com/roscha10/MLOps_SteamGames/blob/main/main.py) mencionado anteriormente se puede observar cada uno de los *endpoints* con sus respectivas rutas y el desarrollo completo de la API.

# Despliegue de la API

La API finalizada fue desplegada en la plataforma render.com para su implementación. Sin embargo, se encontraron ciertas limitaciones en el entorno de despliegue gratuito, que ofrecía solo 512MB de capacidad. Para abordar estas restricciones, se tomaron medidas específicas para optimizar el rendimiento y la eficiencia de la API.

Una de las principales adaptaciones consistió en la reducción de la carga de datos en el sistema de recomendación. Dado que el procesamiento requerido por el modelo de Machine Learning para procesar todos los datos excedía el límite de recursos establecido, se implementaron estrategias para limitar el volumen de datos procesados sin sacrificar la calidad de las recomendaciones.

Además, se enfrentaron desafíos relacionados con las bibliotecas y versiones de software disponibles en el entorno de despliegue de render.com. Se tomó la decisión de incluir únicamente las bibliotecas necesarias para el funcionamiento de la API y asegurarse de que estas estuvieran en las versiones compatibles con el entorno de despliegue.

Por otro lado, se proporcionó una interfaz gráfica mínima en la ruta inicial de la API para mostrar ejemplos visuales de las entradas de los endpoints y sus respectivas respuestas. Sin embargo, para una documentación más detallada y completa, se utilizó FastAPI para generar automáticamente la documentación esencial. Esta documentación se encuentra disponible en la ruta /docs y brinda ejemplos de consultas que los usuarios pueden ejecutar para observar las respuestas correspondientes, lo que simplifica significativamente la comprensión y el uso efectivo de la API.

En resumen, el despliegue de la API en render.com implicó superar desafíos relacionados con los recursos limitados disponibles, optimizar el procesamiento de datos, adaptar bibliotecas y versiones, y proporcionar una interfaz amigable y documentación detallada para garantizar una experiencia de usuario efectiva.

# EDA

Este proceso se centró en la observación de la distribución de variables, la identificación de patrones, la detección de posibles valores atípicos (outliers), y otros aspectos clave. El objetivo principal del EDA fue confirmar o descartar hipótesis relacionadas con las características (features) que podrían resultar relevantes para las recomendaciones.

En el transcurso del EDA, se tomó la decisión de eliminar algunos valores atípicos que podrían afectar negativamente el rendimiento del sistema de recomendación, garantizando así la calidad y precisión de las recomendaciones ofrecidas.

Para obtener más detalles sobre el proceso y los hallazgos específicos del EDA empleado en este proyecto, se encuentra disponible un cuaderno Jupyter en el siguiente enlace: [Link](JupyterNotebooks/3A_EDA.ipynb)



#RENDER

En este [link](https://mlops-steamgames.onrender.com/docs) se podrá acceder a la API y realizar consultas.
