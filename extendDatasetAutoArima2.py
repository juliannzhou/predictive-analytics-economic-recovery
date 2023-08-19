import pandas as pd
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
    # Use auto_arima to determine the best order
    stepwise_model = auto_arima(train[column], seasonal=False, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
    best_order = stepwise_model.order

    # Use the best order for the ARIMA model
    model = ARIMA(train[column], order=best_order)
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=len(test))
    predictions[column] = forecast

# 5. Forecasting beyond the dataset
end_date = '2030-01-01'
total_weeks = pd.date_range(start='2023-04-01', end=end_date, freq='W')

# Initialize an empty DataFrame with the forecasted date range
consolidated_forecast = pd.DataFrame({
    'DATE': total_weeks
})

for column in train.columns:
    # Use auto_arima to determine the best order for the entire dataset
    stepwise_model = auto_arima(df[column], seasonal=False, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
    best_order = stepwise_model.order
    print("Best order:", best_order)

    # Use the best order for the ARIMA model
    model = ARIMA(df[column], order=best_order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(total_weeks))
    
    # Add the forecasted values as a new column to the consolidated DataFrame
    consolidated_forecast[column] = forecast.values

# Export the consolidated DataFrame to a single CSV file
consolidated_forecast.to_csv('autoArima2-1983-2030.csv', index=False)

# 6. Model Evaluation
for column in test.columns:
    mse = mean_squared_error(test[column], predictions[column])
    print(f'MSE for {column}: {mse}')
