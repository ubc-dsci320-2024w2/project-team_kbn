import pandas as pd

# The .csv from the website provided is more difficult to parse, so Excel is used
public_trees = pd.read_excel("data/raw/public-trees.xlsx")
public_trees.to_csv("data/raw/public-trees.csv", index=False)
print("Read file")

public_trees_cleaned = public_trees.copy()

# `HEIGHT_RANGE` is set to be an ordinal attribute, with the order provided in `priority_order`
priority_order = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '>90']
public_trees_cleaned['HEIGHT_RANGE'] = pd.Categorical(public_trees_cleaned['HEIGHT_RANGE'], categories=priority_order, ordered=True)

# `TREE_ID`, `CIVIC_NUMBER`, `ON_STREET_BLOCK` are set to be categorical attributes
public_trees_cleaned[['TREE_ID', 'CIVIC_NUMBER', 'ON_STREET_BLOCK']] = public_trees_cleaned[['TREE_ID', 'CIVIC_NUMBER', 'ON_STREET_BLOCK']].astype(str)

print("Set to correct data types")

# Earlier EDA provided `CULTIVAR_NAME`, `NEIGHBOURHOOD_NAME`, `DATE_PLANTED` as having NA values; `CULTIVAR_NAME` is filled with the corresponding `SPECIES_NAME`, `NEIGHBOURHOOD_NAME` has `NA` strings applied instead, and `DATE_PLANTED` is left with `None`
public_trees_cleaned['CULTIVAR_NAME'] = public_trees_cleaned['CULTIVAR_NAME'].fillna(public_trees_cleaned['SPECIES_NAME'])
public_trees_cleaned['NEIGHBOURHOOD_NAME'] = public_trees_cleaned['NEIGHBOURHOOD_NAME'].fillna('NA')
public_trees_cleaned['DATE_PLANTED'] = public_trees_cleaned['DATE_PLANTED'].fillna('')
print("NAs filled")

# Latitude and longitude are initially joined together in a single column geo_point_2d and thus need to be split
public_trees_cleaned[['LATITUDE', 'LONGITUDE']] = public_trees_cleaned['geo_point_2d'].str.split(', ', expand=True)
public_trees_cleaned['LATITUDE'] = public_trees_cleaned['LATITUDE'].astype(float)
public_trees_cleaned['LONGITUDE'] = public_trees_cleaned['LONGITUDE'].astype(float)
print("Cleaned LATITUDE and LONGITUDE")

# The values 9, 0 and 10 all correspond to HEIGHT_RANGE = '>90' and thus 0 and 10 are replaced with value 9
public_trees_cleaned['HEIGHT_RANGE_ID'] = public_trees_cleaned['HEIGHT_RANGE_ID'].replace([0, 10], 9)
print("HEIGHT_RANGE_ID set")

# `NOMENCLATURE` is a column derived from combining `GENUS_NAME` and `SPECIES_NAME` into 1 string
public_trees_cleaned['NOMENCLATURE'] = public_trees_cleaned['GENUS_NAME'] + " " + public_trees_cleaned['SPECIES_NAME']
print("Created NOMENCLATURE")

# `ON_ADDRESS` is a column derived from combining `ON_STREET` and `ON_STREET_BLOCK` into 1 string
public_trees_cleaned['ON_ADDRESS'] = public_trees_cleaned['ON_STREET_BLOCK'] + " " + public_trees_cleaned['ON_STREET'] + " " + public_trees_cleaned['NEIGHBOURHOOD_NAME'] + " (" + public_trees_cleaned['STREET_SIDE_NAME'] + ")"
print("Created ON_ADDRESS")

# Due to being redundant and difficult to use, 'Geom' and 'geo_point_2d' are dropped
public_trees_cleaned = public_trees_cleaned.drop(columns=['Geom', 'geo_point_2d'])
print("Columns dropped")

# Write processed data to "data/processed/public_trees_cleaned.csv"
public_trees_cleaned.to_csv("data/processed/public_trees_cleaned.csv", index=False)
print("Processed data saved")