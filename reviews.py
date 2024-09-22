import pandas as pd
df = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# value counts for each country
country_counts = df['country'].value_counts().reset_index()
country_counts.columns = ['country', 'count']

# average points for each country
average_points = df.groupby('country')['points'].mean().reset_index()
average_points.columns = ['country', 'points']

# Merge the two DataFrames on 'country'
summary = pd.merge(country_counts, average_points, on='country')

# Sort the summary by country
summary = summary.sort_values(by='count', ascending=False)

# To match the table
summary['points'] = summary['points'].round(1)
summary.columns = ['country', 'count', 'points']


output_file_path = 'data/reviews-per-country.csv'

# new CSV file
summary.to_csv(output_file_path, index=False)