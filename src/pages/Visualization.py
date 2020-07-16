"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast
import pandas as pd
import numpy as np
from sklearn import preprocessing
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import os
import sys
from pandas.errors import ParserError
import time
import matplotlib.cm as cm
import base64
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go



# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("Training & Visualization")

    # if os.path.isfile('Testfile\\test_complete.csv'):
    #     os.remove("Testfile\\test_complete.csv")


    class Predictor:
        # Data preparation part, it will automatically handle with your data

        def declare(self):
            global data_train
            global data_test
            data_train = self.data_train[self.features]
            data_test = self.data_test[self.features_test]
        
        @st.cache(suppress_st_warning=True)
        def graphics(self):

            st.header("Visualization of Training Data")
         
            st.subheader("Graph of week vs number of orders ")
            df =data_train[['week','num_orders']]
            df = df.groupby(['week'],as_index=False).sum()
            fig = px.line(df,y='num_orders',x='week')
            fig.update_layout(template="plotly_dark")
            st.write(fig)
            


            st.subheader("Graph of category vs number of orders")
            df1 = data_train[['category','num_orders']]
            df1 = df1.groupby(['category'],as_index=False).sum()
            fig1 = px.bar(df1, x='category', y='num_orders',color= 'num_orders')
            fig1.update_layout(template="plotly_dark")
            st.write(fig1)

            st.subheader("Graph of cuisine vs number of orders ")
            cat = ['Beverages', 'Rice Bowl', 'Starters', 'Pasta', 'Sandwich',
                'Biryani', 'Extras', 'Pizza', 'Seafood', 'Other Snacks', 'Desert',
                'Soup', 'Salad', 'Fish']
            df2=data_train[['category','cuisine','num_orders']]
            df2 = df2.groupby(['category','cuisine'],as_index=False).sum()



            fig2 = make_subplots(rows=2, cols=2,vertical_spacing=0.3)
            fig2.add_trace( go.Bar(name='Italian', x=cat, y=[13953970,0,0,1637744,17636782,0,0,0,0,0,0,0,10944336,0,]),row=1, col=1)
            fig2.add_trace(go.Bar(name='Continental', x=cat, y=[5943046,0,0,0,0,0,0,7383720,2715714,0,0,0,0,871959]),row=1, col=2)
            fig2.add_trace( go.Bar(name='Thai', x=cat, y=[18237307,0,4649122,0,0,0,3984979,0,0,4766293,0,1039646,0,0,]),row=2, col=1)
            fig2.add_trace( go.Bar(name='Indian', x=cat, y=[2345879,20874063,0,0,0,631848,0,0,0,0,1940632,0,0,0]) ,row=2, col=2)

            # Update yaxis properties
            fig2.update_yaxes(title_text="Num of orders", row=1, col=1)
            fig2.update_yaxes(title_text="Num of orders",  row=1, col=2)
            fig2.update_yaxes(title_text="Num of orders",  row=2, col=1)
            fig2.update_yaxes(title_text="Num of orders", row=2, col=2)

            fig2.update_layout(template="plotly_dark",height=800, width=800)
            st.write(fig2)       
        



        @st.cache(suppress_st_warning=True)
        def prepare_data(self):
            global data_train
            global data_test
            data_train = self.data_train[self.features]
            data_test = self.data_test[self.features_test]
            # target_options = data_train.columns
            # self.chosen_target = st.sidebar.selectbox("Please choose target column", (target_options))

            with st.spinner('Feature Engineering Started.......'):
                # Convert 'city_code' and 'region_code' into a single feature - 'city_region'.
                data_train['city_region'] = \
                    data_train['city_code'].astype('str') + '_' + \
                    data_train['region_code'].astype('str')
            
            
                data_test['city_region'] = \
                    data_test['city_code'].astype('str') + '_' + \
                    data_test['region_code'].astype('str')
            
            # Label encode categorical columns for use in LightGBM.
                label_encode_columns = ['center_id','meal_id',
                    'city_code','region_code','city_region','center_type',
                    'category','cuisine']
            

                le = preprocessing.LabelEncoder()

                for col in label_encode_columns:
                    le.fit(data_train[col])
                    data_train[col + '_encoded'] = le.transform(data_train[col])
                    data_test[col + '_encoded'] = le.transform(data_test[col])

            
                # Feature engineering - treat 'week' as a cyclic feature.
                # Encode it using sine and cosine transform.
                data_train['week_sin'] = \
                    np.sin(2 * np.pi * data_train['week'] / 52.143)
                data_train['week_cos'] = \
                    np.cos(2 * np.pi * data_train['week'] / 52.143)

                data_test['week_sin'] = \
                    np.sin(2 * np.pi * data_test['week'] / 52.143)
                data_test['week_cos'] = \
                    np.cos(2 * np.pi * data_test['week'] / 52.143)
            
            

            # Convert email and homepage features into a single feature - 'email_plus_homepage'.
                data_train['email_plus_homepage'] = \
                    data_train['emailer_for_promotion'] + \
                    data_train['homepage_featured']

                data_test['email_plus_homepage'] = \
                    data_test['emailer_for_promotion'] + \
                    data_test['homepage_featured']
            
            

            

                # Log transform the target variable - num_orders.
                data_train['num_orders'] = np.log1p(data_train['num_orders'])
            
            st.success("Feature Engineering Complete ✔️ ")
        
        
        # Classifier type and algorithm selection
        def set_classifier_properties(self):
            self.type = st.sidebar.selectbox(
                "Algorithm type", ('Regression', 'No other options available'))
            if self.type == "Regression":
                self.chosen_classifier = st.sidebar.selectbox(
                    "Please choose a classifier", ('LGBMRegressor', 'No other options available'))
                if self.chosen_classifier == 'LGBMRegressor':
                    self.n_trees = st.sidebar.slider('number of trees', 0, 30000, 2000)
                    self.learning_rate = float(st.sidebar.text_input('learning rate:', '0.003'))
        
        
        
        # Model training and predicitons
        
        def predict(self, predict_btn):

            if self.type == "Regression":
                if self.chosen_classifier == 'LGBMRegressor':
                
                    # Prepare a list of columns to train on.
                    # Also decide which features to treat as numeric and which features to treat as categorical.
                    columns_to_train = ['week', 'week_sin', 'week_cos',
                                'checkout_price', 'base_price', 'email_plus_homepage', 'city_region_encoded', 'center_type_encoded', 'op_area', 'category_encoded', 'cuisine_encoded', 'center_id_encoded', 'meal_id_encoded']

                    categorical_columns = ['email_plus_homepage',
                               'city_region_encoded', 'center_type_encoded',
                               'category_encoded', 'cuisine_encoded',
                               'center_id_encoded', 'meal_id_encoded']

                

                    numerical_columns = [col for col in columns_to_train if col not in categorical_columns]

                    # Train-Test split.
                    global X
                    global y
                    global y_test
                    global y_train

                    X = data_train[categorical_columns + numerical_columns]
                    y = data_train[self.chosen_target]
                    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.02,shuffle=False)

                

                    g = {'colsample_bytree': 0.4,'min_child_samples': 5,'num_leaves': 255}
                    
                
                    with st.spinner('Training in Progress.......'):


                      
                        self.alg = LGBMRegressor(
                            learning_rate=self.learning_rate, n_estimators=self.n_trees, silent=False, **g)

                        fit_params = {'early_stopping_rounds': 1000,
                            'feature_name': categorical_columns + numerical_columns, 'categorical_feature': categorical_columns,
                            'eval_set': [(X_train, y_train), (X_test, y_test)]}

        
                    
                        self.alg.fit(X_train, y_train, **fit_params)
                        X = data_test[categorical_columns + numerical_columns]
                        predictions = self.alg.predict(X)
                        predictions = np.expm1(predictions)
                        self.predictions = predictions
                        

                        y_pred = self.alg.predict(X_test)
                        global mse
                        mse =mean_squared_error(y_test,y_pred)
                        df = data_t.copy()
                        df['num_orders'] = predictions
                        df.to_csv('Testfile\\test_complete.csv',index=False)
                        mse= round(mse, 4)
                    st.success("Training Complete ✔️")
                    st.subheader(" Mean Squared Error :")
                    st.success(mse)
                    st.markdown("\n\n")
                    st.info("Please go the prediction section to see the predictions and download the file ")


            return self.predictions
    
        
        def file_selector(self):
            file = st.sidebar.file_uploader("Choose the train CSV file", type="csv")
            if file is not None:
                data = pd.read_csv(file)
                return data
            else:
                st.markdown("Please upload the train csv file")

        
        def file_selector2(self):
            global data_t
            file = st.sidebar.file_uploader("Choose the test CSV file", type="csv")
            if file is not None:
                data = pd.read_csv(file)
                data_t= data
                return data
            else:
                st.markdown("Please upload the test csv file")

        
        def file_selector3(self):
            file = st.sidebar.file_uploader("Choose the meal info CSV file", type="csv")
            if file is not None:
                data = pd.read_csv(file)
                return data
            else:
                st.markdown("Please upload the meal info csv file")

        
        def file_selector4(self):
            file = st.sidebar.file_uploader("Choose the fulfillment center CSV file", type="csv")
            if file is not None:
                data = pd.read_csv(file)
                return data
            else:
                st.markdown("Please upload the fullfillment csv file")

        
        def set_features(self):
            self.features =  self.data_train.columns
    
        
        def set_features2(self):
            self.features_test =  self.data_test.columns

        
        def file(self):

            submission_df = data_t.copy()
            submission_df['num_orders'] = predictions

            df = submission_df
            df.to_csv('Testfile\\test_complete.csv')
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
                values=[df.id,df.num_orders],
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

        
        def merge(self):
            df_train = pd.merge(self.df_train, self.df_center_info,how="left",left_on='center_id',right_on='center_id')
            df_train = pd.merge(df_train, self.df_meal_info,how='left',left_on='meal_id',right_on='meal_id')
            df_test = pd.merge(self.df_test, self.df_center_info,how="left",left_on='center_id',right_on='center_id')
            df_test = pd.merge(df_test, self.df_meal_info,how='left',left_on='meal_id',right_on='meal_id')

            return df_train,df_test
    
    

    st.markdown("")
    st.markdown("\n\n")
    controller = Predictor()

    try:
        st.sidebar.markdown("Input train data")
        controller.df_train = controller.file_selector()

        st.sidebar.markdown("Input meal info data")
        controller.df_meal_info  = controller.file_selector3()

        st.sidebar.markdown("Input fulfillment center data")
        controller.df_center_info  = controller.file_selector4()

        st.sidebar.markdown("Input test data")
        controller.df_test = controller.file_selector2()

        

        if controller.df_train is not None:
            if controller.df_meal_info  is not None:
                if controller.df_center_info  is not None:
                    st.success("Training Dataset Loaded ✔️")


        if controller.df_test is not None:
            st.success("Testing Dataset Loaded ✔️")

        if controller.df_train is not None:
            if st.sidebar.checkbox('Show training raw data'):
                st.subheader('Raw data')
                df = controller.df_train.head(1000)
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
                    font = dict(color = 'darkslategray')
                    ))
                ])
                fig.update_layout(height=600,width=900)
                st.write(fig)
            
        if controller.df_train is not None:
            if controller.df_test is not None:
                if controller.df_center_info is not None:
                    if controller.df_meal_info is not None:
                        controller.data_train,controller.data_test =controller.merge()
                        controller.set_features()
                        controller.set_features2()
        

                        if len(controller.features) > 1:
                            controller.declare()
                            controller.graphics()
                            controller.prepare_data()
                            target_options = data_train.columns
                            controller.chosen_target = st.sidebar.selectbox("Please choose target column", (target_options[0:9]))
                            controller.set_classifier_properties()
                            predict_btn = st.sidebar.button('Predict')
                            if controller.data_train is not None and len(controller.features) > 1:
                        
                                if predict_btn:
                                    st.sidebar.markdown("Progress:")
                                    my_bar = st.sidebar.progress(0)
                                    for percent_complete in range(1,50):
                                        my_bar.progress(percent_complete + 1)
                                        

                                    predictions = controller.predict(predict_btn)
                                    for percent_complete in range(50,100):
                                        my_bar.progress(percent_complete + 1)
                                    
                                else:
                                    st.info("💁 Select the target variable on the sidebar and press Predict")
                                    

                    
            
    except (AttributeError, ParserError, KeyError) as e:
        st.write(e)
        st.markdown('<span style="color:blue">WRONG FILE TYPE</span>',unsafe_allow_html=True)


        
        

    
