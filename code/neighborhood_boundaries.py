import requests
import json
from shapely.geometry import Polygon


def fetch_and_save_localareaboundary_geojson(output_path, limit=22):
    """Fetches local area boundaries from Vancouver Open Data API and saves as GeoJSON."""
    url = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/local-area-boundary/records"
    params = {"limit": limit}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    data = response.json()
    geojson = {"type": "FeatureCollection", "features": []}
    
    for record in data.get("results", []):
        geometry = record.get("geom", {}).get("geometry")
        lon = record.get("geo_point_2d", {}).get("lon")
        lat = record.get("geo_point_2d", {}).get("lat")
        
        if geometry and lon is not None and lat is not None:
            feature = {
                "type": "Feature",
                "geometry": geometry,
                "properties": {"name": record.get("name"), "center_lon": lon, "center_lat": lat}
            }
            geojson["features"].append(feature)
    
    try:
        with open(output_path, "w") as f:
            json.dump(geojson, f, separators=(',', ':'))
        print(f"GeoJSON file '{output_path}' has been created.")
    except IOError as e:
        print(f"Error writing to file: {e}")


def create_geojson_feature(polygon_coords, name="", center_lon=None, center_lat=None):
    """Creates a GeoJSON Feature object from polygon coordinates."""
    if polygon_coords[0] != polygon_coords[-1]:
        polygon_coords.append(polygon_coords[0])
    
    return {
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": [polygon_coords]},
        "properties": {"name": name, "center_lon": center_lon, "center_lat": center_lat}
    }


def merge_geojsons(*geojsons):
    """Merges multiple GeoJSON FeatureCollections into one."""
    merged_features = []
    for geojson in geojsons:
        if geojson.get("type") == "FeatureCollection":
            merged_features.extend(geojson.get("features", []))
        elif geojson.get("type") == "Feature":
            merged_features.append(geojson)
        else:
            print("Invalid GeoJSON object skipped.")
    
    return {"type": "FeatureCollection", "features": merged_features}


def create_park_polygon_from_coordinates(coordinates):
    """Creates a Shapely Polygon from a list of coordinates."""
    return Polygon(coordinates)


def load_geojson(file_path):
    """Loads a GeoJSON file and returns its content as a Python dictionary."""
    with open(file_path, "r") as f:
        return json.load(f)


def save_geojson(data, file_path):
    """Saves GeoJSON data to a file with minimized size."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, separators=(',', ':'))
        print(f"GeoJSON file has been written to {file_path}.")
    except IOError as e:
        print(f"Error writing to file: {e}")


def filter_features_by_name(geojson, target_name):
    """Filters GeoJSON features by a specific name property."""
    filtered_features = [
        feature for feature in geojson.get("features", [])
        if feature.get("properties", {}).get("name") == target_name
    ]
    return {"type": "FeatureCollection", "features": filtered_features}


def get_boundary_by_way_id(way_id):
    """Fetches boundary coordinates for a given Way ID using Overpass API."""
    url = "https://overpass-api.de/api/interpreter"
    query = f"[out:json];way({way_id});out geom;"
    
    try:
        response = requests.post(url, data={'data': query})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
    data = response.json()
    for element in data['elements']:
        if element.get('type') == 'way' and 'geometry' in element:
            return [(coord['lon'], coord['lat']) for coord in element['geometry']]
    
    print("No coordinates found or an error occurred.")
    return None


def filter_out_west_point_grey(geojson_data):
    """Removes 'West Point Grey' features from the GeoJSON data."""
    filtered_features = [
        feature for feature in geojson_data['features']
        if feature['properties']['name'] != 'West Point Grey'
    ]
    return {"type": "FeatureCollection", "features": filtered_features}


def validate_and_buffer_polygon(polygon):
    """Validates and buffers a polygon if it is invalid."""
    return polygon.buffer(0) if not polygon.is_valid else polygon


def extract_boundary_coordinates(polygon):
    """Extracts boundary coordinates from a polygon (or MultiPolygon)."""
    if polygon.geom_type == 'MultiPolygon':
        combined_boundary_coordinates = []
        for poly in polygon.geoms:
            x, y = poly.exterior.xy
            combined_boundary_coordinates.extend(list(zip(x, y)))
        return combined_boundary_coordinates
    else:
        x, y = polygon.exterior.xy
        return list(zip(x, y))