import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

df = pd.read_csv('data_C02_emission.csv')

input_vars = [
    'Engine Size (L)',
    'Cylinders',
    'Fuel Consumption City (L/100km)',
    'Fuel Consumption Hwy (L/100km)',
    'Fuel Consumption Comb (L/100km)',
    'Fuel Consumption Comb (mpg)'
]
output_var = 'CO2 Emissions (g/km)'

X = df[input_vars]
y = df[output_var]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

plt.scatter(X_train['Engine Size (L)'], y_train, c='blue', s=10)
plt.scatter(X_test['Engine Size (L)'], y_test, c='red', s=10)
plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('Emissions vs Engine Size')
plt.show()

plt.hist(X_train['Engine Size (L)'])
plt.show()

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
plt.hist(X_train_scaled[:, 0])
plt.show()

X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

print(model.intercept_)
print(model.coef_)

y_pred = model.predict(X_test_scaled)
plt.scatter(y_test, y_pred)
plt.xlabel('Real values')
plt.ylabel('Predicted values')
plt.title('Real vs Predicted CO2 Emissions')
plt.show()

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
MAPE = mean_absolute_percentage_error(y_test, y_pred)
RMSE = mean_squared_error(y_test, y_pred, squared=False)
R2 = r2_score(y_test, y_pred)

print(MAE, MSE, MAPE, RMSE, R2)

metrics_r2 = []
for i in range(1, len(input_vars)+1):
    model_sub = LinearRegression()
    model_sub.fit(X_train_scaled[:, :i], y_train)
    y_pred_sub = model_sub.predict(X_test_scaled[:, :i])
    metrics_r2.append(r2_score(y_test, y_pred_sub))

print(metrics_r2)