#### STEP - 1 - IMPORTING LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import os

from PIL import Image


#Reading Dataset
df = pd.read_csv("resources\data\openpubs.csv")


#st.title("OPEN PUB WEB APPLICATION")
st.markdown("<h1 style='text-align: center; color: red;'>OPEN PUB WEB-APP</h1>", unsafe_allow_html=True)

#Reading the Image File
image = Image.open("resources\images\pub.jpg")
st.image(image, use_column_width= True)

#Brief Description about PUB's

st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'>What is a PUB? </h1>", unsafe_allow_html=True)
st.markdown("The word pub is short for 'Public House'. It describes an establishment that's been granted a licence to serve alcoholic beverages for drinking on the premises.")
st.markdown('This web application was developed to help you find the closest pub in UK while you are on a vacation with your friends.')

st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'>Data Summary</h1>", unsafe_allow_html=True)

st.dataframe(df.head())


statistics = st.selectbox(
    "Statistical Data",
    ('Number of Pub\'s in UK','Shape','Tail','Describe'))

if statistics == 'Number of Pub\'s in UK':
    st.markdown(f'The number of  Pubs  in  **UK** is **{df.shape[0]}**')

elif statistics == 'Shape':
    st.text('Number of rows: {}'.format(df.shape[0]))
    st.text('Number of columns: {}'.format(df.shape[1]))

elif statistics == 'Tail':
    st.dataframe(df.tail())

elif statistics == 'Describe':
    st.table(df.describe())
