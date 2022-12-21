import streamlit as st


def main():
    """_summary_"""
    status_option = st.selectbox(
        "Select Status?",
        ("active", "inactive", "entered-in-error"),
        0,
    )

    return status_option
