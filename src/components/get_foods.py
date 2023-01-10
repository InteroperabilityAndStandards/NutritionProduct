import requests
import streamlit as st


def main(use_server: bool, base_url: str, food_name: str):
    """_summary_"""
    response = None
    with st.spinner():
        # if st.session_state.product_name != food_name:
        if use_server:
            response = requests.get(f"{base_url}/food/{food_name}", timeout=15)
        else:
            response = requests.get(
                f"https://api.nal.usda.gov/fdc/v1/food/{food_name}?api_key=DEMO_KEY",
                timeout=15,
            )
    if response and response.status_code == 200:
        st.session_state.product_name = food_name
        return response.json()
    else:
        raise Exception("No response from server")
