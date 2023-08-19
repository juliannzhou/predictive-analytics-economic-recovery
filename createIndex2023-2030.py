import csv
import pandas as pd

def appendToCSV(val):
    with open('EHI-2023-2030-ARIMA.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([val])

# ordered based on alphabetical order of columns
feature_rank = [0.823332319, 0.968706134, 0.00993695, 0.962182598,
                0.283132067, 0.850528726, 0.869850653, 0.672332248,
                0.919218144, 0.112236151, 0.760717009, 0.303502222,
                0.997993709, 0.826920584, 0.229311899, 0.646416649,
                0.498817155
                ]
df = pd.read_csv('./finalArimaDatasets/arima_consolidated_forecast_2023_2030.csv')
df = df[sorted(df.columns)]
df = df.drop(columns=['DATE', 'GDP'])

with open('EHI-2023-2030-ARIMA.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Economic Health Index'])

for index, row in df.iterrows():
    indexVal = 0
    for i in range(len(feature_rank)):
        weight = feature_rank[i]
        indexVal += weight * row[i]

    appendToCSV(indexVal)

print("done")
