import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample time series with random data
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
time_series_data = np.random.randn(len(date_rng))

# Create a DataFrame with the time series data
time_series_df = pd.DataFrame(time_series_data, columns=['Value'], index=date_rng)

# Plot the time series using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(time_series_df.index, time_series_df['Value'], label='Time Series Data', color='blue')
plt.title('Time Series Data Visualization')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()