"""
https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
"""


import streamlit as st
from dotenv import load_dotenv

from src import dsld_page, fdc_page

load_dotenv()

st.set_page_config(page_title="NutrientProduct", page_icon=":pill:")

base_url = "http://localhost:8000"

FDC = "Food Data Central"
DSLD = "Dietary Supplement Label Database"

if "status_option" not in st.session_state:
    st.session_state.status_option = "active"
if "nutrient_product" not in st.session_state:
    st.session_state.nutrient_product = None
if "product_name" not in st.session_state:
    st.session_state.product_name = None


sidebar_col1, sidebar_col2 = st.sidebar.columns(2)
with sidebar_col1:
    st.write("[NutritionProduct](https://build.fhir.org/nutritionproduct.html)")
with sidebar_col2:
    use_server = st.checkbox("Use Server?")


dashboard_option = st.sidebar.selectbox(
    "Select Dashboard?",
    (DSLD, FDC),
    0,
)

st.header(dashboard_option, ":pill:")

### Food Data Central
if dashboard_option == FDC:
    fdc_page.main(use_server, base_url)

### Dietary Supplement Label Database
if dashboard_option == DSLD:
    dsld_page.main(use_server, base_url)
