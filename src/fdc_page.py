import pandas as pd
import streamlit as st

from .components import download_button, fhir, get_foods

DEFAULT_FOODS = [
    {"name": "Apple", "fdc_id": 1750340},
    {"name": "Banana", "fdc_id": 1105314},
    {"name": "Skippy Peanut Butter", "fdc_id": 1759570},
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
        status_option = fhir.main()

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            food = food_df[food_df["name"] == food_name]
            response = get_foods.main(use_server, base_url, food["fdc_id"].item())
            product = response
            ingredients = []
            manufacturer = []

            # for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
            #     ingredients.append({"name": ingredient["name"]})
            # for contanct in product["contacts"]:
            #     manufacturer.append({"name": contanct["name"]})

            nutrition_product = {
                "resourceType": "NutritionProduct",
                "status": status_option,
                "manufacturer": manufacturer,
                "ingredient": ingredients,
            }
            st.session_state.nutrition_product = nutrition_product

    download_button.main()

    tab1, tab2 = st.tabs(["NutritionProduct", "Response"])

    with tab1:
        st.json(nutrition_product)

    with tab2:
        st.json(response)
