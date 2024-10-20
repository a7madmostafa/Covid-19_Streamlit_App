import streamlit as st
import pandas as pd

import helper

# Load Data
df = helper.load_data()

# About Data
st.title('About Data')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')

# Display Data
st.header('Data')
if st.checkbox('Show Data'):
    st.write(df)
