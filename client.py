""" 
https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
"""

import numpy as np
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

import config

load_dotenv()

st.set_page_config(page_title="NutrientProduct", page_icon=":pill:")

base_url = "http://localhost:8000"

FDC = "Food Data Central"
DSLD = "Dietary Supplement Label Database"


col1, col2 = st.sidebar.columns(2)
with col1:
    st.write("[NutritionProduct](https://build.fhir.org/nutritionproduct.html)")
with col2:
    use_server = st.checkbox("Use Server?")


dashboard_option = st.sidebar.selectbox(
    "Select Dashboard?",
    (DSLD, FDC),
    0,
)


st.session_state.status_option = "active"

st.header(dashboard_option)


### Food Data Central
if dashboard_option == FDC:
    nutrition_product = {}
    foods_df = pd.DataFrame(config.DEFAULT_FOODS)

    food_option = st.selectbox(
        "Select Food?",
        foods_df,
        0,
    )

    food = foods_df[foods_df["name"] == food_option]
    response = None
    if use_server:
        response = requests.get(f"{base_url}/food/{food['fdc_id'].item()}", timeout=5)
    else:
        response = requests.get(
            f"https://api.nal.usda.gov/fdc/v1/food/{food['fdc_id'].item()}?api_key=DEMO_KEY",
            timeout=10,
        )
    tab1, tab2 = st.tabs(["NutritionProduct", "Response"])

    with tab1:
        st.json(response.json())

    with tab2:
        st.json(response.json())

### Dietary Supplement Label Database
if dashboard_option == DSLD:
    nutrition_product = {}
    supplements_df = pd.DataFrame(config.DEFAULT_SUPPLEMENTS)

    supplement_option = st.sidebar.selectbox(
        "Select supplement?",
        supplements_df,
        0,
    )

    supplement = supplements_df[supplements_df["name"] == supplement_option]
    response = None
    if use_server:
        response = requests.get(
            f"{base_url}/supplement/{supplement['dsld_id'].item()}", timeout=5
        )
    else:
        response = requests.get(
            f"https://api.ods.od.nih.gov/dsld/v8/label/{supplement['dsld_id'].item()}",
            timeout=10,
        )

    tab1, tab2, tab3 = st.tabs(["Inputs", "NutritionProduct", "Response"])

    with tab1:
        status_option = st.selectbox(
            "Select Status?",
            ("active", "inactive", "entered-in-error"),
            0,
        )
        st.download_button(
            "Download",
            pd.DataFrame(nutrition_product).to_json(),
            mime="application/json",
        )
        st.session_state.status_option = status_option

    with tab2:
        product = response.json()
        ingredients = []
        manufacturer = []
        for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
            print(ingredient["name"])
        for contanct in product["contacts"]:
            print(contanct["name"])

        # print(statement_groups)
        nutrition_product = {
            "resourceType": "NutritionProduct",
            "status": st.session_state.status_option,
            "manufacturer": product["brand"],
        }

        st.json(nutrition_product)

    with tab3:
        st.json(response.json())
