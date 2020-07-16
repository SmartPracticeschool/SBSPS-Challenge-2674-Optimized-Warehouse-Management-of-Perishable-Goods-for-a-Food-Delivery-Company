"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("")
        st.write(
            """
            ## Problem Statement
 The task is to predict the number of orders for the next 10 weeks for a meal delivery company in order to minimize wastage as well as overcome shortage.

## Machine Learning Model used
[**LightGBM**](https://lightgbm.readthedocs.io/en/latest/). Light GBM is prefixed as ‘Light’ because of its high speed. Light GBM can handle the large size of data and takes lower memory to run. Another reason of why Light GBM is popular is because it focuses on accuracy of results. LGBM also supports GPU learning and thus data scientists are widely using LGBM for data science application development.

LightGBM is used here because gradient boosting models are very powerful in handling huge amounts if data and this data set had more than 450000 rows. In such cases LGBM models served to be efficient with higher accuracy.

## Feature Engineering
Firstly, the feature **week** was converted to a cyclic feature, by changing the week data to **week cos** and **week sin**.This is useful when you are trying to capture dependencies like increased demand during a particular month every year due to a festival.

Other feature engineering which were applied are:
The ‘city_code’ and ‘region_code’ into a single feature - ‘**city_region**’.
**Price difference percentage** was added as a feature which is the difference of 'checkout_price' and 'base_price'.
The ad campaign features - ‘emailer_for_promotion’ and ‘homepage_featured’ were converted into a single feature.

LightGBM's **LabelEncoder** was used to convert the categorical data to numeric format.

## Modifying the target variable
The target variable **num_orders** was transformed into its logarithmic value to give the values of that column a more Gaussian like distribution.
""")


        st.code('''
        df_train['num_orders_log1p'] = np.log1p(df_train['num_orders'])
                ''')
        st.write(
    """
## Hyperparameter tuning
The scikit-learn’s Parameter Grid has been used to systematically search through hyperparameter values for the LightGBM model.

The hyperparameters that are tuned with this method are:

- **colsample_bytree** - Also called feature fraction, it is the fraction of features to consider while building a single gradient boosted tree. Reducing its value reduces overfitting by considering fewer features while building each tree.

- **min_child_samples** - The number of samples in the leaf node of the tree.

- **num_leaves** - The number of leaf nodes. Higher the number, the more complex and deeper the tree is going to be making the model overfit.

"""
        )
        st.write(
            """
## Train-test split and Cross Validation
The data was sorted in ascending order week wise. Since the task asked to predict the orders for a future date, the parameter **shuffle = False** because random shuffling of the data before the split does not make sense.
            """
        )
        st.code('''
        X=df_train[categorical_columns + numerical_columns]
        y=df_train['num_orders_log1p']
        X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.02, shuffle=False)
                ''')

        st.write(
            """
## Grid search and training
The grid search technique was used to search for finding the best hyperparameter values.

The model was then trained using the best hyperparameter values and a function called **early stopping** was called while training to reduce overfitting. This allowed me to keep a small test set aside while training and not the entire training set was used.
            """
        )

        st.code('''
        param_grid = {'num_leaves': [31, 127, 255],
              'min_child_samples': [5, 10, 30],
              'colsample_bytree': [0.4, 0.6, 0.8]}

        estimator = LGBMRegressor(learning_rate=0.003,
                              n_estimators=10000,
                              silent=False,
                              **g)
        
        fit_params = {'feature_name': categorical_columns + numerical_columns,
                  'categorical_feature': categorical_columns,
                  'eval_set': [(X_train, y_train), (X_test, y_test)]}
        
        estimator.fit(X_train, y_train, **fit_params)
                ''')

        st.write(
            """
## Getting predictions
Since the num_orders was transformed into its logarithmic format to train the model, it was necessary to revert back to its original format. For this the **np.expm1()** function has been used.
The predicted values are then stored in a dataframe with the corresponding id values given in the test data and is made available for downloading. For the purpose of downloading, some string byte encoding have been performed from the **base64** library of python.
            """
        )

        st.code('''
        submission_df['num_orders'] = predictions
        df = submission_df[['id', 'num_orders']]

        data = pd.DataFrame(df).to_csv( index=False)        
            b64 = base64.b64encode(data.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}">Download Results</a> (right-click and save as &lt;some_name&gt;.csv)'
            '''
        )
