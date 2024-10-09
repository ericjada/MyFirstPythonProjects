
# COVID-19 Data Visualization Dashboard

This project is a COVID-19 Data Visualization dashboard built using Python and Streamlit. The dashboard allows users to interactively explore COVID-19 data for various countries, visualizing new cases, total cases, deaths, 7-day rolling averages, and case fatality rates.

## Project Overview

The dashboard provides visualizations for:

1. **Daily New Cases**: Line chart showing new COVID-19 cases for the selected country.
2. **7-Day Rolling Average of New Cases**: A smoothed-out visualization of new cases.
3. **Total Cases and Deaths**: Line chart showing cumulative cases and deaths.
4. **Case Fatality Rate (CFR)**: Ratio of total deaths to total cases over time.

The data is sourced from [Our World in Data](https://ourworldindata.org/covid-sources) and updated in CSV format. The dashboard is interactive, allowing users to select any country from the dataset.

## Features

- **Interactive Country Selection**: Users can select a country to visualize COVID-19 metrics.
- **Data Summary**: Displays the latest data summary for the selected country.
- **Time Series Visualizations**: New cases, deaths, rolling averages, and case fatality rates over time.
- **Easy Setup**: The project is designed to be run locally with minimal setup using Streamlit.

## Installation and Usage

### Prerequisites

- Python 3.x
- Streamlit

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ericjada/MyFirstPythonProjects.git
   cd MyFirstPythonProjects/covid19_data_visualization
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run covid_dashboard.py
   ```

4. The dashboard will automatically open in your default web browser. If not, you can view it by visiting `http://localhost:8501` in your browser.

### File Structure

```
covid19_data_visualization/
│
├── data/
│   └── owid-covid-data.csv  # COVID-19 dataset
│
├── visualizations/          # Folder where plots will be saved
│
├── covid_dashboard.py       # The main dashboard script
├── covid_visualization.py   # Python script for generating visualizations
└── README.md                # This README file
```

## Data Source

The data used in this project is from [Our World in Data](https://covid.ourworldindata.org/data/owid-covid-data.csv).

## License

This project is open-source and licensed under the MIT License.

## Author

This project was created by [Eric](https://github.com/ericjada).
