# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:28:21 2023

@author: ELCOT
"""

import streamlit as st
def app():
    st.title("Titanic Survival Prediction")
    st.write("""Discover the Titanic's story through our web app, which predicts whether a passenger
    survived based on their details. Immerse yourself in the realm of data science and unlock
    insights from this historic voyage""")  

    st.subheader("Purpose")
        
    st.write("""This application aims to delve into the fate of Titanic passengers using machine learning.
    Explore the dataset, understand influential features, and experience the predictive
    capabilities of our model.""")


    st.subheader("Journey Through History and Data")
    st.write("""
    1. Explore the Dataset: Analyze the Titanic dataset for a comprehensive understanding.
    2. Input Form: Easily input passenger details for predictions.
    3. Result Display: Receive predictions with a click of a button.
    4. Dataset Insights: Dive deeper into the "Dataset" tab for additional information.
    Embark on an interactive and educational journey through the Titanic's history and data!""")

    st.subheader("Why Titanic?")
    st.write("""
    The sinking of the Titanic is a historic event, and our model uses machine learning to predict
    survival outcomes. Explore the dataset, make your predictions, and uncover the stories of
    those who sailed on the ill-fated voyage.""")
    
