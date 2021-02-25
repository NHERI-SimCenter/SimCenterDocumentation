#pip install censusgeocode
import  censusgeocode as cg
res = cg.onelineaddress('1600 Pennsylvania Avenue, Washington, DC')
print("censusgeocode")
print(res)

import geocoder
arcgisEncoder = geocoder.arcgis('1600 Pennsylvania Avenue, Washington, DC')
print("\ngeocoder - arcgis")
print(arcgisEncoder.json)


osmEncoder = geocoder.osm('1600 Pennsylvania Avenue, Washington, DC')
print("\ngeocoder - osm (open street maps)")
print(osmEncoder.json)

#$ export GOOGLE_API_KEY=<Secret API Key>
#$ export GOOGLE_CLIENT=<Secret Client>
#$ export GOOGLE_CLIENT_SECRET=<Secret Client Secret>
print("\ngeocoder - google")
googleEncoder = geocoder.google('1600 Pennsylvania Avenue, Washington, DC')
print(googleEncoder.json)

