from pyqgis_scripting_ext.core import *

#covid data
folder = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/" 
coviddata = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/dpc-covid19-ita-regioni.csv"
provinces = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/natural_earth_vector.gpkg"
provincesName = "ne_10m_admin_1_states_provinces"
HMap.remove_layers_by_name(['OpenStreetMap', provincesName])

osm = HMap.get_osm_layer()

HMap.add_layer(osm) 



provincesLayer = HVectorLayer.open(provinces, provincesName)
HMap.add_layer(provincesLayer)

provincesLayer.subset_filter("admin = 'Italy'") #just show those features that are obeying to th filter



regionIndex = provincesLayer.field_index("region") 
provinceIndex = provincesLayer.field_index("name")

regionsFeatures = provincesLayer.features()


 #create regions layer and dump it to gpkg
     
fields = {
    "region": "String",
    "province": "String"
}

regionsLayer = HVectorLayer.new("regions", "MultiPolygon", "EPSG:4326",fields)


for feature in regionsFeatures:
     regions = feature.attributes[regionIndex] #regions is a "list "of all regions
     provinces = feature.attributes[provinceIndex]
     geometry = feature.geometry
     
     regionsLayer.add_feature(geometry, [regions, provinces])
     
HMap.add_layer(regionsLayer)

path = folder + "regions.gpkg"
error = regionsLayer.dump_to_gpkg(path, overwrite = True)

if error:
    print(error)
    
    


#combine provinces to regions

