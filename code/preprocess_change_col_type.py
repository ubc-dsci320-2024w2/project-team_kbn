import pandas as pd

def convert_categorical(df, columns):
    df[columns] = df[columns].apply(pd.Categorical)
    return df

def convert_ordinal(df, column, order=None):
    if order:
        df[column] = pd.Categorical(df[column], categories=order, ordered=True)
    else:
        df[column] = pd.Categorical(df[column])
    return df

def convert_dates(df, columns):
    df[columns] = pd.to_datetime(df[columns], errors='coerce', dayfirst=True) 
    return df

def convert_quantitative(df, columns):
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    return df

# the one shot function if too lazy to do all of the above.

def convert_column_types(df):
    
    categorical_columns = [
        'CIVIC_NUMBER', 'STD_STREET', 'GENUS_NAME', 'SPECIES_NAME', 'CULTIVAR_NAME',
        'COMMON_NAME', 'ON_STREET_BLOCK', 'ON_STREET', 'NOMENCLATURE', 'ON_ADDRESS', 'FAMILY_NAME'
    ]
    
    ordinal_columns = ['HEIGHT_RANGE_ID', 'HEIGHT_RANGE']
    
    height_range_order = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '>90']
    
    quantitative_columns = ['DIAMETER', 'LATITUDE', 'LONGITUDE']
    
    date_columns = 'DATE_PLANTED'
    
    # Apply conversions
    df = convert_categorical(df, categorical_columns)
    df = convert_ordinal(df, 'HEIGHT_RANGE', height_range_order)
    df = convert_quantitative(df, quantitative_columns)
    df = convert_dates(df, date_columns)
    
    return df