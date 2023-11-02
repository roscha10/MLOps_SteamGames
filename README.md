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
- [SteamGames_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/A1_SteamGames_ETL.ipynb)
- [UserReviews_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/A2_UserReviews_ETL.ipynb)
- [UserItems_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/A3_UserItems_ETL.ipynb)

# Despliegue de la API
En este [link](https://mlops-steamgames.onrender.com/docs) se podrá acceder a la API y realizar consultas.
