import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('weekly-1983-2023+holt-winters.csv', delimiter='\t')
print(df)

df['DATE'] = pd.to_datetime(df['DATE'])

# Split the data based on the year
before_2023 = df[df['DATE'].dt.year < 2023]
from_2023_to_2030 = df[(df['DATE'].dt.year >= 2023) & (df['DATE'].dt.year <= 2030)]

plt.figure(figsize=(10,6))

# Plot the data before 2023 with one color
plt.plot(before_2023['DATE'], before_2023['Economic Health Index'], color='blue', label='Before 2023')

# Plot the data from 2023 to 2030 with another color
plt.plot(from_2023_to_2030['DATE'], from_2023_to_2030['Economic Health Index'], color='red', label='2023-2030')

# Set x-axis major ticks to every 5 years
ax = plt.gca()  # Get the current axis
ax.xaxis.set_major_locator(mdates.YearLocator(base=5))  # Set major ticks every 5 years
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format major ticks to display just the year

plt.title('Economic Health Index Over Time')
plt.xlabel('Date')
plt.ylabel('Economic Health Index')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
