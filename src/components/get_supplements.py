import requests
import streamlit as st


def main(use_server: bool, base_url: str, supplement_name: str):
    """_summary_"""
    response = None
    with st.spinner():
        # if st.session_state.product_name != supplement_name:
        if use_server:
            response = requests.get(
                f"{base_url}/supplement/{supplement_name}",
                timeout=15,
            )
        else:
            response = requests.get(
                f"https://api.ods.od.nih.gov/dsld/v8/label/{supplement_name}",
                timeout=15,
            )
    if response and response.status_code == 200:
        st.session_state.product_name = supplement_name
        return response.json()
    else:
        raise Exception("No response from server")
