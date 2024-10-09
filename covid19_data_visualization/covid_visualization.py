import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data/owid-covid-data.csv')

# Filter by a specific country
us_data = data[data['location'] == 'United States']
us_data['date'] = pd.to_datetime(us_data['date'])

# Plot the new cases over time
plt.figure(figsize=(10,6))
plt.plot(us_data['date'], us_data['new_cases'], label='New Cases', color='blue')
plt.xlabel('Date')
plt.ylabel('New COVID-19 Cases')
plt.title('Daily New COVID-19 Cases in the United States')
plt.legend()
plt.show()
