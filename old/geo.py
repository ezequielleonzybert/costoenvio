from geopy.geocoders import Nominatim
from functools import partial

query = input()
geolocator = Nominatim(user_agent="costoenvio")
results = geolocator.geocode(query, exactly_one=False)

print(len(results))
print(results)