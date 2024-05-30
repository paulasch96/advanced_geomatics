from pyqgis_scripting_ext.core import *

folder = "/Users/paulaschmidl/Desktop/GIS"


geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
#cleanup
HMap.remove_layers_by_name(["OpenStreetMap", countriesName,]) 

#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
HMap.add_layer(countriesLayer)

schema = {
    "cn": "string"
    
}

centroidsLayer = HVectorLayer.new("centroids", "Point", "EPSG:4326", schema)

i = 0
for country in countriesLayer.features():
    countriesLayerGeometry = countriesLayer.features()[i].geometry
    i+=1
    countryCentroids = countriesLayerGeometry.centroid
    cn = "NAME"

HMap.add_layer(centroidsLayer)    
centroidsLayer.add_feature(countryCentroids, ["cn"])