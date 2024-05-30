from pyqgis_scripting_ext.core import *

folder = "/Users/paulaschmidl/Desktop/GIS/"
geopackagePath = folder + "natural_earth_vectors.gpkg"
countriesNames = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
testName = "test"

osm = HMap.get_osm_layer()

#cleanup
HMap.remove_layers_by_name(['OpenStreetMap', citiesName, testName ]) #otherwise there would be many layers, as we run it each time and create new layers...name from layerspanel


HMap.add_layer(osm) #HMap is the map of QGIS so you can add izt to ypur project

#load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesNames)
#HMap.add_layer(countriesLayer)

#getschema
print("Schema")
counter = 0 
for name, type in countriesLayer.fields.items():
    counter += 1
    if counter < 6:
        print("\t", name, "of type", type)

#get CRS/coordRefSystem
crs = countriesLayer.prjcode
print("Projection is", crs)


#getboundaries
boundaries = countriesLayer.bbox()
print("the boundaries are", boundaries)

#get feature count
featurecount = countriesLayer.size()
print("Featurescount:", featurecount)

print("attributes for italy:")
nameIndex = countriesLayer.field_index("NAME")  #if there is no field called NAME it would print -1
#print(nameIndex)

countriesFeatures = countriesLayer.features()

for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "Italy":
        geometry = feature.geometry #this geometry can be used for buffers, intersections.....
        print("Geometry:", geometry.asWkt()[:90] + "...")
        
#USE FILTERS
expression = "NAME like 'I%' AND POP_EST > 3000000" #like is a bit like = 'I%' for everything starting with I pop_est is just an other column in the attribute table
filtered_countriesFeatures = countriesLayer.features(expression) #select by expression
count = 0
for feature in filtered_countriesFeatures:
    print(feature.attributes[nameIndex])
    count += 1
    
print("Feature count with Filter", count)

#BOUNDINGBOX FILTER

lon = 11.119982
lat = 46.080428
point = HPoint(lon,lat)
buffer = point.buffer(2)#2 degrees wich is in our region aboout 200kmc
citiesLayer = HVectorLayer.open(geopackagePath, citiesName) #to open the layer of the gpckg
HMap.add_layer(citiesLayer)

citiesNameIndex = citiesLayer.field_index("NAME")
aoi = buffer.bbox()

count = 0 
for feature in citiesLayer.features(bbox=aoi): #use bbox as an expression, bbox is always the min rectangle so its bigger than the buffer/radius
    count +=1
    print(feature.attributes[citiesNameIndex])
print ("Cities festures listed:", count)


count= 0
for feature in citiesLayer.features(geometryfilter=buffer): #use geometryfilter as an expression
    count +=1
    print(feature.attributes[citiesNameIndex])
print ("Cities festures listed:", count)



#CREATE DATA

#create a schema
fields = {
    "id": "Integer",
    "name": "String"
}
just2citiesLayer = HVectorLayer.new("test", "Point", "EPSG:4326", fields) #"name of layer", "geometrytype","CRS", "schema"

just2citiesLayer.add_feature(HPoint(-122.42,37.78), [1, "San Francisco"]) #add Point/geometry and fields, crs and layername stay the same
just2citiesLayer.add_feature(HPoint(-73.98, 40.47), [2, "NewYork"])

path = folder + "test.gpkg"
error = just2citiesLayer.dump_to_gpkg(path, overwrite=True) #overwirte true --> will start gpkg from scratch, if you want  to insert a layer to the same gpkg overwrite = false
if error:   #error is NONE if there is no error
    print(error)
#when dumped to gpkg its not a temporary file anymore
#HMap.add_layer(just2citiesLayer) ---> just a temporary layer

testLayer = HVectorLayer.open(path, "test")
HMap.add_layer(testLayer)

fields ={
    "name": "String",
    "population":"Integer",
    "lat": "Double",
    "lon": "Double"

}

oneCityMoreAttributes = HVectorLayer.new("test2", "Point", "EPSG:4326", fields) #"name of layer", "geometrytype","CRS", "schema"

oneCityMoreAttributes.add_feature(HPoint(-73.98, 40.47), ["New York", 19040000, 40.47, -73.98])


#dumping it into tghe same gpkg, but to the "test" gpkg. to see it you need to drag it to the layers panel and then you can choose between test and test2

error = oneCityMoreAttributes.dump_to_gpkg(path, overwrite=False)

if error:
    print(error)
    
    































