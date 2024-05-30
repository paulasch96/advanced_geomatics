from pyqgis_scripting_ext.core import *


file = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/22yr_T10MX"
folder = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/natural_earth_vector.gpkg"


crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

geopackagePath = folder 
countriesName = "ne_50m_admin_0_countries"

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

with open (file, 'r') as file:
    lines = file.readlines()
     
canvas = HMapCanvas.new() 
osm = HMap.get_osm_layer()
canvas.set_layers([osm])


#colortable

colors = ["lilac","purple","darkblue","darblue","blue","lightblue","turquoise","lightgreen","green","yellow","orange","red","brown"]


# copy starts here

country = "Germany"

nameIndex = countriesLayer.field_index("NAME")
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == country:
        countryGeom = feature.geometry
        countryGeom = crsHelper.transform(countryGeom)
        

canvas.set_extent(countryGeom.bbox())
canvas.add_geometry(countryGeom)



  
for line in lines[14:]:
    if line.startswith("#"):
        continue
    lineStrip = line.strip()
    lineSplit = lineStrip.split(' ')
    annualAverage = lineSplit[-1]
    if annualAverage == '':
        continue
    else: 
        annualAverage = float(lineSplit[-1])

    
  
    #print(annualAverage)
    
    Lon = float(lineSplit[0])
    Lat = float(lineSplit[1])

    coords = [[Lat, Lon],[Lat+1, Lon],[Lat+1, Lon+1],[Lat, Lon+1],[Lat, Lon]]
    polygon = HPolygon.fromCoords(coords)
    polygon = crsHelper.transform(polygon)
    
    if polygon.intersects(countryGeom):
        polygon = polygon.intersection(countryGeom)
        if annualAverage <= 2:
            colour = "darkblue"
        elif annualAverage >= 2 and  annualAverage < 4:
            colour = "blue"
        elif annualAverage >= 4 and  annualAverage < 5:
            colour = "green"
        elif annualAverage >= 5 and  annualAverage < 5.5:
            colour = "yellow"
        elif annualAverage >= 5.5 and annualAverage < 6:
            colour = "orange"
        elif annualAverage >= 6 and  annualAverage < 7:
            colour = "blue"
        elif annualAverage >= 7 and  annualAverage < 8:
            colour = "green"
        elif annualAverage >= 8 and  annualAverage < 9:
            colour = "yellow"
        elif annualAverage >= 10 and annualAverage < 11:
            colour  = "orange"
        elif annualAverage >= 11 and  annualAverage < 12:
            colour = "brown"
        elif annualAverage >= 12 and  annualAverage < 13:
            colour = "red"
        elif annualAverage >=13:
            colour = "black"
        
        canvas.add_geometry(polygon, colour)
        
        
    
    

canvas.show()