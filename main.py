import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')

df['Date.Full'] = pd.to_datetime(df['Date.Full'])

df.set_index('Date.Full', inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Data.Precipitation'], color='g', label='Precipitation')
plt.title('Daily Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_precipitation_trend.png')
plt.show()


monthly_avg_temp = df['Data.Temperature.Avg Temp'].resample('ME').mean()

plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_temp.index, monthly_avg_temp, color='r', marker='o', linestyle='-', label='Monthly Avg Temperature')
plt.title('Monthly Average Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_average_temperature.png')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df['Data.Wind.Speed'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Wind Speeds')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('wind_speed_distribution.png')
plt.show()
