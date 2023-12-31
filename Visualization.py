# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:54:27 2023

@author: ELCOT
"""

import streamlit as st
from PIL import Image
def visualization():
    # Page Title
    st.title("Visualizations")
    # Introduction
    st.write("Explore visualizations highlighting patterns and insights from Titanic passenger data.")
    
    # Image 1: Countplot Survival Distribution
    st.header("1. Countplot Survival Distribution")
    image1 = Image.open("Survival_Distribution.png") 
    st.image(image1, caption="Survival Distribution", use_column_width=True)
    
    # Image 2: Age Distribution Histogram
    st.header("2. Age Distribution Histogram")
    image2 = Image.open("Age_Distribution.png") 
    st.image(image2, caption="Age Distribution", use_column_width=True)
    
    # Image 3: Fare Distribution Histogram
    st.header("3. Gender Distribution Barplot")
    image3 = Image.open("Gender_Distribution.png") 
    st.image(image3, caption="Gender Distribution", use_column_width=True)
    
    # Image 4: Countplot Embarked Distribution
    st.header("4. Countplot Embarked Distribution")
    image4 = Image.open("Embarked_Distribution.png") 
    st.image(image4, caption="Embarked Distribution", use_column_width=True)
    
    # Image 5: Family Size Survival Rate Bar Plot
    st.header("5. Family Size Survival Rate Bar Plot")
    image5 = Image.open("Family_Size.png") 
    st.image(image5, caption="Family Size Survival Rate", use_column_width=True)
    
    # Call to Action
    st.write('''Ready to explore more or make predictions? Head to the **Dataset** and **Input
    Form** pages for a deeper dive into the Titanic data.''')
