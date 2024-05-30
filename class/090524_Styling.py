from pyqgis_scripting_ext.core import *

folder = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/"
geopackagePath = folder + "natural_earth_vectors.gpkg"
countriesNames = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"
tmpFolder = f"{folder}/tmp/"

#cleanup
HMap.remove_layers_by_name(['OpenStreetMap', citiesName, countriesNames ]) #otherwise there would be many layers, as we run it each time and create new layers...name from layerspanel

osm = HMap.get_osm_layer()

HMap.add_layer(osm) 



citiesLayer = HVectorLayer.open(geopackagePath, citiesName)

#CitiesLayer

citiesLayer.subset_filter("SOV0NAME = 'Italy'") #just show those features that are obeying to th filter

pointStyle = HMarker("square",5,45) + HFill("red") + HStroke("black", 1) #3 argumnets: geom, size, rotation, 0,255,0 (RGB) is green (you can look it up on intscape, 128 is transparency, must be between 0 and 255 in this cas32

field = "NAME"

#pointStyle += HLabel(field, yoffset =-15, xoffset = 15) + HHalo("white",1)#field,  yoffset,... halo = buffer

field = "if(POP_MAX > 1000000, concat(NAME, ' (',round(POP_MAX/1000000,1),')'), NAME)" #if(expression,iftrue,else), concat takes several strings and takes them together

labelProperties = {
    "font": "Arial",
    "color": "black",
    "size": 10,
    "field": field,
    "xoffset": 0,
    "yoffset": -10
}

pointStyle += HLabel(**labelProperties) +  HHalo("white",1)  # ** take the dictonary and expand it so that it is equivalet to HLabel(font='Arial',color='black',...)


citiesLayer.set_style(pointStyle)



#PolygonLayer
countriesLayer = HVectorLayer.open(geopackagePath, countriesNames)
countriesLayer.subset_filter("NAME = 'Italy'")
italyGeometry = countriesLayer.features()[0].geometry


polygonStyle = HFill("0,255,0,100") + HStroke("green",2)
countriesLayer.set_style(polygonStyle)


#linesLayer

riversLayer = HVectorLayer.open(geopackagePath, riversName)
riversLayerItaly = riversLayer.sub_layer(italyGeometry, "rivers_italy", ['scalerank','name'])  #qgis doesmz allow sub set with geometries. but you can do so and get a new layer. boundary, new layer name, s



#THEMATIC STYLING
#list of lists for ranges. later on we will make a list of styles for these ranges
ranges = [
    [0,0],
    [1,5],
    [6,7],
    [8,9],
    [10,11],
]

styles = [
    HStroke("blue",7),
    HStroke("blue",5),
    HStroke("blue", 2),
    HStroke("darkblue", 2),
    HStroke("darkblue",1)
]

labelProperties = {
    "font": "Arial",
    "color": "blue",
    "size": 14,
    "field": 'name',
    "along_line": True,
    "bold": True,
    "italic": True
    
}

labelStyle = HLabel(**labelProperties) +HHalo("white",1)


riversLayerItaly.set_graduated_style('scalerank', ranges, styles, labelStyle )

# lineStyle = HStroke("blue",2)
# riversLayerItaly.set_style(lineStyle)


#lineStyle += labelStyle
# riversLayerItaly.set_style(lineStyle)

HMap.add_layer(countriesLayer)

HMap.add_layer(citiesLayer)

HMap.add_layer(riversLayerItaly)

#making a layout
printer = HPrinter(iface)
#default layout is a4 landscape
mapProperties = {
    "x": 5, #x ynd y give you the position
    "y": 25,
    "width": 285, #size of the map on the layout
    "height": 180,
    "extent": [10,44,12,46],#bounding box you could get from layers, what part of the world/map
    "frame": True
}

printer.add_map(**mapProperties)

outputPdf = f"{tmpFolder}/test.pdf"
printer.dump_to_pdf(outputPdf)

outputPng





