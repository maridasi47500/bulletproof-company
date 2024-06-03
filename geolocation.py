from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
class Geolocation():
    def __init__(self,place_type,search_radius):
            print("==geolocation==")
            self.place_type=place_type
            self.search_radius=search_radius
    def find_nearby_places(lat, lon, place_type, radius):
            geolocator = Nominatim(user_agent="nearby_search")
            location = geolocator.reverse((lat, lon))
            print(f"\nYour current location: {location}\n")
                        
            query = f"{place_type} near {lat}, {lon}"
            try:
                places = geolocator.geocode(query, exactly_one=False, limit=None)
                if places:
                    for place in places:
                        place_coords = (place.latitude, place.longitude)
                        place_distance = geodesic((lat, lon), place_coords).kilometers
                        if place_distance <= radius:
                            print(f"{place.address} ({place_distance:.2f} km)")
                else:
                    print("No nearby places found for the given type.")
            except:
                print("Error: Unable to fetch nearby places.")
    def geolocate(self,user_lat,user_lon):
            if user_lat is not None and user_lon is not None:
                place_type = self.place_type#input("What type of place are you looking for? (e.g., park, mall, ATM, hotel): ")
                search_radius = self.search_radius# float(input("Enter the search radius (in kilometers): "))
                x=self.find_nearby_places(float(user_lat), float(user_lon), place_type, search_radius)
                print(x)
                return x
