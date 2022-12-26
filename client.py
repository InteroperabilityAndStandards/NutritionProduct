"""
https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
"""


import streamlit as st
from dotenv import load_dotenv
import json

from src import dsld_page, fdc_page
from src.components import resource_selectbox

load_dotenv()

st.set_page_config(page_title="NutrientProduct", page_icon=":pill:")

base_url = "http://localhost:8000"


APP_DASHBOARDS = [
    {"dashboard": "Food Data Central"},
    {"dashboard": "Dietary Supplement Label Database"},
]

FDC = "Food Data Central"
DSLD = "Dietary Supplement Label Database"

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


def set_nutrient_product_state_to_none():
    st.session_state.nutrition_product = None


dashboard_option = st.sidebar.selectbox(
    "Select Dashboard?",
    (DSLD, FDC),
    index=0,
    on_change=set_nutrient_product_state_to_none,
)

resource_selectbox.main()

st.caption(dashboard_option)

### Food Data Central
if dashboard_option == FDC:
    fdc_page.main(use_server, base_url)

### Dietary Supplement Label Database
if dashboard_option == DSLD:
    dsld_page.main(use_server, base_url)
