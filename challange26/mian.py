# ==========================================
# ONLINE RECIPE BOOK PROJECT (ALL-IN-ONE)
# FastAPI + SQLite
# ==========================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

# ==========================================
# DATABASE SETUP
# ==========================================

conn = sqlite3.connect("recipes.db", check_same_thread=False)
cursor = conn.cursor()

# CREATE TABLES

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    ingredients TEXT,
    instructions TEXT,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)
""")

conn.commit()



app = FastAPI(title="Online Recipe Book")



class Category(BaseModel):
    name: str


class Recipe(BaseModel):
    title: str
    ingredients: str
    instructions: str
    category_id: int




@app.get("/")
def home():
    return {"message": "Recipe Book API Running Successfully"}





@app.post("/categories/")
def add_category(category: Category):

    try:
        cursor.execute(
            "INSERT INTO categories(name) VALUES(?)",
            (category.name,)
        )

        conn.commit()

        return {
            "message": "Category Added Successfully"
        }

    except:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )




@app.get("/categories/")
def get_categories():

    cursor.execute("SELECT * FROM categories")

    categories = cursor.fetchall()

    result = []

    for category in categories:
        result.append({
            "id": category[0],
            "name": category[1]
        })

    return result




@app.delete("/categories/{category_id}")
def delete_category(category_id: int):

    cursor.execute(
        "DELETE FROM categories WHERE id=?",
        (category_id,)
    )

    conn.commit()

    return {
        "message": "Category Deleted"
    }