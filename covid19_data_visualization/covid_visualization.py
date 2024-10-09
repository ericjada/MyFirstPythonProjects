import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the current working directory (where the script is being run)
current_directory = os.getcwd()

# Set the path to the CSV file dynamically, assuming it is in the 'data' subdirectory
data_path = os.path.join(current_directory, 'covid19_data_visualization', 'data', 'owid-covid-data.csv')

# Set the path to the 'visualizations' directory
visualizations_dir = os.path.join(current_directory, 'covid19_data_visualization', 'visualizations')

# Ensure the 'visualizations' directory exists
if not os.path.exists(visualizations_dir):
    os.makedirs(visualizations_dir)

# Print the paths to verify
print(f"Looking for the data file at: {data_path}")
print(f"Saving visualizations to: {visualizations_dir}")

# Load the CSV data into a DataFrame
data = pd.read_csv(data_path)

# Convert the 'date' column to a datetime object for proper plotting
data['date'] = pd.to_datetime(data['date'])

# Function to plot new cases over time for a specific country
def plot_new_cases(data, country):
    country_data = data[data['location'] == country]
    plt.figure(figsize=(10,6))
    plt.plot(country_data['date'], country_data['new_cases'], label=f'New Cases in {country}', color='blue')
    plt.xlabel('Date')
    plt.ylabel('New COVID-19 Cases')
    plt.title(f'Daily New COVID-19 Cases in {country}')
    plt.legend()
    plt.savefig(os.path.join(visualizations_dir, f'{country}_new_cases.png'))  # Save the plot as a PNG file
    plt.show()

# Function to plot total cases and total deaths over time for a specific country
def plot_total_cases_and_deaths(data, country):
    country_data = data[data['location'] == country]
    plt.figure(figsize=(10,6))
    plt.plot(country_data['date'], country_data['total_cases'], label='Total Cases', color='green')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Total Deaths', color='red')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title(f'Total COVID-19 Cases and Deaths in {country}')
    plt.legend()
    plt.savefig(os.path.join(visualizations_dir, f'{country}_cases_and_deaths.png'))  # Save the plot as a PNG file
    plt.show()

# Function to plot 7-day rolling average of new cases for a specific country
def plot_7day_avg_new_cases(data, country):
    country_data = data[data['location'] == country]
    country_data['new_cases_7day_avg'] = country_data['new_cases'].rolling(window=7).mean()
    plt.figure(figsize=(10,6))
    plt.plot(country_data['date'], country_data['new_cases_7day_avg'], label=f'7-Day Average New Cases in {country}', color='orange')
    plt.xlabel('Date')
    plt.ylabel('New COVID-19 Cases (7-day average)')
    plt.title(f'7-Day Rolling Average of New COVID-19 Cases in {country}')
    plt.legend()
    plt.savefig(os.path.join(visualizations_dir, f'{country}_7day_avg_new_cases.png'))  # Save the plot as a PNG file
    plt.show()

# Function to plot case fatality rate (CFR) over time for a specific country
def plot_case_fatality_rate(data, country):
    country_data = data[data['location'] == country]
    country_data['case_fatality_rate'] = country_data['total_deaths'] / country_data['total_cases']
    plt.figure(figsize=(10,6))
    plt.plot(country_data['date'], country_data['case_fatality_rate'], label=f'Case Fatality Rate in {country}', color='red')
    plt.xlabel('Date')
    plt.ylabel('Case Fatality Rate')
    plt.title(f'Case Fatality Rate Over Time in {country}')
    plt.legend()
    plt.savefig(os.path.join(visualizations_dir, f'{country}_cfr.png'))  # Save the plot as a PNG file
    plt.show()

# Function to compare new cases for multiple countries
def compare_new_cases(data, countries):
    plt.figure(figsize=(10,6))
    for country in countries:
        country_data = data[data['location'] == country]
        plt.plot(country_data['date'], country_data['new_cases'], label=country)
    plt.xlabel('Date')
    plt.ylabel('New COVID-19 Cases')
    plt.title('New COVID-19 Cases Comparison')
    plt.legend()
    plt.savefig(os.path.join(visualizations_dir, 'comparison_new_cases.png'))  # Save the plot as a PNG file
    plt.show()

# Main function to run the visualizations
def main():
    # Call functions to visualize data for the United States
    plot_new_cases(data, 'United States')
    plot_total_cases_and_deaths(data, 'United States')
    plot_7day_avg_new_cases(data, 'United States')
    plot_case_fatality_rate(data, 'United States')

    # Compare new cases between multiple countries (USA, India, Brazil)
    countries_to_compare = ['United States', 'India', 'Brazil']
    compare_new_cases(data, countries_to_compare)

# Entry point for the script
if __name__ == "__main__":
    main()
