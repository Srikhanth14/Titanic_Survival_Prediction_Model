# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:20:05 2023

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home,Dataset,Visualization,Input_form

st.set_page_config(page_title="Titanic", page_icon="ship", layout="wide")        

selected = option_menu(
                            menu_title="Titanic",
                            options=["Home","Dataset","Visualization","Input_form"],
                            icons=["house-fill","database-down","bar-chart", "ui-radios-grid"],
                            menu_icon="ship",
                            default_index=0,
                            orientation="horizontal"
                      )
if selected == "Home":
    home.home()
if selected == "Dataset":
    Dataset.dataset()
if selected == "Visualization":
    Visualization.visualization()
if selected == "Input_form":
    Input_form.app()
