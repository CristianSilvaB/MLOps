from fastapi import FastAPI
import pandas as pd

from src.Api import funciones
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pickle

# Cargar los datos
user_reviews = pd.read_pickle("./Data/user_reviews.pkl")
matrix_utility = pickle.load(open("./Data/matrix_utility.pkl", "rb"))
model_knn = pickle.load(open("./Data/model_knn.pkl", "rb"))
steam_games_model= pickle.load(open("./Data/steam_games_model.pkl", "rb"))
users_items_model = pickle.load(open("./Data/users_items_model.pkl", "rb"))

app = FastAPI()

@app.get("/developer/{desarrollador}")
async def get_developer_info(desarrollador: str):
    result = funciones.developer_info(desarrollador, steam_games_model)
    return result

@app.get("/user-data/{user_id}")
async def get_user_data(user_id: str):
    result = funciones.user_data(user_id, user_reviews, users_items_model)
    return result

@app.get("/user-for-genre/{genre}")
async def get_user_for_genre(genre: str):
    result = funciones.user_for_genre(genre, steam_games_model, users_items_model)
    return result

@app.get("/best-developer-year/{year}")
async def get_best_developer_year(year: int):
    result = funciones.best_developer_year(year, steam_games_model, user_reviews)
    return result

@app.get("/developer-reviews-analysis/{desarrolladora}")
async def get_developer_reviews_analysis(desarrolladora: str):
    result = funciones.developer_reviews_analysis(desarrolladora, steam_games_model, user_reviews)
    return result

@app.get("/recomendacion-juego/{item_id}")
async def get_recomendacion_juego(item_id: str):
    result = funciones.recomendacion_juego(item_id, steam_games_model, matrix_utility, model_knn, k=5)
    return result
