import requests
import json
import pandas as pd
from shapely.geometry import Point, Polygon
from scipy.spatial import cKDTree


def get_boundary_by_way_id(way_id):
    """
    Fetches the boundary coordinates for a given Way ID using the Overpass API and returns them as a list.

    Parameters:
    - way_id (int): The ID of the Way whose boundary we want to fetch.

    Returns:
    - Optional[List[dict]]: A list of coordinate dictionaries with longitude and latitude if the request is successful, 
      or None if there is an error or no coordinates are found.
    """
    
    url = "https://overpass-api.de/api/interpreter"
    
    # Define the Overpass query with the given Way ID
    query = f"""
    [out:json];
    way({way_id});  // Input Way ID for the boundary
    out geom;
    """
    
    try:
        response = requests.post(url, data={'data': query})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
    data = response.json()
    coordinates = []
    
    for element in data['elements']:
        if 'type' in element and element['type'] == 'way':
            if 'geometry' in element:
                coordinates = [(coord['lon'], coord['lat']) for coord in element['geometry']]
                break  # Take the first valid geometry (the way itself)
    
    if coordinates:
        return coordinates
    else:
        print("No coordinates found or an error occurred.")
        return None


def create_park_polygon_from_coordinates(coordinates, buffer_distance=0.01):
    """
    Creates a Shapely Polygon object from a list of coordinates and adds a buffer to allow points slightly outside the park boundary.

    Parameters:
    - coordinates (List[Tuple[float, float]]): List of tuples containing (longitude, latitude) pairs.
    - buffer_distance (float): The distance to buffer the polygon by (in degrees). Default is 0.001.

    Returns:
    - Polygon: A Shapely Polygon object with a buffer representing the park boundary.
    """
    # Create the park polygon from the coordinates
    park_polygon = Polygon(coordinates)
    
    # Apply a buffer to expand the polygon by a certain distance
    buffered_polygon = park_polygon.buffer(buffer_distance)
    
    return buffered_polygon


def assign_neighborhood_to_points(df, park_polygon, neighborhood_name):
    """
    Function to check if a point is inside the park and update the neighborhood name.

    Parameters:
    df (pandas.DataFrame): DataFrame containing columns 'LONGITUDE', 'LATITUDE', and 'NEIGHBOURHOOD_NAME'.
    park_polygon (shapely.geometry.Polygon): Polygon representing the park boundary.
    neighborhood_name (str): The neighborhood name to assign when the point is inside the park. Default is "STANLEY PARK".

    Returns:
    pandas.DataFrame: Updated DataFrame with neighborhood names assigned.
    """
    
    def assign_neighborhood(row, park_polygon, neighborhood_name):
        if pd.isna(row['NEIGHBOURHOOD_NAME']):
            point = Point(row['LONGITUDE'], row['LATITUDE'])  
            if park_polygon.contains(point): 
                return neighborhood_name
        return row['NEIGHBOURHOOD_NAME'] 

    df['NEIGHBOURHOOD_NAME'] = df.apply(assign_neighborhood, axis=1, park_polygon=park_polygon, neighborhood_name=neighborhood_name)
    
    return df


def assign_neighborhood_using_knn(new, k=10):
    """
    Assigns the neighborhood names to the rows with missing values by using KNN (k-nearest neighbors).
    
    Parameters:
    - new (pandas.DataFrame): The DataFrame containing the tree data, with columns 'LATITUDE', 'LONGITUDE', and 'NEIGHBOURHOOD_NAME'.
    - k (int): The number of nearest neighbors to consider for assigning the neighborhood name (default is 10).
    
    Returns:
    - pandas.DataFrame: The updated DataFrame with neighborhood names assigned to the previously missing rows.
    """
    
    # Separate rows with known and unknown NEIGHBOURHOOD_NAME
    known_df = new[new['NEIGHBOURHOOD_NAME'].notna()]  # Rows with known neighborhood names
    unknown_df = new[new['NEIGHBOURHOOD_NAME'].isna()]  # Rows with missing neighborhood names
    
    # Create a KDTree from the known points
    known_coords = known_df[['LATITUDE', 'LONGITUDE']].values
    tree = cKDTree(known_coords)
    
    # Get coordinates for unknown points
    unknown_coords = unknown_df[['LATITUDE', 'LONGITUDE']].values
    
    # Query the k nearest neighbors for each unknown point
    distances, indices = tree.query(unknown_coords, k=k)
    
    # Function to get the most frequent neighborhood name
    def get_most_frequent_neighborhood(indices):
        # Extract neighborhood names of the k nearest neighbors
        neighbor_names = known_df.iloc[indices]['NEIGHBOURHOOD_NAME']
        # Return the most frequent name
        return neighbor_names.mode()[0]  # mode() gives the most frequent value
    
    # Assign the most frequent neighborhood name to each unknown point using .loc to avoid warnings
    unknown_df.loc[:, 'NEIGHBOURHOOD_NAME'] = [get_most_frequent_neighborhood(idx_list) for idx_list in indices]
    
    # Update the original DataFrame with the new values
    new.update(unknown_df[['TREE_ID', 'NEIGHBOURHOOD_NAME']])  # Updates only the NaN rows in the original DataFrame
    
    return new