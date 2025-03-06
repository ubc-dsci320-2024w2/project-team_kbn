import pandas as pd

# The .csv from the website provided is more difficult to parse, so Excel is used
public_trees = pd.read_excel("data/raw/public-trees.xlsx")
public_trees.to_csv("data/raw/public-trees.csv", index=False)
print("Read file")

# Latitude and longitude are initially joined together in a single column geo_point_2d and thus need to be split
public_trees_cleaned = public_trees.copy()
public_trees_cleaned[['LATITUDE', 'LONGITUDE']] = public_trees_cleaned['geo_point_2d'].str.split(', ', expand=True)
public_trees_cleaned['LATITUDE'] = public_trees_cleaned['LATITUDE'].astype(float)
public_trees_cleaned['LONGITUDE'] = public_trees_cleaned['LONGITUDE'].astype(float)
print("Cleaned LATITUDE and LONGITUDE")

# The priority for HEIGHT_RANGE is provided in priority_order
priority_order = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '>90']
public_trees_cleaned['HEIGHT_RANGE'] = pd.Categorical(public_trees_cleaned['HEIGHT_RANGE'], categories=priority_order, ordered=True).astype(str)
print("HEIGHT_RANGE set")

# The values 9, 0 and 10 all correspond to HEIGHT_RANGE = '>90' and thus are grouped together to value 9
public_trees_cleaned['HEIGHT_RANGE_ID'] = public_trees_cleaned['HEIGHT_RANGE_ID'].replace([0, 10], 9)
print("HEIGHT_RANGE_ID set")

# Earlier EDA provided 'CULTIVAR_NAME', 'NEIGHBOURHOOD_NAME', 'DATE_PLANTED' as having NA values; 'CULTIVAR_NAME' is filled with the corresponding 'SPECIES_NAME', while 'NEIGHBOURHOOD_NAME', 'DATE_PLANTED' have 'NA' strings applied instead
public_trees_cleaned['CULTIVAR_NAME'] = public_trees_cleaned['CULTIVAR_NAME'].fillna(public_trees_cleaned['SPECIES_NAME'])
public_trees_cleaned['NEIGHBOURHOOD_NAME'] = public_trees_cleaned['NEIGHBOURHOOD_NAME'].fillna('')
public_trees_cleaned['DATE_PLANTED'] = public_trees_cleaned['DATE_PLANTED'].fillna('')
print("NAs filled")

# Due to being redundant and difficult to use, 'Geom' and 'geo_point_2d' are dropped
public_trees_cleaned = public_trees_cleaned.drop(columns=['Geom', 'geo_point_2d'])
print("Columns dropped")

# Write processed data to "data/processed/public_trees_cleaned.csv"
public_trees_cleaned.to_csv("data/processed/public_trees_cleaned.csv", index=False)
print("Processed data saved")