# This py is for scraping off https://www.paldat.org/, a Palynological database (an online publication on recent pollen)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_species_list(df, genus_column_name="GENUS_NAME", species_column_name="SPECIES_NAME"):
    """
    Searches for species in the PalDat database based on a DataFrame containing genus and species names.

    Args:
        df (pd.DataFrame): A DataFrame containing genus and species names.
        genus_column_name (str): The name of the column containing genus names. Default is "GENUS_NAME".
        species_column_name (str): The name of the column containing species names. Default is "SPECIES_NAME".

    Returns:
        list: A list of scientific names that were found in the PalDat database.
    """
    df_sci_name = df.copy()
    
    df_sci_name['SCIENTIFIC_NAME'] = (
        df_sci_name[genus_column_name].str.capitalize() + ' ' + df_sci_name[species_column_name].str.lower()
    )
    
    unique_scientific_names = df_sci_name['SCIENTIFIC_NAME'].unique()
    
    species_list = [
        name.replace(' xx', '').replace(' x', '').strip().replace(" ", "_") 
        for name in unique_scientific_names
    ]
    

    output_list = []
    
    with requests.Session() as session:
        
        for species_name in species_list:
            
            url = f"https://www.paldat.org/pub/{species_name}"
            try:
                response = session.get(url, timeout=10)  
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    if soup.find('h1', class_='species'):
                        output_list.append(species_name)
                        
            except requests.exceptions.RequestException as e:
                print(f"Error requesting {url}: {e}")
    
    return output_list

def map_has_pollen_to_dataframe(df, pollen_species_list, genus_column="GENUS_NAME", species_column="SPECIES_NAME"):
    """
    Adds a 'HAS_POLLEN' column to the DataFrame indicating if the species produces pollen.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with genus and species columns.
    - genus_column (str): Column name for genus. Default is "GENUS_NAME".
    - species_column (str): Column name for species. Default is "SPECIES_NAME".
    - pollen_species_list (list): List of scientific names (genus + species) that produce pollen.

    Returns:
    - pd.DataFrame: DataFrame with the new 'HAS_POLLEN' column.
    """
    df_copy = df.copy()
    
    df_copy['SCIENTIFIC_NAME'] = (df_copy[genus_column].str.capitalize() + ' ' + df_copy[species_column].str.lower()).str.replace(' xx|x', '', regex=True).str.strip().str.replace(" ", "_")
    df_copy['HAS_POLLEN'] = df_copy['SCIENTIFIC_NAME'].isin(pollen_species_list)
    
    return df_copy.drop(columns=['SCIENTIFIC_NAME'])

def add_has_pollen_to_cleaned(file_path, df_with_has_pollen):
    """
    Adds HAS_POLLEN to the processed CSV by merging on TREE_ID.
    If HAS_POLLEN already exists, it is replaced with new values.
    
    Parameters:
        file_path (str): Path to the processed CSV file.
        df_with_has_pollen (pd.DataFrame): DataFrame containing TREE_ID and HAS_POLLEN.
    
    Returns:
        None: Updates the CSV file in place.
    """
    df_cleaned = pd.read_csv(file_path)

    # If HAS_POLLEN exists, drop it and add the new values
    if 'HAS_POLLEN' in df_cleaned.columns:
        print("HAS_POLLEN already exists. Replacing the column.")
        df_cleaned = df_cleaned.drop(columns=['HAS_POLLEN'])
    
    df_selected = df_with_has_pollen[['TREE_ID', 'HAS_POLLEN']]

    # Merge the has_pollen values on TREE_ID and add them to df_cleaned
    df_cleaned = df_cleaned.merge(df_selected, on="TREE_ID", how="right")

    # Save the updated dataframe to the CSV
    df_cleaned.to_csv(file_path, index=False)
    
    print("HAS_POLLEN replaced in the CSV.")