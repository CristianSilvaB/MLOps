# <h1 align=center> *PROYECTO INDIVIDUAL Nº1* </h1>
# <h1 align=center>*Machine Learning Operations (MLOps)*</h1>
# <h2 align=left>*Realizado por: Cristian Silva*</h2>

<hr>  


Tomando el papel de un científico de datos para Steam, una multinacional de videojuegos, se busca desarrollar un producto mínimo viable. A partir del conjunto de dataset brindados se buscó crear un sistema de recomendación de videojuegos para los usuarios mediante Machine Learning. Sin embargo, los datos presentan una madurez deficiente. Por lo tanto, es necesario realizar además un ETL (Extracción, Transformación y Carga de los datos), un EDA (Análisis Exploratorio de Datos), y finalmente, la creación del modelo de Machine Learning.

## Tecnologías utilizadas

Para el desarrollo de este proyecto se utilizaron tecnologías como: Python, FastAPI, Pandas, Scikit-learn, TextBlob, NLTK y  Render.

## Metodología

### ETL

Se llevó a cabo un proceso de ETL (Extracción, Transformación y Carga) en tres etapas principales:

1. *Extracción*: En esta etapa, se extrajeron y exploraron los datos de las fuentes proporcionadas en el [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

2. *Transformación*: Esta etapa implicó una serie de pasos para limpiar y preparar los datos para el análisis, entre ellas:
    - *Identificación y tratamiento de valores nulos*: Se identificaron los valores nulos y se tomaron decisiones sobre cómo manejarlos, ya sea eliminándolos o reemplazándolos con valores significativos.
    - *Revisión de registros duplicados*: Se revisaron los conjuntos de datos en busca de registros duplicados y se tomaron medidas para tratarlos.
    - *Eliminación de datos y columnas innecesarias*: Se eliminaron los datos y las columnas que no eran relevantes para el análisis.
    - *Desanidación de columnas*: Algunas columnas que contenían datos anidados fueron desanidadas para facilitar el análisis.
    - *Filtrado de registros*: Se filtraron los registros según criterios específicos para centrarse en los datos relevantes.
    - *Conversión de tipos de datos*: Se realizaron conversiones de tipos de datos cuando fue necesario, como la conversión a enteros, la transformación de fechas y el ajuste de precios.
    - *Creación de nuevas columnas*: Se crearon nuevas columnas a partir de los datos existentes para facilitar el análisis.
    - *Explode de los géneros de videojuegos*: Se realizó un explode de los géneros de videojuegos para facilitar su análisis.
    - *Preservación de columnas con ID*: Se preservaron las columnas con ID para mantener la integridad de los datos.
    - *Normalización de datos*: Se normalizaron algunos datos para mantener la consistencia en los conjuntos de datos.

3. *Carga*: Finalmente, los datos limpios y normalizados se almacenaron en un formato pickle para su uso posterior en el análisis y modelado.


### Análisis Exploratorio de Datos (EDA)

Se realizó un Análisis Exploratorio de Datos (EDA) con el objetivo de comprender las características de los datos. Este incluye:

1. *Exploración Inicial*: Se realizó un chequeo y análisis de valores nulos, duplicados, faltantes; así mismo, se analizaron los tipos de datos y las estadísticas descriptivas para cada dataset.

2. *Análisis Gráfico y Correlacional*: Se llevó a cabo un análisis bivariado y multivariado que incluye:
    - Distribución de juegos por género y desarrollador.
    - Tendencias de lanzamiento a lo largo del tiempo.
    - Análisis de precios: distribución de precios y relación entre precio y género.
    - Distribución del análisis de sentimientos y su relación con la recomendación.
    - Análisis de tendencias temporales en las reseñas y sentimientos a lo largo de los años.
    - Análisis de palabras frecuentes en las reseñas utilizando técnicas de Procesamiento del Lenguaje Natural (NLP).
    - Distribución del tiempo de juego.
    - Relación entre tiempo de juego y género de juegos.
    - Usuarios con mayor tiempo de juego y su distribución entre diferentes juegos.

3. *Resumen Ejecutivo*: Se presentan los hallazgos más importantes, que incluyen:
    - Estadísticas Descriptivas.
    - Detección de Outliers.
    - Palabras más frecuentes en las reseñas.
    - Análisis por Categorías.

### Feature Engineering

A partir de las reseñas obtenidas del conjunto de datos user_reviews, se realizó un análisis de sentimientos utilizando Procesamiento del Lenguaje Natural (NLP). Como resultado de este análisis, se creó una nueva columna que representa el sentimiento de cada reseña. Esta columna toma los siguientes valores:
- '0' si el sentimiento es negativo
- '1' si el sentimiento es neutral
- '2' si el sentimiento es positivo

El objetivo de esta transformación es facilitar el análisis de datos y el aprendizaje automático, permitiendo que el modelo utilice esta información de sentimiento de manera efectiva.

### API

Además, se lleva a cabo la creación de las funciones de la API RESTful creada utilizando FastAPI, las cuales al ser consultadas permiten un facil acceso a los datos requeridos. Estas son: 


+ *developer*:  Devuelve la cantidad de juegos y el porcentaje de juegos gratuitos por año, agrupados por desarrollador. 

+ *userdata*: Proporciona la cantidad total de dinero gastado por el usuario, el porcentaje de juegos recomendados según las reseñas y la cantidad de juegos.

+ *UserForGenre*: Devuelve el usuario con más horas jugadas en un género específico, junto con una lista de las horas jugadas acumuladas por año.

+ *best_developer_year*: Muestra los tres principales desarrolladores con la mayor cantidad de juegos recomendados por los usuarios en un año específico.

+ *developer_reviews_analysis*: Para un desarrollador específico, devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de reseñas de usuarios categorizadas como positivas o negativas.


### Modelo de aprendizaje automático

El sistema de recomendación implementado es de tipo ítem-ítem. Cuando se introduce el ID de un juego, el sistema retorna una lista de 5 juegos que similares. El método empleado es el K-NN (K-nearest neighbors) en combinación con filtrado colaborativo. En la primera etapa, los datos se preprocesan y se desarrolla una matriz dispersa. Posteriormente, facilitando la identificación de patrones de juego, el modelo se entrena utilizando una métrica de similitud del coseno y se eligen los 20 juegos más parecidos (vecinos más cercanos). Este procedimiento proporciona un equilibrio entre precisión y eficiencia. Las recomendaciones generadas se fundamentan en patrones de juego similares, lo que enriquece la experiencia del usuario en Steam, representando una mejora en la personalización de la experiencia de juego.

### Deployment

Para el deploy de la API se utilizó [Render](https://render.com/docs/free#free-web-services) conectado a este repositorio. El link para acceder a la API es el siguiente: https://mlops-4yyh.onrender.com/docs

### Video 

Se realizó un video de presentación en el cual se muestra el correcto funcionamiento de la API. En este se muestran distintas consultas a los endpoints de la API y el funcionamiento del modelo de Machine Learning. Se encuentra en este [Link](https://render.com/docs/free#free-web-services)