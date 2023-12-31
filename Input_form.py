# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:31:04 2023

@author: ELCOT
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
    

def app():
    loaded_model = pickle.load(open("titanic_trained_model.sav","rb"))

    # Creating function for prediction
    def titanic_survival_prediction(input_data):

        # Map string values to numeric values
        sex_mapping = {'Male': 0, 'Female': 1}
        embarked_mapping = {'Q': 0, 'S': 1, 'C': 2}

        # Map 'Sex' and 'Embarked' columns to numeric values
        input_data[1] = sex_mapping.get(input_data[1],0) # 'Sex' column
        input_data[4] = embarked_mapping.get(input_data[4],0) # 'Embarked' column

        # Change the input data to a numpy array
        input_data_np_array = np.asarray(input_data)

        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        column_names = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'FamilySize']
        # Make predictions using the trained model
        input_data_reshaped_df = pd.DataFrame(input_data_reshaped,columns=column_names)
        prediction = loaded_model.predict(input_data_reshaped_df)

        # Display prediction result
        if prediction[0] == 0:
            st.error("The passenger did not survive.")
        else:
            st.success("The passenger survived.")
       
    def main():
        st.title('Titanic Survival Prediction Web App')
        st.write("Enter the Passenger Details: ")
        Pclass = st.selectbox('Passenger Class', [1, 2, 3],index=None)
        sex_options = ['Male', 'Female']
        Sex = st.radio('Sex', sex_options, index=None)
        Age = st.text_input("Passenger Age")
        Fare = st.text_input('Enter the Fare Amount')
        embarked_options = ['Q', 'S', 'C']
        Embarked = st.selectbox("Embarked", embarked_options,index=None)
        FamilySize = st.text_input('Family Size')

        if st.button('Survival Test Result'):
                titanic_survival_prediction([Pclass,Sex,Age,Fare,Embarked,FamilySize])

    
    main()


