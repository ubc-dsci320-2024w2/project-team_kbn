from pygbif import species

def get_genus_to_family_mapping(df, genus_column='GENUS_NAME'):
    """
    Maps unique genus names to family names using the GBIF API.

    Parameters:
        df (pd.DataFrame): DataFrame containing genus names.
        genus_column (str): Column name for genus names. Default is 'GENUS_NAME'.

    Returns:
        dict: Dictionary mapping genus names (lowercase) to family names ("NaN" if not found).
    """
    
    unique_genera = df[genus_column].str.lower().unique()
    
    genus_to_family = {}
    
    for genus in unique_genera:
        try:
            result = species.name_backbone(name=genus)
            family = result.get('family', "NaN")
        except Exception as e:
            print(f"Error querying GBIF for genus '{genus}': {e}")
            family = "NaN"
        genus_to_family[genus] = family
    
    return genus_to_family


def add_family_column(df, genus_to_family_dict, genus_column='GENUS_NAME', family_column='FAMILY_NAME'):
    """
    Adds a family column to the DataFrame by mapping genus names to family names.

    Parameters:
        df (pd.DataFrame): DataFrame to modify.
        genus_to_family_dict (dict): Dictionary mapping genus names (lowercase) to family names.
        genus_column (str): Column name for genus names. Default is 'GENUS_NAME'.
        family_column (str): New column name for family names. Default is 'FAMILY_NAME'.

    Returns:
        pd.DataFrame: DataFrame with the new family column.
    """
    if genus_column not in df.columns:
        raise ValueError(f"Column '{genus_column}' not found in DataFrame.")
    
    df[family_column] = df[genus_column].apply(
        lambda genus_name: genus_to_family_dict.get(genus_name.lower(), "NaN").upper()
    )
    
    return df