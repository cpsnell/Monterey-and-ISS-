import requests
import reverse_geocode
from reverse_geocode import search
from haversine import haversine
from geopy import distance
#from geopy.distance import haversine
from geopy.distance import geodesic # More accurate for ellipsoidal Earth

#Monterey
point1 = (36.5973, -121.8978) # (latitude, longitude)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    print("Likely an error")

print("International Space Station Coordinates:")
print(response.json()["iss_position"])

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
#print(longitude)
#print(latitude)
point2 = (float(latitude), float(longitude))

print(f"Haversine distance between Monterey and the ISS: {haversine(point1, point2,unit='km'):.2f} km")
#print(f"Geodesic distance between Monterey and the ISS: {geodesic(point1, point2).km:.2f} km")


#api.kanye.rest
#sunrise-sunset.org

#https://api.sunrise-sunset.org/json

