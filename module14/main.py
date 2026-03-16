import pandas as pd
from keras.src.layers import average

df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

first_rows = df.head()

print(first_rows)

country_data = df["Country"]

print(country_data)

subset = df [['Country' , 'Average IQ']]

print(subset)


filterd_df = subset[subset['Average IQ'] > 100 ]

print(filterd_df)

null_mask = df.isnull()

null_count = null_mask.sum()

print("Count of the null values in each colum")
print(null_count)


df.dropna(inplace=True)
print(df.info())


duplicaate_count = df.duplicated().sum()

print("Count of duplicate rows")
print(duplicaate_count)


average_iq_continent = df.groupby('Countinent')['Average IQ'].mean()

print(average_iq_continent)

sorted_average_iq_per_continent = average_iq_continent.sort_values(ascending=False)

print(sorted_average_iq_per_continent)


