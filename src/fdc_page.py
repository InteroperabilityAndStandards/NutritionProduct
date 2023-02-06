import pandas as pd
import streamlit as st

from .components import download_button, get_foods, status_select_box
from .functions import parse_food

DEFAULT_FOODS = [
    {"name": "Fugi Apple", "fdc_id": 1750340},
    {"name": "Banana", "fdc_id": 1105314},
    {"name": "Skippy Peanut Butter", "fdc_id": 1759570},
    {"name": "ENSURE, HIGH PROTEIN POWDER, VANILLA, VANILLA", "fdc_id": 1838332},
]


def main(use_server: bool, base_url: str):
    """_summary_"""
    response = {}
    nutrition_product = {}
    food_df = pd.DataFrame(DEFAULT_FOODS)

    with st.sidebar.form("dsld_form"):
        food_name = st.selectbox(
            "Select Food?",
            food_df,
            0,
        )
        status_option = status_select_box.main()

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            food = food_df[food_df["name"] == food_name]
            response = get_foods.main(use_server, base_url, food["fdc_id"].item())
            nutrition_product = None
            if use_server is True:
                nutrition_product = response
            else:
                nutrition_product = parse_food.main(response, status_option)

            st.session_state.nutrition_product = nutrition_product

    download_button.main()

    tab1, tab2 = st.tabs(["NutritionProduct", "FDC Response"])

    with tab1:
        st.json(nutrition_product)

    with tab2:
        st.json(response)
