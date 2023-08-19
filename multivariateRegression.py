import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df = pd.read_csv('weekly-1983-Present.csv')

# all features except DATE, GDP, and Real GDP
X = df.drop(['DATE', 'GDP', 'Real GDP'], axis=1)

# 2 different y's in case there is a difference; should be no difference
y = df['GDP']

lr = LinearRegression().fit(X, y)
c = lr.intercept_
m = lr.coef_

y_pred_train = lr.predict(X)

# Scatter plot of actual vs predicted values
plt.scatter(y, y_pred_train, color='blue', label='Data points')
plt.xlabel("Actual GDP")
plt.ylabel("Predicted GDP")

# Plotting the regression line
plt.plot(y, y_pred_train, color='red', label='Regression Line')

plt.legend()
plt.show()

rSquared = r2_score(y, y_pred_train)
print("R^2 Value:", rSquared)
