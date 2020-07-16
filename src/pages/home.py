import streamlit as st
import os
import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("")
        st.markdown("\n\n\n")
        if os.path.isfile('Testfile\\test_complete.csv'):
            os.remove("Testfile\\test_complete.csv")

        st.write(f'<img src="https://onefamily.ie/wp-content/uploads/2019/12/img_ed7460393073e6b0abab4a69b572f0bc_1512388377925_processed_original.jpg" width="750" height="500">', unsafe_allow_html=True)
        st.markdown("\n\n\n")
        st.write("\n\n")
        st.write(
            """
            **Demand forecasting** is a key component to every growing online business. Without proper demand forecasting processes in place, it can be nearly impossible to have the right amount of stock on hand at any given time. 

A food delivery service has to deal with a lot of perishable raw materials which makes it all, 
the most important factor for such a company is to accurately forecast daily and weekly demand. Too much inventory in the warehouse means more risk of wastage, and not enough could lead to out-of-stocks — and push customers to seek solutions from your competitors. 

The replenishment of majority of raw materials is done on weekly basis and since the raw material is perishable, the procurement planning is of utmost importance.

              



It has been a challenging task to manage perishable food supply chains because of the
perishable product’s short lifetime, the possible spoilage of the product due to its deterioration
nature, and the retail demand uncertainty. All of these factors can lead to a significant amount
of shortage of food items and a substantial retail loss. The mass spoilage and difficulty in
management impel retailers to set a higher retail price, which retains the consumption and results in
frequent shortages.


The recent development of tracing and tracking technologies, which facilitate effective monitoring of the inventory level and product quality continuously, can greatly improve the performance of food supply chain and reduce spoilage waste.
Motivated by this recent technological advancement, our research aims to investigate the situation and has come to a conclusion that, optimized management can be done only when profit is more and loss is less. Profit depends on the timely 
supply of quality products to the consumers, which can be determined when the demand is known. Prediction of demand can help anticipate the supply, which in return can prevent loss of perishable goods.


In this project, get a taste of demand forecasting challenge using a real dataset.


            """
        )
        
    

        
