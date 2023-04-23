import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image


# Reading Dataset

filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "openpubs.csv"))

df = pd.read_csv(filepath)
df.columns=['fsa_id','name','address','postcode','easting','northing','lat','lon','local_authority']

#Replacing Special characters with NaN and Dropping the Null Values.
df = df.replace('\\N',np.NaN)
df = df.dropna()

df[['lat', 'lon']] = df[['lat', 'lon']].apply(pd.to_numeric)
df.info()


st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'> PUB's NEAR ME </h1>", unsafe_allow_html=True)

lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.0001)
lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.0001)
button = st.button("Search")
df_new = df[['lat', 'lon']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 

Eucl_distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))
## Sort the pubs by distance and get the nearest 5 pubs using argpartition
n = 5
min_indices = np.argpartition(Eucl_distances, n-1) [:n]


if button:
    st.map(df.iloc[min_indices])
    st.text("The location corresponding to below nearest distances : ")
    st.dataframe(df.iloc[min_indices])