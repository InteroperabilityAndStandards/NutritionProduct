import json

import streamlit as st


def main():
    """_summary_

    Args:
        nutrition_product (dict): _description_
    """
    name = "NutritionProduct"
    if st.session_state.nutrition_product is not None:
        name = st.session_state.nutrition_product["code"]["text"]
    # print("nutrition_product...", json.dumps(nutrition_product, indent=4))
    st.download_button(
        label="Download NutritionProduct",
        disabled=True if st.session_state.nutrition_product is None else False,
        data=json.dumps(st.session_state.nutrition_product, indent=4),
        file_name=f"{name}.json",
        mime="application/json",
    )
