
import streamlit as st
import pandas as pd


recipes = [
    {
        "id": 1,
        "title": "Pasta",
        "description": "Creamy pasta recipe",
        "category": "Italian"
    },
    {
        "id": 2,
        "title": "Burger",
        "description": "Cheese burger recipe",
        "category": "Fast Food"
    }
]

categories = ["Italian", "Fast Food", "Dessert"]



def get_recipes():
    return pd.DataFrame(recipes)


def get_categories():
    return categories


def create_recipe(title, description, category):
    new_recipe = {
        "id": len(recipes) + 1,
        "title": title,
        "description": description,
        "category": category
    }
    recipes.append(new_recipe)
    st.success("Recipe added succsessfully!")

-
def update_recipe(recipe_id, title, description, category):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            recipe["title"] = title
            recipe["description"] = description
            recipe["category"] = category
            st.success("Recipe updated successfully!")
            break


def delete_recipe(recipe_id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe["id"] != recipe_id]
    st.success("Recipe deleted successfully!")


def create_category(category_name):
    categories.append(category_name)
    st.success("Category added successfully!")


def update_category(old_name, new_name):
    index = categories.index(old_name)
    categories[index] = new_name
    st.success("Category updated successfully!")


def delete_category(category_name):
    categories.remove(category_name)
    st.success("Category deleted successfully!")



st.title("Recipe Management System")


menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Manage Recipes", "Manage Categories"]
)


if menu == "Dashboard":

    st.header("Dashboard")

    st.subheader("Recipes")
    st.dataframe(get_recipes())

    st.subheader("Categories")
    st.dataframe(pd.DataFrame(categories, columns=["Category"]))


elif menu == "Manage Recipes":

    st.header("Manage Recipes")

    # Add Recipe
    st.subheader("Add New Recipe")

    title = st.text_input("Recipe Title")
    description = st.text_area("Recipe Description")
    category = st.selectbox("Category", get_categories())

    if st.button("Add Recipe"):
        create_recipe(title, description, category)

    st.divider()

    # Update/Delete Recipe
    st.subheader("Edit or Delete Recipe")

    recipe_df = get_recipes()

    if not recipe_df.empty:

        selected_recipe_title = st.selectbox(
            "Select Recipe",
            recipe_df["title"]
        )

        selected_recipe = next(
            recipe for recipe in recipes
            if recipe["title"] == selected_recipe_title
        )

        updated_title = st.text_input(
            "Update Title",
            value=selected_recipe["title"]
        )

        updated_description = st.text_area(
            "Update Description",
            value=selected_recipe["description"]
        )

        updated_category = st.selectbox(
            "Update Category",
            get_categories(),
            index=get_categories().index(selected_recipe["category"])
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Update Recipe"):
                update_recipe(
                    selected_recipe["id"],
                    updated_title,
                    updated_description,
                    updated_category
                )

        with col2:
            if st.button("Delete Recipe"):
                delete_recipe(selected_recipe["id"])


elif menu == "Manage Categories":

    st.header("Manage Categories")

    # Add Category
    st.subheader("Add New Category")

    category_name = st.text_input("Category Name")

    if st.button("Add Category"):
        create_category(category_name)

    st.divider()


    st.subheader("Edit or Delete Category")

    if categories:

        selected_category = st.selectbox(
            "Select Category",
            categories
        )

        updated_category_name = st.text_input(
            "Update Category Name",
            value=selected_category
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Update Category"):
                update_category(
                    selected_category,
                    updated_category_name
                )

        with col2:
            if st.button("Delete Category"):
                delete_category(selected_category)