import pandas as pd
import streamlit as st
import json


def main(nutrition_product: dict):
    """_summary_

    Args:
        nutrition_product (dict): _description_
    """
    print("nutrition_product...", json.dumps(nutrition_product, indent=4))
    st.download_button(
        label="Download NutritionProduct",
        # disabled=True if st.session_state.nutrient_product is None else False,
        data=json.dumps(nutrition_product, indent=4),
        mime="application/json",
    )
