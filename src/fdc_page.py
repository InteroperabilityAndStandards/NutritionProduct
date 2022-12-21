import pandas as pd
import requests
import streamlit as st
from .components import fhir, get_foods

DEFAULT_FOODS = [
    {"name": "Apple", "fdc_id": 1750340},
    {"name": "Banana", "fdc_id": 1105314},
    {"name": "Skippy Peanut Butter", "fdc_id": 1759570},
]


def main(use_server: bool, base_url: str):
    """_summary_"""
    response = None
    nutrition_product = None
    foods_df = pd.DataFrame(DEFAULT_FOODS)

    food_name = st.selectbox(
        "Select Food?",
        foods_df,
        0,
    )

    status_option = fhir.main()

    food = foods_df[foods_df["name"] == food_name]
    response = get_foods.main(use_server, base_url, food["fdc_id"].item())
    tab1, tab2 = st.tabs(["NutritionProduct", "Response"])

    with tab1:
        st.json(response)

    with tab2:
        st.json(response)
