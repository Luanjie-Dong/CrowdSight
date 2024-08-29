import plotly.express as px
import json
import random 
import math 
import folium
from folium.plugins import HeatMap  
import branca.colormap as cm

def create_map():
    # Load your GeoJSON file
    with open('data/sg-2008.geojson') as f:
        geojson_data_sg = json.load(f)

    """BASE LAYER"""
    # Initialize the map centered around the same coordinates with a similar zoom level
    m = folium.Map(location=[1.291648, 103.858459], zoom_start=15, tiles="cartodb positron")
    """"""

    """SITE MAP"""
    # Add the route as a line on the map from GeoJSON data
    for feature in geojson_data_sg['features']:
        if feature['geometry']['type'] == 'LineString':
            route = [(coord[1], coord[0]) for coord in feature['geometry']['coordinates']]
            folium.PolyLine(route, color='green', weight=5, opacity=0.7, popup=feature['properties']['Name']).add_to(m)
    """"""

    """MARKER LAYER"""
    ##MRT##
    mrt = {
        "City Hall": [1.293191026024169, 103.85165498556803],
        "Promenade": [1.2941545600857782, 103.86030346981188],
        "Esplanade": [1.2942208358078537, 103.8556156333854],
        "Nicoll Highway": [1.300926176540319, 103.8636853229336]
    }

    for station, coords in mrt.items():
        folium.Marker(
            location=coords,
            popup=station,
            icon=folium.Icon(color='black', icon='train', prefix='fa')
        ).add_to(m)
    ###END###
        
    ###BUS STOPS###
    bus_stops = {
        "Aft City Hall Stn Exit B": [1.2923858977559841, 103.85182924546],
        "Suntec City": [1.2961185801465722, 103.8579983262912]
    }

    for stop, coords in bus_stops.items():
        folium.Marker(
            location=coords,
            popup=stop,
            icon=folium.Icon(color='blue', icon='bus', prefix='fa')
        ).add_to(m)
    ###END###
        
    """HEATMAP LAYER"""
    # Add Cameras with continuous color scale based on density
    cameras = {
        "Gate 1": {
            "Lattitude": 1.299810,
            "Longitude": 103.862298,
            "Num_people": 240
        },
        "Gate 2": {
            "Lattitude": 1.291419,
            "Longitude": 103.860814,
            "Num_people": 100
        },
        "Gate 3A": {
            "Lattitude": 1.293067,
            "Longitude": 103.85422,
            "Num_people": 400
        },
        "Gate 3B": {
            "Lattitude":1.293668,
            "Longitude":103.854485,
            "Num_people":134
        }
    }

    locations= []
    radius = 0.0005  # Adjust the radius to control the spread of people around the point

    for info in cameras.values():
        lat_center = info['Lattitude']
        lon_center = info['Longitude']
        num_people = info['Num_people']
        
        for i in range(num_people):
            # Random angle and radius
            angle = random.uniform(0, 2 * math.pi)
            r = radius * math.sqrt(random.uniform(0, 1))  # Uniform distribution within the circle
            
            # Convert polar to Cartesian coordinates
            delta_lat = r * math.cos(angle)
            delta_lon = r * math.sin(angle)
            
            # Adjust delta_lon for latitude (longitude distortion near poles)
            delta_lon /= math.cos(math.radians(lat_center))
            
            # Calculate new latitude and longitude
            lat = lat_center + delta_lat
            lon = lon_center + delta_lon
            
            # Add to locations list
            locations.append([lat, lon])

    # Add heat map layer 
    HeatMap(locations, radius=10, gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(m) 

    # Add a colormap (color scale)
    colormap = cm.LinearColormap(
        colors=['blue', 'purple', 'orange', 'red'],
        vmin=0,
        vmax=1,
        caption='Density'  # Caption for the colormap
    )
    colormap.add_to(m)

    """"""
    m.save('static/map.html')

# This ensures that the function runs when the script is called directly
if __name__ == "__main__":
    create_map()

