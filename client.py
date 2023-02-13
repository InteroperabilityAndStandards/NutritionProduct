"""
https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
"""


import os
from tqdm.auto import tqdm

import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import sqlite3

from src import dsld_page, fdc_page
from scispacy.linking import EntityLinker
import spacy

dir_downloads = os.path.abspath(f"{os.getcwd()}/src/_downloads")


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


def create_umls_entity_ruler(ruler, df_cleaned_umls_terms):
    """A dummy docstring."""
    print("Creating UMLS entity ruler...")
    patterns = []
    for _, row in tqdm(
        df_cleaned_umls_terms.iterrows(), total=df_cleaned_umls_terms.shape[0]
    ):
        patterns.append({"label": row["CUI"], "pattern": row["STR"], "id": row["CUI"]})
    ruler.add_patterns(patterns)


@st.cache_resource
def load_nlp():
    nlp = spacy.load("en_core_sci_sm")
    nlp.add_pipe(
        "scispacy_linker",
        config={
            "resolve_abbreviations": True,
            "linker_name": "umls",
            "threshold": 0.85,
            "filter_for_definitions": False,
            # "disabling": ["tagger", "parser", "attribute_ruler", "lemmatizer"]
        },
    )
    ruler = nlp.add_pipe("entity_ruler", before="tok2vec")
    df_cleaned_umls_terms = pd.read_csv(
        f"{dir_downloads}/umls-data/filtered_umls_atoms.csv"
    )

    create_umls_entity_ruler(ruler, df_cleaned_umls_terms)
    return nlp, ruler


@st.cache_resource
def init_sqlite3():
    return sqlite3.connect("fhir.db")


def set_nutrient_product_state_to_none():
    st.session_state.nutrition_product = None


nlp, ruler = load_nlp()
init_sqlite3()


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

if use_server:
    st.sidebar.write(f"Server URL: {os.getenv('BASE_URL')}")

dashboard_option = st.sidebar.selectbox(
    "Select Dashboard?",
    app_dashboards_df,
    index=0,
    on_change=set_nutrient_product_state_to_none,
)

st.caption(dashboard_option)

### Food Data Central
if dashboard_option == app_dashboards_df[app_dashboards_df.key == "FDC"].name.item():
    fdc_page.main(use_server, base_url, nlp)

### Dietary Supplement Label Database
if dashboard_option == app_dashboards_df[app_dashboards_df.key == "DSLD"].name.item():
    dsld_page.main(use_server, base_url)
