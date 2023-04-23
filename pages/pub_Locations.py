import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image


# Reading Dataset
df = pd.read_csv("resources\data\open_pubs.csv")

df.columns=['fsa_id','name','address','postcode','easting','northing','lat','lon','local_authority']

#Replacing Special characters with NaN and Dropping the Null Values.
df = df.replace('\\N',np.NaN)
df = df.dropna()

df[['lat', 'lon']] = df[['lat', 'lon']].apply(pd.to_numeric)
df.info()


st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'> UK PUB LOCATIONS </h1>", unsafe_allow_html=True)

#Get User Input to Search for Location based on Postal Code or Local Authority

location_search = st.selectbox("Choose Search Type", ["Postal_Code", "Local_Authority"])

#Conditonal Statement for Postal_Code User Input:

if location_search == "Postal_Code":
    location_postal = df["postcode"].unique()
    option = st.selectbox('Choose Postal_Code',location_postal)

#Conditional Statement for Local_Authority User Input:

if location_search == "Local_Authority":
    location_authority = df["local_authority"].unique()
    option = st.selectbox('Choose Local_Authority',location_authority)


btn_clk = st.button('Search')

if location_search == "Postal_Code":
    if btn_clk==True:
        result = df[df['postcode']==option]
        result = result[['lat','lon']]
        st.success('These are the Pub\'s results under the criteria selected.')
        st.map(result, zoom = 10 , use_container_width=True)

elif location_search == "Local_Authority":
    if btn_clk==True:
        result = df[df['local_authority']==option]
        result = result [['lat','lon']]
        st.success('These are the Pub\'s results under the criteria selected.')
        st.map(result, zoom = 10 , use_container_width=True)
