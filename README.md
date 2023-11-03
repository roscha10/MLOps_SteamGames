![Github](https://camo.githubusercontent.com/544426317a6c6226b7f6b3367232378ea367aa5001a41da4f302a77f9959909f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4769744875622d3333333333333f7374796c653d666c6174266c6f676f3d676974687562) ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas) ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib) ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn) ![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn) ![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)  ![jupyter](https://camo.githubusercontent.com/520feca36c380051805100a73d5b396d4a27490fb5dacbc9e87c03e2ca4fd7f4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4a7570797465722d3333333333333f7374796c653d666c6174266c6f676f3d6a757079746572) ![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render) ![Visual](https://camo.githubusercontent.com/194ae9b0be9bfd4caedab16de320d3987f4c144112461590a206262d21eb769b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d56697375616c25323053747564696f253230436f64652d3333333333333f7374796c653d666c6174266c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d303037414343)
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


## Datasets originales

**user_reviews.json.gz:**
Este dataset incluye comentarios de usuarios sobre juegos en Steam. Cada revisión contiene detalles como emoticones "graciosos," fechas de publicación y edición, ID del juego, estadísticas de utilidad, y recomendaciones. Los usuarios también están identificados por su ID y URL de perfil.

**users_items.json.gz:**
En este dataset, se registran los juegos jugados por los usuarios de Steam, junto con el tiempo acumulado en cada juego. Proporciona información sobre la cantidad de juegos que ha consumido cada usuario, su ID único, URL de perfil y los juegos que han jugado en términos de ID, nombre y tiempo de juego.

**steam_games.json.gz:**
Este dataset contiene datos detallados sobre juegos, incluyendo la empresa publicadora, géneros, nombre del juego, título, URL, fecha de lanzamiento, etiquetas, URL de reseñas, especificaciones, precio y acceso temprano (True/False). Cada juego está identificado con un ID único y el nombre del desarrollador.

Datos Crudos: [Dataset_Original](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

# Camino recorrido al MVP:

## ETL (Extract, Transform and Load)
En el proceso de transformación de datos para este proyecto, realizamos la extracción, transformación y carga (ETL) de los tres conjuntos de datos proporcionados. Esto implicó descomprimir archivos y leerlos línea por línea. Abordamos la complejidad de conjuntos de datos con estructuras anidadas, como diccionarios o listas de diccionarios en columnas, utilizando estrategias para convertir estas estructuras en columnas separadas. Además, rellenamos valores nulos en variables esenciales, eliminamos columnas con una alta cantidad de nulos y duplicados, y descartamos columnas que no eran relevantes para el proyecto. Estas acciones se llevaron a cabo considerando las restricciones de almacenamiento y para optimizar el rendimiento de la API. El uso de la biblioteca Pandas facilitó estas transformaciones, garantizando la integridad y eficiencia de los datos finales para su implementación en el proyecto.

## Detalles de ETL:
- [SteamGames_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1A_SteamGames_ETL.ipynb)
- [UserReviews_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1B_UserReviews_ETL.ipynb)
- [UserItems_ETL](https://github.com/roscha10/MLOps_SteamGames/blob/main/JupyterNotebooks/1C_UserItems_ETL.ipynb)

## Análisis de sentimiento

En el contexto de este proyecto, uno de los requisitos clave fue aplicar un análisis de sentimiento a las revisiones de los usuarios. Para abordar este desafío, inicialmente utilizamos la biblioteca TextBlob para realizar este análisis. Sin embargo, después de una exhaustiva revisión de los resultados, identificamos algunas inconsistencias en la calificación de los sentimientos en los comentarios de los usuarios.

Como respuesta a esta situación, realizamos una investigación adicional y exploramos otras bibliotecas. Fue entonces cuando descubrimos la biblioteca NLTK (Natural Language Toolkit) y su módulo SentimentIntensityAnalyzer. Este módulo demostró una mayor consistencia en la calificación de sentimientos, lo que lo convirtió en la elección principal para este proyecto.

En consecuencia, creamos una nueva columna llamada 'sentiment_analysis', que reemplazó la columna original que contenía las revisiones de los usuarios. Esta nueva columna asigna una clasificación numérica a los comentarios siguiendo la siguiente escala:

- 0 si el sentimiento es negativo.
- 1 si el sentimiento es neutral o si no hay una revisión disponible.
- 2 si el sentimiento es positivo.

El propósito de esta etapa de ingeniería de características es proporcionar una representación numérica de los comentarios de los usuarios para categorizarlos como expresiones de sentimientos negativos, neutrales o positivos.

Para obtener detalles más específicos sobre el desarrollo de esta etapa de análisis de sentimiento, se encuentra disponible una Jupyter Notebook detallada en el siguiente enlace: [Link](JupyterNotebooks/1D_Sentiment_Analysis.ipynb).

## Datasets procesados

Con el propósito de optimizar la eficiencia en la respuesta de las consultas de la API y en consideración de las limitaciones de almacenamiento impuestas por el servicio en la nube para la implementación de la API, llevamos a cabo un proceso clave de gestión de datos. Como parte de este proceso, creamos dataframes auxiliares específicos para cada una de las funciones requeridas en el sistema de recomendación.

Estos dataframes auxiliares desempeñaron un papel fundamental al permitir una respuesta más ágil y eficiente a las consultas de los usuarios. Además, para abordar las restricciones de almacenamiento, optamos por almacenar estos dataframes en dos formatos estratégicos: "parquet" y "csv".

Para obtener información detallada sobre el desarrollo de los conjuntos de datos auxiliares, te invito a consultar la Jupyter Notebook correspondiente en el siguiente enlace: [Link](JupyterNotebooks/2A_Datasets_API.ipynb). Esta notebook proporcionará información adicional sobre cómo se crearon y gestionaron los dataframes auxiliares.

## EDA

Este proceso se centró en la observación de la distribución de variables, la identificación de patrones, la detección de posibles valores atípicos (outliers), y otros aspectos clave. El objetivo principal del EDA fue confirmar o descartar hipótesis relacionadas con las características (features) que podrían resultar relevantes para las recomendaciones.

En el transcurso del EDA, se tomó la decisión de eliminar algunos valores atípicos que podrían afectar negativamente el rendimiento del sistema de recomendación, garantizando así la calidad y precisión de las recomendaciones ofrecidas.

Para obtener más detalles sobre el proceso y los hallazgos específicos del EDA empleado en este proyecto, se encuentra disponible un cuaderno Jupyter en el siguiente enlace: [Link](JupyterNotebooks/3A_EDA.ipynb)


## Desarrollo de la API
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

## Implementación de la API

Las funciones propuestas se desarrollaron de la mano de **python** y **FastAPI**, testeando su funcionamiento en el entorno local mediante **uvicorn**. En el ['main.py'](https://github.com/roscha10/MLOps_SteamGames/blob/main/main.py) mencionado anteriormente se puede observar cada uno de los *endpoints* con sus respectivas rutas y el desarrollo completo de la API.

## Despliegue de la API

La API finalizada fue desplegada en la plataforma render.com para su implementación. Sin embargo, se encontraron ciertas limitaciones en el entorno de despliegue gratuito, que ofrecía solo 512MB de capacidad. Para abordar estas restricciones, se tomaron medidas específicas para optimizar el rendimiento y la eficiencia de la API.

Una de las principales adaptaciones consistió en la reducción de la carga de datos en el sistema de recomendación. Dado que el procesamiento requerido por el modelo de Machine Learning para procesar todos los datos excedía el límite de recursos establecido, se implementaron estrategias para limitar el volumen de datos procesados sin sacrificar la calidad de las recomendaciones.

Además, se enfrentaron desafíos relacionados con las bibliotecas y versiones de software disponibles en el entorno de despliegue de render.com. Se tomó la decisión de incluir únicamente las bibliotecas necesarias para el funcionamiento de la API y asegurarse de que estas estuvieran en las versiones compatibles con el entorno de despliegue.

Por otro lado, se proporcionó una interfaz gráfica mínima en la ruta inicial de la API para mostrar ejemplos visuales de las entradas de los endpoints y sus respectivas respuestas. Sin embargo, para una documentación más detallada y completa, se utilizó FastAPI para generar automáticamente la documentación esencial. Esta documentación se encuentra disponible en la ruta /docs y brinda ejemplos de consultas que los usuarios pueden ejecutar para observar las respuestas correspondientes, lo que simplifica significativamente la comprensión y el uso efectivo de la API.

En resumen, el despliegue de la API en render.com implicó superar desafíos relacionados con los recursos limitados disponibles, optimizar el procesamiento de datos, adaptar bibliotecas y versiones, y proporcionar una interfaz amigable y documentación detallada para garantizar una experiencia de usuario efectiva.

## Desarrollo del sistema de recomendación

El proceso de nuestro sistema de recomendacion comienza cuando un usuario ingresa el nombre de un videojuego. El sistema responde proporcionando una lista de los cinco videojuegos que considera más similares al juego ingresado. Para lograr esto, empleamos una matriz de similitud de coseno.

### Matriz de Similitud de Coseno:

La matriz de similitud de coseno es una herramienta fundamental en nuestro proyecto de recomendación de videojuegos. Esta matriz se utiliza para calcular las similitudes entre todos los pares de videojuegos en nuestro conjunto de datos. Su funcionamiento se basa en la medida de la similitud angular entre los vectores que representan los videojuegos en un espacio multidimensional. Una similitud más alta indica que los juegos son más parecidos en términos de sus atributos y características.

### Preparación de datos:

En nuestro enfoque para el desarrollo del sistema de recomendación, utilizamos un enfoque detallado para calcular un puntaje de recomendación llamado 'Recommendation'. Este puntaje se sitúa en una escala del 1 al 5 y se basa en dos factores clave: el análisis de sentimiento de las reseñas de los juegos y las recomendaciones de los usuarios. Este enfoque integral nos permite brindar recomendaciones de juegos altamente personalizadas y precisas que se ajustan a las preferencias y experiencias de cada usuario, enriqueciendo su interacción con nuestra plataforma.

### Obtención de los 5 juegos más similares:

Una vez que el usuario ingresa el nombre de un juego como consulta, el sistema mapea ese título a un índice en la matriz de similitud de coseno. Luego, utilizando estos índices, el sistema identifica los cinco juegos más similares al juego de consulta. Estos juegos se seleccionan en función de su similitud con el juego ingresado, y posteriormente se devuelven los títulos de estos juegos similares al usuario. Este proceso permite a los usuarios descubrir juegos relacionados y afines a sus preferencias, mejorando así su experiencia de juego y exploración en nuestra plataforma.

Para información más detallada y uso del modelo de manera externa a la API vea:[Link](JupyterNotebooks/4A_recommendation_model.ipynb)


# Link de Interés

En este [link](https://mlops-steamgames.onrender.com/docs) se podrá acceder a la API y realizar consultas.
