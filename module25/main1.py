import database
import models
from models import Movie, MovieCreate
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"messeage": "Welcome to the movies CRUD API"}

@app.post(path: "/movies/", response_model=Movie) new *
def create_movie(movie: MovieCreate):
    movie_id =database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get(path: "/movies/" , response_model=Movie) new *
def read_movie(movie_id , int):
    movie = database.read_movies(movie_id)
    if movie is None:
        raise HTTPException(status_code=404 , detail="Movie Not found")
    return movie

