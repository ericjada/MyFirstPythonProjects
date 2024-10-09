
# COVID-19 Data Visualization Dashboard

This project is a COVID-19 Data Visualization dashboard built using Python and Streamlit. The dashboard allows users to interactively explore COVID-19 data for various countries, visualizing new cases, total cases, deaths, 7-day rolling averages, and case fatality rates.

## Project Overview

The script generates visualizations for:

1. **Daily New Cases**: Line chart showing new COVID-19 cases for the selected country.
2. **7-Day Rolling Average of New Cases**: A smoothed-out visualization of new cases.
3. **Total Cases and Deaths**: Line chart showing cumulative cases and deaths.
4. **Case Fatality Rate (CFR)**: Ratio of total deaths to total cases over time.

The data is sourced from [Our World in Data](https://ourworldindata.org/covid-sources) and updated in CSV format. The script automatically generates and saves visualizations to a `visualizations` folder.

## Features

- **Interactive Country Selection**: Users can modify the code to choose different countries to visualize.
- **Multiple Visualizations**: New cases, deaths, rolling averages, and case fatality rates over time.
- **Automated Visualizations**: Generates and saves PNG files in the `visualizations` folder.
- **Modularized Code**: The script uses functions and a `main()` function for better organization.

## Installation and Usage

### Prerequisites

- Python 3.x
- Streamlit (for the dashboard)

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

3. Run the script:
   ```bash
   python covid_visualization.py
   ```

4. The visualizations will be saved automatically in the `visualizations` directory.

### File Structure

```
covid19_data_visualization/
│
├── data/
│   └── owid-covid-data.csv  # COVID-19 dataset
│
├── visualizations/          # Folder where plots will be saved
│
├── covid_dashboard.py       # The Streamlit dashboard script
├── covid_visualization.py   # Python script for generating visualizations
└── README.md                # This README file
```

## Data Source

The data used in this project is from [Our World in Data](https://covid.ourworldindata.org/data/owid-covid-data.csv).

## License

This project is open-source and licensed under the MIT License.

## Author

This project was created by [Eric](https://github.com/ericjada).
