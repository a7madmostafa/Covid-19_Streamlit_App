import pandas as pd
import plotly.express as px
import streamlit as st
import os

csv_path = os.path.join(os.getcwd(), 'WHO-COVID-19-global-data.csv')
# Load Data
@st.cache_data  # the new updated streamlit data caching decorator.
def load_data():
    # df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    #df = pd.read_csv(csv_path)
    df = pd.read_csv("WHO-COVID-19-global-data.csv")
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    return df

df = load_data()

def countries_total_cases(countries, start_date = df.Date_reported.min(), end_date = df.Date_reported.max()):
    if countries != 'All Countries':
        df_temp = df[(df['Country'].isin(countries))]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_cases',
             title='Total Cases', range_x=[start_date, end_date], nbins=50)
    return fig

def regions_total_cases(regions, start_date = df.Date_reported.min(), end_date = df.Date_reported.max()):
    if regions != 'All Regions':
        df_temp = df[(df['WHO_region'].isin(regions))]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_cases',
             title='Total Cases', range_x=[start_date, end_date], nbins=50)
    return fig

def countries_total_deaths(countries, start_date = df.Date_reported.min(), end_date = df.Date_reported.max()):
    if countries != 'All Countries':
        df_temp = df[(df['Country'].isin(countries))]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_deaths',
             title='Total Deaths', range_x=[start_date, end_date], nbins=50)
    return fig

def regions_total_deaths(regions, start_date = df.Date_reported.min(), end_date = df.Date_reported.max()):
    if regions != 'All Regions':
        df_temp = df[(df['WHO_region'].isin(regions))]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_deaths',
             title='Total Deaths', range_x=[start_date, end_date], nbins=50)
    return fig
