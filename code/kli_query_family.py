from pygbif import species
import pandas as pd

def get_genus_to_family_mapping(df, genus_column='GENUS_NAME'):
    """
    Maps unique genus names to family names using the GBIF API with name_lookup.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing genus names.
        genus_column (str): Column name for genus names. Default is 'GENUS_NAME'.
    
    Returns:
        dict: Dictionary mapping genus names (lowercase) to family names ("NaN" if not found).
    """
    
    unique_genera = df[genus_column].str.lower().str.split().str[0].unique()
    
    genus_to_family = {}
    
    for genus in unique_genera:
        family = "NaN"

        response = species.name_lookup(genus, rank="genus", limit=10)

        if response.get('results'):
            for result in response['results']:
                if 'family' in result:
                    family = result['family']
                    break 
        
        genus_to_family[genus] = family
    
    return genus_to_family

def map_family_to_dataframe(df, genus_to_family_dict, genus_column='GENUS_NAME', family_column='FAMILY_NAME'):
    """
    Maps the genus-to-family dictionary back to the original DataFrame.
    
    Parameters:
        df (pd.DataFrame): Original DataFrame containing genus names.
        genus_to_family (dict): Dictionary mapping genus names to family names.
        genus_column (str): Column name for genus names. Default is 'GENUS_NAME'.
        family_column (str): Column name to store family names. Default is 'FAMILY_NAME'.
    
    Returns:
        pd.DataFrame: DataFrame with an additional column for family names.
    """
    df['cleaned_genus'] = df[genus_column].str.lower().str.split().str[0]
    df[family_column] = df['cleaned_genus'].map(genus_to_family_dict).str.upper()
    df.drop(columns=['cleaned_genus'], inplace=True)
    
    return df

def add_family_name_to_cleaned(file_path, df_with_family):
    """
    Adds FAMILY_NAME to the processed CSV by merging on TREE_ID.
    If FAMILY_NAME already exists, it skips the process.
    
    Parameters:
        file_path (str): Path to the processed CSV file.
        df_with_family (pd.DataFrame): DataFrame containing TREE_ID and FAMILY_NAME.
    
    Returns:
        None: Updates the CSV file in place.
    """
    df_cleaned = pd.read_csv(file_path)

    if 'FAMILY_NAME' in df_cleaned.columns:
        print("FAMILY_NAME already exists in the dataset. Skipping merge.")
        return

    df_selected = df_with_family[['TREE_ID', 'FAMILY_NAME']]

    df_cleaned = df_cleaned.merge(df_selected, on="TREE_ID", how="right")

    df_cleaned.to_csv(file_path, index=False)
    
    print("FAMILY_NAME added and dataset saved.")