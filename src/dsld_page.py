import pandas as pd
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
    response = {}
    nutrition_product = {}
    supplements_df = pd.DataFrame(DEFAULT_SUPPLEMENTS)

    with st.sidebar.form("dsld_form"):
        supplement_name = st.selectbox(
            "Select supplement",
            supplements_df,
            0,
        )
        status_option = fhir.main()

        print(st.session_state.nutrition_product)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            supplement = supplements_df[supplements_df["name"] == supplement_name]
            response = get_supplements.main(
                use_server, base_url, supplement["dsld_id"].item()
            )
            product = response
            ingredients = []
            manufacturer = []

            for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
                ingredients.append({"name": ingredient["name"]})
            for contanct in product["contacts"]:
                manufacturer.append({"active": True, "name": contanct["name"]})

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
        st.json(response if response else {})
