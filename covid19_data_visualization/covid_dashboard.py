import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Get the current working directory
current_directory = os.getcwd()

# Set the path to the CSV file dynamically, assuming it is in the 'data' subdirectory
data_path = os.path.join(current_directory, 'covid19_data_visualization', 'data', 'owid-covid-data.csv')

# Load the CSV data into a DataFrame
data = pd.read_csv(data_path)

# Convert the 'date' column to a datetime object for proper plotting
data['date'] = pd.to_datetime(data['date'])

# Streamlit title and description
st.title("COVID-19 Data Dashboard")
st.write("This dashboard provides visualizations of COVID-19 data for different countries.")

# Country selection
countries = data['location'].unique()
selected_country = st.selectbox("Select a country", countries)

# Filter the data for the selected country
country_data = data[data['location'] == selected_country]

# Calculate 7-day rolling average for new cases
country_data['new_cases_7day_avg'] = country_data['new_cases'].rolling(window=7).mean()

# Plotting the new cases
st.subheader(f"New COVID-19 Cases in {selected_country}")
st.line_chart(country_data.set_index('date')['new_cases'])

# Plotting the 7-day rolling average of new cases
st.subheader(f"7-Day Rolling Average of New Cases in {selected_country}")
st.line_chart(country_data.set_index('date')['new_cases_7day_avg'])

# Plotting total cases and total deaths
st.subheader(f"Total Cases and Deaths in {selected_country}")
st.line_chart(country_data.set_index('date')[['total_cases', 'total_deaths']])

# Display case fatality rate
country_data['case_fatality_rate'] = country_data['total_deaths'] / country_data['total_cases']
st.subheader(f"Case Fatality Rate in {selected_country}")
st.line_chart(country_data.set_index('date')['case_fatality_rate'])

# Display a data summary for the selected country
st.subheader(f"Summary Data for {selected_country}")
st.write(country_data[['date', 'new_cases', 'total_cases', 'total_deaths', 'new_cases_7day_avg', 'case_fatality_rate']].tail())
