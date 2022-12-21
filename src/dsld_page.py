import pandas as pd
import requests
import streamlit as st

from .components import download_button, fhir, get_supplements


DEFAULT_SUPPLEMENTS = [
    {"name": "Centrum Adults", "dsld_id": 256965},
    {"name": "Vitamin D", "dsld_id": 252101},
    {
        "name": "Kirkland Signature Extra Strength Glucosamine",
        "dsld_id": 207402,
    },
]


def main(use_server: bool, base_url: str):
    """_summary_"""
    dsld_response = None
    nutrition_product = {}
    supplements_df = pd.DataFrame(DEFAULT_SUPPLEMENTS)

    tab1, tab2, tab3 = st.tabs(["Inputs", "NutritionProduct", "Response"])

    with tab1:
        supplement_name = st.selectbox(
            "Select supplement?",
            supplements_df,
            0,
        )

        status_option = fhir.main()
        supplement = supplements_df[supplements_df["name"] == supplement_name]
        dsld_response = get_supplements.main(
            use_server, base_url, supplement["dsld_id"].item()
        )
        product = dsld_response
        ingredients = []
        manufacturer = []

        for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
            ingredients.append({"name": ingredient["name"]})
            print(ingredient["name"])
        for contanct in product["contacts"]:
            manufacturer.append({"name": contanct["name"]})
            print(contanct["name"])

        nutrition_product = {
            "resourceType": "NutritionProduct",
            "status": st.session_state.status_option,
            "manufacturer": manufacturer,
            "ingredient": ingredients,
        }

        download_button.main(nutrition_product)
        st.session_state.status_option = status_option

    with tab2:
        st.json(nutrition_product)
    with tab3:
        st.json(dsld_response if dsld_response else {})
