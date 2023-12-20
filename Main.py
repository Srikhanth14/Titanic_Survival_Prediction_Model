# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:20:05 2023

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home, About, Dataset,Input_form

st.set_page_config(page_title="Titanic", page_icon="ship", layout="wide")        

selected = option_menu(
                            menu_title="Titanic",
                            options=["Home","About","Dataset", "Input_form"],
                            icons=["house-fill","book","bar-chart-fill", "card-list"],
                            menu_icon="menu-up",
                            default_index=0,
                            orientation="horizontal"
                      )
if selected == "Home":
    home.app()
if selected == "Dataset":
    Dataset.app()
if selected == "Input_form":
    Input_form.app()
if selected == "About":
    About.app()