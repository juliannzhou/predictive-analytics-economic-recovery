import pandas as pd
import os
import time

"""
directory = './rawData'
arr = ["NASDAQ.csv", "SPX500.csv"]

for file_name in arr:
    file_path = directory + "/" + file_name

    df = pd.read_csv(file_path, on_bad_lines='skip')
    df['Date'] = pd.to_datetime(df['Date'])
    df = (df.set_index('Date')
      .reindex(pd.date_range('1983-01-01', '2023-04-01', freq='W'))
      .rename_axis(['Date'])
      .fillna(-1.6969)
      .reset_index())
    colName = df.columns[1]
    firstIt = True
    prevVal = 0
    for index, row in df.iterrows():
        if firstIt:
            prevVal = row[colName]
            firstIt = False
            continue
        # remove time of day
        row['Date'] = row['Date'].date()
        curVal = row[colName]

        if curVal == -1.6969:
            df.at[index, colName] = prevVal
        else:
            prevVal = curVal
    
    csv_name = file_name[0:file_name.index(".csv")] + "-daily.csv"
    df.to_csv(csv_name)
    print("successfully created " + csv_name)
    time.sleep(2)
"""

directory = './rawData'
for file_name in os.listdir(directory):
    if file_name == "NASDAQ.csv" or file_name == "SPX500.csv":
        continue
    
    file_path = directory + "/" + file_name
    
    df = pd.read_csv(file_path, on_bad_lines='skip')
    df['DATE'] = pd.to_datetime(df['DATE'])
    df = (df.set_index('DATE')
    .reindex(pd.date_range('1983-01-01', '2023-04-01', freq='W'))
    .rename_axis(['DATE'])
    .fillna(-1.6969)
    .reset_index())
    colName = df.columns[1]
    firstIt = True
    prevVal = 0
    for index, row in df.iterrows():
        if firstIt:
            prevVal = row[colName]
            firstIt = False
            continue
        # remove time of day
        row['DATE'] = row['DATE'].date()
        curVal = row[colName]

        if curVal == -1.6969:
            df.at[index, colName] = prevVal
        else:
            prevVal = curVal
    
    csv_name = file_name[0:file_name.index(".csv")] + "-weekly.csv"
    df.to_csv(csv_name)
    print("successfully created " + csv_name)
    time.sleep(2)


