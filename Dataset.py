# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:31:24 2023

@author: ELCOT
"""

import streamlit as st
import pandas as pd
def app():
    st.title("Titanic Dataset Overview")

    st.write(
    """
    Welcome to the Titanic Dataset Page. This dataset provides valuable information about
    passengers aboard the Titanic, allowing us to explore and understand patterns related to
    survival. It has undergone cleaning and exploratory data analysis (EDA) as part of the
    project.
    """)
    
    st.subheader("Data Source")
    st.write("- Source: [Kaggle](https://www.kaggle.com/)")
    st.write("- Dataset Credits: [Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file)")

    st.subheader("Data Cleaning")
    st.write("The dataset has been cleaned to ensure accurate and reliable analysis.")

    st.subheader("Exploratory Data Analysis (EDA)")
    st.write("""Exploratory data analysis has been conducted to gain insights into the dataset.
    Visualizations and summaries are available in the project.""")

    st.subheader("Sample Data")
    st.write("Here is a snippet of the dataset, showcasing a few rows:")
    data=pd.read_csv("tested.csv")
    st.dataframe(data)

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
    
    #st.markdown("[Download Titanic Dataset](csv_download_link)")
    st.subheader("GitHub Repository")
    st.write("For detailed information,and project code, you can explore the [GitHub repository](https://github.com/Srikhanth14/CODSOFT).")
    st.write("Feel free to explore the dataset and check out the analysis conducted during the project!")
    

