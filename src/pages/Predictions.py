import streamlit as st
import awesome_streamlit as ast
import pandas as pd
import numpy as np
import os
import sys
from pandas.errors import ParserError
import time
import base64
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("Predictions")


        try:
            df = pd.read_csv('Testfile\\test_complete.csv')

            @st.cache(suppress_st_warning=True)
            def previous():
                st.markdown("\n\n\n")
                st.info("⬅️ You can download prediction from the side bar")
                df['num_orders'] = df['num_orders'].astype(int)
                st.subheader("\nThe weekly demand of the next 10 weeks (from 146-155) is:")
                fig = go.Figure(data=[go.Table(
                header=dict(
                    values=list(df.columns),
                    line_color='white',
                    fill_color='rgb(169, 169, 169)',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[df.id, df.week, df.center_id, df.meal_id, df.checkout_price,
                            df.base_price, df.emailer_for_promotion, df.homepage_featured,
                            df.num_orders],
                    line_color='white',
                    fill_color = 'rgb(255, 255, 255)',
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 12)
                    ))
                ])
                
                st.write(fig)
                data = pd.DataFrame(df).to_csv( index=False)        
                b64 = base64.b64encode(data.encode()).decode()  # some strings <-> bytes conversions necessary here
                href = f'<a href="data:file/csv;base64,{b64}">Download Results</a> (right-click and save as &lt;some_name&gt;.csv)'
                st.sidebar.markdown(href, unsafe_allow_html=True)   
            
            def second():


                st.header(" Get Predictions for the specific id")
                st.write("\n\n\n\n\n\n")

            

                id = st.number_input("Enter id",1000085,1499996)
                num=df.loc[df['id']==id]
                if(num.empty):
                    st.info("Id not found")
                else:
                    num =num.values
                    st.subheader("Following are the values for the entered id")
                    st.subheader("Week:")
                    st.info(int(num[0][1]))
                    st.subheader("Center Id:")
                    st.info(int(num[0][2]))
                    st.subheader("Meal Id:")
                    st.info(int(num[0][3]))
                    st.subheader("Checkout Price: ")
                    st.info(int(num[0][4]))
                    st.subheader("Base Price:")
                    st.info(int(num[0][5]))
                    st.subheader("Email for Promotion:")
                    if num[0][6]==1:
                        st.info("Yes")
                    else:
                        st.info("No")
                    st.subheader("Home Featured:")
                    if num[0][7]==1:
                        st.info("Yes")
                    else:
                        st.info("No")
                    st.subheader("Number of Orders:")
                    st.info(int(num[0][8]))
            previous()
            second()

        except FileNotFoundError:
            st.info("Training has not been done. Please train the model first")
            st.write(f'<img src="https://media1.giphy.com/media/Xg4Lc2tzOXXdNCU4Qc/source.gif" width="500" height="500">', unsafe_allow_html=True)

        

        

