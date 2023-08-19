import pandas as pd
import matplotlib
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima

"""
REASON: We are trying to predict when the economy will recover, so not only do we have to create regression models on
past data, but we also have to forecast what the economy will look like in the future in order to test our model.
In this class, we predict each of the element's daily value until 2030
"""

# 1. Load the data
df = pd.read_csv("weekly-1983-Present.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index('DATE', inplace=True)

# 2. Visualize the data
column_groups = [df.columns[i:i+4] for i in range(0, len(df.columns), 4)]
for group in column_groups:
    df[group].plot(subplots=True, figsize=(15, 10))
    plt.legend(loc='best')
    plt.show()

# 3. Train / Test Split
train = df[:'2015-01-01']
test = df['2015-01-01':]

# 4. Model Training & Prediction
predictions = {}
for column in train.columns:
    model = ARIMA(train[column], order=(6,2,1))
    model_fit = model.fit()

    """
    model = auto_arima(feature_column, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
    model.fit(feature_column)
    print(model.order)
    """
    forecast = model_fit.forecast(steps=len(test))
    predictions[column] = forecast
    
    plt.figure(figsize=(10, 6))
    plt.plot(train.index, train[column], label='Train')
    plt.plot(test.index, test[column], label='Test')
    plt.plot(test.index, forecast, label='ARIMA Forecast')
    plt.title(column)
    plt.legend()
    plt.show()

# 5. Forecasting beyond the dataset
end_date = '2030-01-01'
total_weeks = pd.date_range(start='2023-04-01', end=end_date, freq='W')

# Initialize an empty DataFrame with the forecasted date range
consolidated_forecast = pd.DataFrame({
    'DATE': total_weeks
})

for column in train.columns:
    model = ARIMA(df[column], order=(6,2,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(total_weeks))
    
    # Add the forecasted values as a new column to the consolidated DataFrame
    consolidated_forecast[column] = forecast.values  # Use .values to ensure only values are added

# Export the consolidated DataFrame to a single CSV file
consolidated_forecast.to_csv('consolidated_forecast_2023_2030.csv', index=False)

# 6. Model Evaluation
for column in test.columns:
    mse = mean_squared_error(test[column], predictions[column])
    print(f'MSE for {column}: {mse}')




