import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    "Name": ["Dreni", "Gerti", "Deon"],
    "Age": [16, 15, 16],
    "City": ["Prishtina", "Prizreni", "Ferizaj"]
})

st.dataframe(data)
