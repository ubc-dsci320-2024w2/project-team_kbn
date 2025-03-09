import pandas as pd
# importlib.reload(kli_query_family)
import kli_query_family

# Clean the public_trees.csv dataset
def clean_public_trees(df): 
    """
    Cleans the DataFrame by .
    
    Parameters:
        df (pd.DataFrame): Original DataFrame containing genus names.
    
    Returns:
        pd.DataFrame: DataFrame with additional columns for latitude, longitude, nomenclature, full address and family names.
    """
    
    # `HEIGHT_RANGE` is set to be an ordinal attribute, with the order provided in `priority_order`
    priority_order = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '>90']
    df['HEIGHT_RANGE'] = pd.Categorical(df['HEIGHT_RANGE'], categories=priority_order, ordered=True)
    
    # `TREE_ID`, `CIVIC_NUMBER`, `ON_STREET_BLOCK` are set to be categorical attributes
    df[['TREE_ID', 'CIVIC_NUMBER', 'ON_STREET_BLOCK']] = df[['TREE_ID', 'CIVIC_NUMBER', 'ON_STREET_BLOCK']].astype(str)
    
    # Earlier EDA provided `CULTIVAR_NAME`, `NEIGHBOURHOOD_NAME`, `DATE_PLANTED` as having NA values; `CULTIVAR_NAME` is filled with the corresponding `SPECIES_NAME`, `NEIGHBOURHOOD_NAME` has `NA` strings applied instead, and `DATE_PLANTED` is left with `None`
    df['CULTIVAR_NAME'] = df['CULTIVAR_NAME'].fillna(df['SPECIES_NAME'])
    df['NEIGHBOURHOOD_NAME'] = df['NEIGHBOURHOOD_NAME'].fillna('NA')
    df['DATE_PLANTED'] = df['DATE_PLANTED'].fillna('')
    
    # Latitude and longitude are initially joined together in a single column geo_point_2d and thus need to be split
    df[['LATITUDE', 'LONGITUDE']] = df['geo_point_2d'].str.split(', ', expand=True)
    df['LATITUDE'] = df['LATITUDE'].astype(float)
    df['LONGITUDE'] = df['LONGITUDE'].astype(float)
    
    # The values 9, 0 and 10 all correspond to HEIGHT_RANGE = '>90' and thus 0 and 10 are replaced with value 9
    df['HEIGHT_RANGE_ID'] = df['HEIGHT_RANGE_ID'].replace([0, 10], 9)
    
    # `NOMENCLATURE` is a column derived from combining `GENUS_NAME` and `SPECIES_NAME` into 1 string
    df['NOMENCLATURE'] = df['GENUS_NAME'] + " " + df['SPECIES_NAME']
    
    # `ON_ADDRESS` is a column derived from combining `ON_STREET` and `ON_STREET_BLOCK` into 1 string
    df['ON_ADDRESS'] = df['ON_STREET_BLOCK'] + " " + df['ON_STREET'] + " " + df['NEIGHBOURHOOD_NAME'] + " (" + df['STREET_SIDE_NAME'] + ")"

    # Following code is in code/kli_query_family.py
    genus_to_family_dict = kli_query_family.get_genus_to_family_mapping(df)
    df_with_family = kli_query_family.map_family_to_dataframe(df, genus_to_family_dict)
    kli_query_family.add_family_name_to_cleaned("../../data/processed/public_trees_cleaned.csv", df_with_family)
    
    return df_with_family
