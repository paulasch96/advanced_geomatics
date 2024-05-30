from pyqgis_scripting_ext.core import *

HMap.remove_layers_by_name(['OpenStreetMap'])
HMap.remove_layers_by_name(['stationsLayer'])

file = "/Users/paulaschmidl/Desktop/GIS/EX0-4_SCHMIDL_PAULA/stations.txt"
folder = "/Users/paulaschmidl/Desktop/GIS/"

with open (file, 'r') as file:
    lines = file.readlines()
    
for line in lines[65:73]:
    print(line)
    
osm = HMap.get_osm_layer()
HMap.add_layer(osm)



#create schema
schema = {

    "STAID": "Integer",
    "STANAME":"String",
    "CN": "String",
    "LAT": "Float",
    "LON": "Float",
    "HGHT": "Integer"
}

stations = HVectorLayer.new("stationsLayer", "Point", "EPSG:4326", schema) #"name of layer", "geometrytype","CRS", "schema"


#convert degree to decimal data


for line in lines[1:]: #removed the first line because it was titles
    line = line.strip()
    # print(line)
    lineSplit = line.split(",")
    staname = lineSplit[1]
    staid = lineSplit[0]
    cn = lineSplit[2]
    hght = lineSplit[5]
    lat = lineSplit[3].strip("+")
    lon = lineSplit[4].strip("+")
    latSplit = lat.split(":")
    lonSplit = lon.split(":")
    
    convLat1 = float(latSplit[1])/60
    convLon1 = float(lonSplit[1])/60
    convLat2 = float(latSplit[2])/3600
    convLon2 = float(lonSplit[2])/3600
    
    latfinal = float(latSplit[0]) + convLat1 + convLat2
    lonfinal = float(lonSplit[0]) + convLon1 + convLon2
    

    point = HPoint(lonfinal, latfinal)

    

    #add data


    stations.add_feature(point, [staid, staname, cn, latfinal, lonfinal, hght])
    
newpath = folder + "stationsLayer.gpkg"

error = stations.dump_to_gpkg(newpath, overwrite=True) 
if error:   
    print(error)

new_stationsLayer = HVectorLayer.open(newpath, "stationsLayer")
HMap.add_layer(new_stationsLayer)
    


