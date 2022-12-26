import pandas as pd
import streamlit as st

RESOURCES = [
    {
        "name": "NutritionProduct",
        "link": "https://build.fhir.org/nutritionproduct.html",
    },
    {"name": "NutritionIntake", "link": "https://build.fhir.org/nutritionintake.html"},
    {"name": "NutritionOrder", "link": "https://build.fhir.org/nutritionorder.html"},
]

resources_df = pd.DataFrame(RESOURCES)


def main():
    col1, col2 = st.columns(2)

    with col1:
        resource_name = st.selectbox(
            "Select Resource?",
            resources_df,
            0,
        )
    with col2:
        st.button("[NutritionProduct](https://build.fhir.org/nutritionproduct.html)")

        return resource_name
