# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:31:24 2023

@author: ELCOT
"""

import streamlit as st
import pandas as pd

def dataset():
    
    # Dataset Information
    st.header("Dataset Information:")
    st.write('''The predictive model is trained on a dataset containing information about Titanic
    passengers, including features such as Pclass, Sex, Age, Fare, Embarked, and
    FamilySize.''')
    
    # Data Source
    st.header("Data Source:")
    st.write("For more details, you can explore the dataset on Kaggle: [Click Here](https://www.kaggle.com/datasets/brendan45774/test-file)")
    
    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the Titanic dataset:")
    data = pd.read_csv("tested.csv") # Update with the actual file name
    st.dataframe(data.head())
    # Display your sample data here
    
    st.subheader("Download Dataset")
    st.write("You can download the full Titanic dataset for further exploration:")
    def data_read(data):
        return data.to_csv().encode('utf-8')
    csv=data_read(data)
    
    st.download_button(
                        label='Download Sample Data',
                        data=csv,
                        file_name='titanic.csv',
                        mime='text/csv'      
                    )
    
    # Input Your Data
    st.header("Input Your Data:")
    st.write('''Want predictions for your specific passenger details? Enter your data in the input
    form and discover the forecasted survival outcome.''')
    
    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write('''To ensure successful predictions, enter your data with the same features as the
    sample data. Include columns for Pclass, Sex, Age, Fare, Embarked, and FamilySize.''')
    
    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Titanic Survival Prediction GitHub Repository](https://github.com/Srikhanth14/CODSOFT/blob/main/Project_1_Titanic_Survival_Prediction.ipynb)")
    
    # Conclusion
    st.write('''Ready to get predictions for your data? Input your passenger details in the input
    form, and let the Titanic Survival Prediction app work its magic!''')    

