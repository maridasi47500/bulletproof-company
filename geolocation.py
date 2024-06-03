from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
from geopy.exc import GeocoderTimedOut
class Geolocation():
    def __init__(self,place_type,search_radius):
            print("==geolocation==")
            self.place_type=place_type
            self.search_radius=search_radius
    def do_geocode(address, attempt=1, max_attempts=5):
            geolocator = Nominatim(user_agent="nearby_search")
            try:
                 print("search",str(address),"nearby")
                 return geolocator.geocode(address,exactly_one=False,limit=None,timeout=15)
            except GeocoderTimedOut:
                 print("timeout",attempt)
                 if attempt <= max_attempts:
                      return self.do_geocode(address, attempt=attempt+1)
                 raise
    def find_nearby_places(self,lat, lon, place_type, radius):
            geolocator = Nominatim(user_agent="nearby_search")
            location = geolocator.reverse((lat, lon),timeout=15)
            print(f"\nYour current location: {location}\n")
            query = f"{place_type} near {lat}, {lon}"
            print(query)
            myplaces=[]
            try:
                #places = self.do_geocode(query)
                places=geolocator.geocode(query,exactly_one=False,limit=None,timeout=15)
                if places:
                    for place in places:
                        print("resultat",place.address)
                        place_coords = (place.latitude, place.longitude)
                        place_distance = geodesic((lat, lon), place_coords).kilometers
                        if place_distance <= radius:
                            print(f"{place.address} ({place_distance:.2f} km)")
                            myplaces.append({"address":place.address,"distance":place_distance,"lat":place.latitude,"lon":place.longitude})
                else:
                    print("No nearby places found for the given type.")
                return myplaces
            except Exception as e:
                print("Error: Unable to fetch nearby places.",e)
                return myplaces
    def geolocate(self,user_lat,user_lon):
            if user_lat is not None and user_lon is not None:
                place_type = self.place_type#input("What type of place are you looking for? (e.g., park, mall, ATM, hotel): ")
                search_radius = self.search_radius# float(input("Enter the search radius (in kilometers): "))
                x=self.find_nearby_places(float(user_lat), float(user_lon), place_type, search_radius)
                print(len(x))
                return x
