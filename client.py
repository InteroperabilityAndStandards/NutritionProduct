"""
https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
"""


import os

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from src import dsld_page, fdc_page

load_dotenv()

st.set_page_config(page_title="NutrientProduct", page_icon=":pill:")

# base_url = "http://localhost:8000"
base_url = os.getenv("BASE_URL")


app_dashboards_df = pd.DataFrame(
    [
        {
            "name": "Food Data Central",
            "key": "FDC",
        },
        {
            "name": "Dietary Supplement Label Database",
            "key": "DSLD",
        },
    ]
)


def set_nutrient_product_state_to_none():
    st.session_state.nutrition_product = None


if "status_option" not in st.session_state:
    st.session_state.status_option = "active"
if "nutrition_product" not in st.session_state:
    st.session_state.nutrition_product = None
if "product_name" not in st.session_state:
    st.session_state.product_name = None


sidebar_col1, sidebar_col2 = st.sidebar.columns(2)
with sidebar_col1:
    st.write("[NutritionProduct](https://build.fhir.org/nutritionproduct.html)")
with sidebar_col2:
    use_server = st.checkbox("Use Server?")
    set_nutrient_product_state_to_none()


dashboard_option = st.sidebar.selectbox(
    "Select Dashboard?",
    app_dashboards_df,
    index=0,
    on_change=set_nutrient_product_state_to_none,
)

st.caption(dashboard_option)

### Food Data Central
if dashboard_option == app_dashboards_df[app_dashboards_df.key == "FDC"].name.item():
    fdc_page.main(use_server, base_url)

### Dietary Supplement Label Database
if dashboard_option == app_dashboards_df[app_dashboards_df.key == "DSLD"].name.item():
    dsld_page.main(use_server, base_url)
