from fastapi import FastAPI
import pandas as pd
from fastapi.responses import JSONResponse



app = FastAPI()

#DATASETS

df_most_played_year = pd.read_csv("./Data_API/df_most_played_year.csv")
df_maxuser_genre_cleaned = pd.read_csv('./Data_API/df_maxuser_genre_cleaned.csv')
df_top_positive_games_by_year = pd.read_csv('./Data_API/df_top_positive_games_by_year.csv')
df_top_negative_games_by_year = pd.read_csv('./Data_API/df_top_negative_games_by_year.csv')
df_sentiment_counts = pd.read_csv('./Data_API/df_sentiment_counts.csv')

#INICIO DE LA API

#1
@app.get("/most_played_genre/{genre}")
async def PlayTimeGenre(genre):
    """
    Retornar el género mas jugado por año.
    """
    # Filtra el DataFrame por el género especificado
    genre_data = df_most_played_year[df_most_played_year['genres'] == genre]
    
    if genre_data.empty:
        return f'El género {genre} no se encuentra en el conjunto de datos.'
    
    # Obtiene el año directamente
    max_playtime_year = genre_data.iloc[0]['release_year']
    
    # Devuelve el resultado en el formato deseado
    result = f"Año de lanzamiento con más horas jugadas para el género {genre}: {max_playtime_year}"
    
    return result

#2
@app.get("/most_hours_played_genre/{genre}")
def UserForGenre(genre):

    # Filtra el DataFrame por el género especificado
    genre_data = df_maxuser_genre_cleaned[df_maxuser_genre_cleaned['genres'] == genre]
    
    if genre_data.empty:
        return f'El género {genre} no se encuentra en el conjunto de datos.'
    
    # Encuentra el usuario con más horas jugadas para el género
    max_playtime_user = genre_data['user_id'].values[0]
    
    # Crea una lista de acumulación de horas jugadas por año
    playtime_by_year = []
    for column in genre_data.columns[3:]:  # Ignora las primeras tres columnas
        year = int(column)
        playtime = round(genre_data[column].sum() , 2)  # Convierte minutos a horas y redondea a 2 decimales
        if playtime > 0:
            playtime_by_year.append({'Año': year, 'Horas': playtime})
    
    # Devuelve el resultado en el formato deseado
    result = {
        f"Usuario con más horas jugadas para Género {genre}": max_playtime_user,
        "Horas jugadas": playtime_by_year
    }

    return result

#3
@app.get("/top_3_MOST_recommended_games/{year}")
def UsersRecommend(year):
    # Filtrar el DataFrame por el año dado
    filtered_df = df_top_positive_games_by_year[df_top_positive_games_by_year['reviews_year'] == year]
    
    # Verificar si se encontraron revisiones para el año dado
    if filtered_df.empty:
        return "Año ingresado inválido o sin revisiones."
    
    top_games_list = [
        {"Puesto 1": filtered_df.iloc[0]['Rank 1']},
        {"Puesto 2": filtered_df.iloc[0]['Rank 2']},
        {"Puesto 3": filtered_df.iloc[0]['Rank 3']}
    ]
    return top_games_list

#4
@app.get("/top_3_LEAST_recommended_games/{year}")
def UsersNotRecommend(year):
    # Filtrar el DataFrame por el año dado
    filtered_df = df_top_negative_games_by_year[df_top_negative_games_by_year['reviews_year'] == year]
    
    # Verificar si se encontraron revisiones para el año dado
    if filtered_df.empty:
        return "Año ingresado inválido o sin revisiones."
    
    top_games_list = [
        {"Puesto 1": filtered_df.iloc[0]['Rank 1']},
        {"Puesto 2": filtered_df.iloc[0]['Rank 2']},
        {"Puesto 3": filtered_df.iloc[0]['Rank 3']}
    ]
    return top_games_list


#5
@app.get("/reviews_sentiment_analysis/{year}")
def sentiment_analysis(year: int):
    """
    Retornar el número de reviews negativas, neutrales y positivas para un año dado.
    """
    # Crear un dataframe donde las filas son años y las columnas análisis de sentimiento.
    df_sentiment_counts = pd.read_csv('./Data_API/df_sentiment_counts.csv')

    # Encontrar los valores de sentimiento para el año pasado como parámetro.
    negativo = df_sentiment_counts.loc[df_sentiment_counts.release_year == year, "total_negativos"].item()
    neutral = df_sentiment_counts.loc[df_sentiment_counts.release_year == year, "total_neutrales"].item()
    positivo = df_sentiment_counts.loc[df_sentiment_counts.release_year == year, "total_positivos"].item()

    return {"Negative" : negativo, "Neutral" : neutral, "Positive" : positivo}


#6
df_item_similarity = pd.read_parquet('./Data_API/df_item_similarity.parquet')
num_recomendaciones=5

@app.get("/top5_recommended_games_name/{id_juego}")
def game_recommendation(id_juego: str):
    if id_juego in df_item_similarity:
        juego_similaridades = df_item_similarity[id_juego]
        juegos_similares = juego_similaridades.sort_values(ascending=False)
        juegos_similares = juegos_similares[1:num_recomendaciones + 1]
        recommendations = [{"Recomendación": i, "Juego": juego} for i, (juego, similitud) in enumerate(juegos_similares.items(), 1)]
        return JSONResponse(content={"Juegos similares a": id_juego, "Recomendaciones": recommendations})
    else:
        return JSONResponse(content={"Mensaje": "El juego ingresado no está en la base de datos."})