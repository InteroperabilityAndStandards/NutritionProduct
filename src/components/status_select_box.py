import streamlit as st
import pandas as pd

# from ..types.NutritionProduct import Status


def main():
    """_summary_"""
    with st.container():
        status_option = st.selectbox(
            "Select Status",
            ("active", "inactive", "entered-in-error"),
            0,
        )

    return status_option
