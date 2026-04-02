import pandas as pd 

data = pd.read_csv('data_C02_emission.csv')


length = len(data['Make'])
print(f'DataFrame ima {length} mjerenja')

for col in data.columns:
    print(f"{col} has a type of {data[col].dtype}")

data['Vehicle Class'] = data['Vehicle Class'].astype('category')

print(f"Redovi s izostalim vrijednostima: {data.isnull().sum()}")
print(f"Duplicirane vrijednosti: {data.duplicated().sum()}")


least_consuming = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
most_consuming = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print('Most consuming: ')
print(most_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print('Least consuming: ')
print(least_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])


selected_data = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
length = len(selected_data['Make'])
print(f"Postoji {length} vozila koje imaju motor izmedu 2.5 i 3.5 L")

print(f"Prosjecni C02 ovih vozila jest: {selected_data['CO2 Emissions (g/km)'].mean()} g/km")


selected_data = data[(data['Make'] == 'Audi')]
length = len(selected_data['Make'])
print(f"U mjerenjima ima {length} mjerenja koja se odnose na marku Audi")

selected_data = selected_data[(selected_data['Cylinders'] == 4)]
print(f"Prosjecni CO2 4 cilindrasa marke Audi je {selected_data['CO2 Emissions (g/km)'].mean()} g/km")


cylinder_counts = data['Cylinders'].value_counts().sort_index()
print(cylinder_counts)

cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print("Cylinder emissions: ")
print(cylinder_emissions)


diesels = data[(data['Fuel Type'] == 'D')]
petrols = data[(data['Fuel Type'] == 'Z')]

print(f"Dizeli:\nProsjecno: {diesels['Fuel Consumption City (L/100km)'].mean()} - Medijalno: {diesels['Fuel Consumption City (L/100km)'].median()}")
print(f"Benzinci:\nProsjecno: {petrols['Fuel Consumption City (L/100km)'].mean()} - Medijalno: {petrols['Fuel Consumption City (L/100km)'].median()}")


four_cylinder_diesels = diesels[(diesels['Cylinders'] == 4)]
print(f"4 cilindricni dizel koji najvise goriva trosi u gradu jest:\n{four_cylinder_diesels.nlargest(1, 'Fuel Consumption City (L/100km)')}")


manuals = data[(data['Transmission'].str[0] == 'M')]
length = len(manuals['Make'])
print(f"Postoji {length} vozila s rucnim mjenjacem")


print(data.corr(numeric_only=True))
