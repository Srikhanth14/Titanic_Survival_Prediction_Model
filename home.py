# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:27:59 2023

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def home():
   
    image = Image.open("Boat.jpeg")

    # Display the image in your Streamlit app
    st.image(image,use_column_width=True)
    
    # Introduction
    st.write("Welcome to the Titanic Survival Prediction App!")
    st.write('''Embark on a journey to uncover the fate of passengers aboard the legendary
    Titanic. This web app showcases the power of machine learning in predicting survival
    outcomes based on various features.''')
    
    # Key Features
    st.subheader("Key Features:")
    st.write('''1. **Predictive Analytics:**
    Explore the predictions of passenger survival using advanced analytics. The model
    considers passenger class, gender, age, fare, embarkation port, and family size.''')
    
    st.write('''2. **User-Friendly Interface:**
    Navigate through the app effortlessly. No expertise required – simply input passenger
    details and witness the predictive magic.''')
    
    st.write('''3. **Data Visualization:**
    Visualize patterns and trends in the dataset with interactive charts. Gain insights into the
    factors influencing survival on the Titanic.''')
    
    # About the Project
    st.subheader("About the Project:")
    st.write('''The Titanic Survival Prediction project combines historical data with modern data
    science techniques. Join us in exploring the features that played a role in determining who
    survived the tragic voyage.''')
    
    # About Me
    st.subheader("About Me:")
    st.write('''Curious about the mind behind the predictions? I'm SRIKHANTH R, a dedicated
    data Anayst passionate about unraveling insights from data.''')
    
    st.write('''Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/srikhanth-r) or explore more
    projects on my [portfolio](https://www.datascienceportfol.io/srikhanth_r). Let's dive deep into the world of data science
    together!''')
    
    
    # Call to Action
    st.write('''Ready to embark on this predictive journey? Head over to the **Dataset** page to
    explore the data and make your own survival predictions!''')
