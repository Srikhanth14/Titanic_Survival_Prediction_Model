# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:27:59 2023

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def app():
   
    image = Image.open('Boat.jpeg')
    # Display the image in your Streamlit app
    st.image(image,use_column_width=True)

    st.markdown("# Titanic Survival Prediction")
    # Welcome to Titanic Survival Prediction
    st.write(
    """
    Welcome to Titanic Survival Prediction
    Explore the fate of passengers aboard the Titanic! Our web app predicts whether a
    passenger survived or not based on their details. Dive into the world of data science and
    discover the insights from the tragic voyage.
    """
    )

    st.subheader("Key Features")
    st.write(
    """
    - Predict whether a passenger survived based on their details.
    - Explore the dataset and uncover insights from the Titanic voyage.
    - Easy-to-use interface to input passenger details and get predictions.
    - Learn about the historic event of the Titanic and its predictive analysis.
    """
    )
    st.subheader("Ready to Explore?")
    st.write(
    """
    Get started now! Navigate through the tabs to learn more about the dataset, input
    passenger details, and witness the predictive power of our model.
    """
    )
