from pyqgis_scripting_ext.core import *

#exercise 1 - UTM grid

map = HMapCanvas.new()
map.set_extent([0,0,60,30])


x = 0 #zone extend chosen by user
values = []

for i in range(60):
    x = x+1
    values.append(x)
    
world = [[0,0],[60,0],[60,30],[0,30],[0,0]]
World = HPolygon.fromCoords(world)
map.add_geometry(World,"red",1)
    
for j in values:
    meridian = [[j,0],[j,30]]
    

    Meridians = HLineString.fromCoords(meridian)
    

   
    map.add_geometry(Meridians,"red",1)

    map.show()