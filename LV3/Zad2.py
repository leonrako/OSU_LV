import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_C02_emission.csv')

plt.figure()
df['CO2 Emissions (g/km)'].plot(kind="hist", bins=20)
plt.show()

df['Fuel Type'] = df['Fuel Type'].astype('category')
fuel_colors = {'Z': 'brown', 'X': 'red', 'E': 'blue', 'D': 'black'}

df.plot.scatter(
    x="Fuel Consumption City (L/100km)",
    y="CO2 Emissions (g/km)",
    c=df["Fuel Type"].map(fuel_colors),
    s=50
)
plt.show()

df.boxplot(column='CO2 Emissions (g/km)', by='Fuel Type')
plt.show()

fuel_counts = df.groupby('Fuel Type').size()
fuel_counts.plot(
    kind='bar',
    xlabel='Fuel Type',
    ylabel='Number of vehicles',
    title='Amount of vehicles by fuel type'
)
plt.show()

cylinders_avg_emission = df.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cylinders_avg_emission.plot(
    kind='bar',
    xlabel='Cylinders',
    ylabel='CO2 emissions (g/km)',
    title='CO2 emissions by number of cylinders'
)
plt.show()