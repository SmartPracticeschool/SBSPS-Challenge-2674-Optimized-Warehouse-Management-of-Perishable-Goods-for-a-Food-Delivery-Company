import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("Dataset")

        def display1():

                st.markdown("Your client is a meal delivery company which operates in multiple cities. They have various fulfillment centers in these cities for dispatching meal orders to their customers. The client wants you to help these centers with demand forecasting for upcoming weeks so that these centers will plan the stock of raw materials accordingly.")
                st.markdown("The replenishment of majority of raw materials is done on weekly basis and since the raw material is perishable, the procurement planning is of utmost importance. Secondly, staffing of the centers is also one area wherein accurate demand forecasts are really helpful. Given the following information, the task is to predict the demand for the next 10 weeks (Weeks: 146-155) for the center-meal combinations in the test set:")
                st.markdown("⚫Historical data of demand for a product-center combination (Weeks: 1 to 145)")
                st.markdown("⚫Product(Meal) features such as category, sub-category, current price and discount")
                st.markdown("⚫Information for fulfillment center like center area, city information etc.")
                st.subheader("Content")
                st.markdown("Weekly Demand data (train.csv): Contains the historical demand data for all centers")
                  


                st.markdown("fulfilmentcenterinfo.csv: Contains information for each fulfillment center")
                       
                st.markdown("meal_info.csv: Contains information for each meal being served")
                        
                        
                st.subheader("Acknowledgements")
                st.markdown("I don't own this data. This data was a  part of IBM Hack Challenge held by IBM. [Click here](https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018) to visit the Kaggle link for this dataset.")
                st.subheader("\n\n Note")
                st.info("Download the data from the above given link to input it in the visualization & training tab")
        display1()
    

       