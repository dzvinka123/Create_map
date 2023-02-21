from haversine import haversine
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import argparse
import folium
from folium import plugins
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("dataset", type= str)
parser.add_argument("year", type = int)
parser.add_argument("longtitude", type=float)
parser.add_argument("latitude", type=float)

args = parser.parse_args()
path = args.dataset
year = args.year
latitude = args.latitude
longtitude = args.longtitude

def check_input(path, year, latitude, longtitude):
    if os.path.isfile(path) and 1860 < year < 2023 and longtitude <= 180 and longtitude >= - 180 and \
        latitude <= 90 and longtitude >= - 90:
        return True
    else:
        return False

def read_file(path: str, year: int) -> dict:
    """
    Function for reading txt file and convert info into dictionary
    Key - year, value - location
    """
    with open(path, "r", encoding="utf-8") as file:
        dictionary = []
        for element in file.read().splitlines()[13:]:
            if f"({year})" in element:
                if "(" in element.split("\t")[-1]:
                    dictionary.append(element.split("\t")[-2])
                else:
                    dictionary.append(element.split("\t")[-1])
    return dictionary

# print(read_file("location.list.txt", 2016))

def get_location(dictionary):
    need_location = []
    geolocator = Nominatim(user_agent="dell")
    for point in dictionary:
        for place in point.split(","):
            location = geolocator.geocode(place, timeout=200)
            if location != None:
                need_location.append((place, location.latitude, location.longitude))
                break
    return need_location

# print(get_location(read_file("location.list.txt", 2016)))

def get_haversine(location, people_place):
    distance = [(element, haversine(element[1:], people_place)) for element in location]
    distance = sorted(distance, reverse= False, key=lambda item: item[1])[:10]
    map_location = [item[0] for item in distance]
    return map_location
# print(get_haversine(get_location(read_file("location.list.txt", 2016)),(47.8507859, 35.1182867)))

def create_map(cordinate_near, latitude, longtitude):

    map = folium.Map(tiles="Cartodb Positron", location=[latitude, longtitude], zoom_start=5)

    feature_group1 = folium.FeatureGroup(name='my_location')
    feature_group1.add_child(folium.Marker(location= [latitude, longtitude], popup= "HOME", tooltip = "Click",
                                    icon=folium.Icon(color='black', icon='home')))

    feature_group2 = folium.FeatureGroup(name='Film_location')
    for item in cordinate_near: # rewrite into needed list
        feature_group2.add_child(folium.Marker(location=[item[1], item[2]], popup= item[0], tooltip = "Click",
                                    icon=folium.Icon(color='lightblack', icon='film')))
    map.add_child(feature_group1)
    map.add_child(feature_group2)

    folium.raster_layers.TileLayer("CartoDB Positron").add_to(map)
    folium.raster_layers.TileLayer('Stamenterrain').add_to(map)
    folium.LayerControl().add_to(map)
    plugins.MiniMap(tile_layer="Stamen Toner").add_to(map)
    map.save("Map_.html")
print(create_map([('Fishers Island', , -72.0239626), (' Hollywood', 34.0980031, -118.329523), ('Los Angeles', 34.0536909, -118.242766), ('England', 52.5310214, -1.2649062), ('Liberia', 5.7499721, -9.3658524), ('Dallas', 32.7762719, -96.7968559), ('Uruapan', 19.4060961, -102.03430719292024), ('Liège', 50.6450944, 5.5736112)], 47.8507859, 35.1182867)))




def main(path, year, latitude, longtitude):
    if check_input(path, year, latitude, longtitude):
        location = read_file(path, year)
        cordinat_near = get_location(location)
        result = get_haversine(cordinat_near, (latitude, longtitude))
        create_map(result, latitude, longtitude)
        return result
    else:
        raise ValueError("Please enter correct input")

# main(path, year, latitude, longtitude)

# print(create_map([('Fishers Island', , -72.0239626), (' Hollywood', 34.0980031, -118.329523), ('Los Angeles', 34.0536909, -118.242766), ('England', 52.5310214, -1.2649062), ('Liberia', 5.7499721, -9.3658524), ('Dallas', 32.7762719, -96.7968559), ('Uruapan', 19.4060961, -102.03430719292024), ('Liège', 50.6450944, 5.5736112)], 47.8507859, 35.1182867))
