import streamlit as st
import pandas as pd
import plotly.express as px

from module3.sets import unique_list

books_df = pd.read_csv("../module19/bestsellers_with_categories_2022_03_27.csv")

st.title("Bestselling Books")
st.write("This app analyzes the amazon top selling books")

st.subheader("Summary Statistsic")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1 , col2 , col3 , col4 = st.columns(4)
col1.metric("total bools", total_books)
col2.metric("unique titles", total_books)
col3.metric("average ", total_books)
col4.metric("average pricw", total_books)

st.subheader("dataset preview")
st.write(books_df.head())


with col1:
    st.subheader("top 10")
    tpo_tti;es = books_df['name'].value