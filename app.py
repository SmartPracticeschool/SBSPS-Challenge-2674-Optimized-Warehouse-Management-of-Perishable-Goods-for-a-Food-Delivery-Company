"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
import src.pages.about
import src.pages.home
import src.pages.Dataset as dataset
import src.pages.Visualization
import src.pages.solution
import src.pages.Predictions
import os

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "Dataset": src.pages.Dataset,
    "Solution":src.pages.solution,
    "Training & Visualization": src.pages.Visualization,
    "Prediction":src.pages.Predictions,
    "About us": src.pages.about,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)



   


    
if __name__ == "__main__":
    main()
    
