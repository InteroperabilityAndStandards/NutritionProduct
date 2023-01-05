import pandas as pd
import streamlit as st

from .components import download_button, get_supplements, status_select_box
from .functions import parse_supplement

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
        status_option = status_select_box.main()

        print(st.session_state.nutrition_product)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            supplement = supplements_df[supplements_df["name"] == supplement_name]
            response = get_supplements.main(
                use_server, base_url, supplement["dsld_id"].item()
            )
            product = response

            nutrition_product = parse_supplement.main(product, status_option)

            st.session_state.nutrition_product = nutrition_product

    download_button.main()

    tab1, tab2 = st.tabs(["NutritionProduct", "DSLD Response"])

    with tab1:
        st.json(nutrition_product)
    with tab2:
        st.json(response if response else {})
