from pyqgis_scripting_ext.core import *


HMap.remove_layers_by_name(['OpenStreetMap'])
HMap.remove_layers_by_name(['ne_50m_populated_places'])
HMap.remove_layers_by_name(['ne_50m_admin_0_countries']) #otherwise there would be many layers, as we run it each time and create new layers...name from layerspanel

folder = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/"
geopackagePath = folder + "natural_earth_vectors.gpkg"
countriesNames = "ne_50m_admin_0_countries"
citiesNames = "ne_50m_populated_places"

osm = HMap.get_osm_layer()

HMap.add_layer(osm) #HMap is the map of QGIS so you can add izt to ypur project

#load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesNames)
citiesLayer = HVectorLayer.open(geopackagePath, citiesNames)
HMap.add_layer(countriesLayer)
HMap.add_layer(citiesLayer)
 


nameIndex_c = citiesLayer.field_index("NAME")
print(nameIndex_c)
locIndex = citiesLayer.field_index("SOV0NAME")
print(locIndex)



countriesFeatures = countriesLayer.features()
citiesFeatures = citiesLayer.features()

frenchCities = []

for feature in citiesFeatures:
    name = feature.attributes[locIndex]
    # print(name)
    if name == "French Republic":
        print(feature.attributes[nameIndex_c], "is a city of France")
        frenchCities.append(feature.attributes[nameIndex_c])
print("there are", len(frenchCities), "big cities in France")
 