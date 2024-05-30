#Homework 28.04.2024

#import pip
#pip.main(['install', 'pyqgis-scripting-ext'])

from pyqgis_scripting_ext.core import *

#exercise0

file = '/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/02_exe0_geometries.csv'

with open (file, 'r') as file:
    lines = file.readlines()
   
for line in lines:
    line = line.strip()
    #print(line)
    
pts = []
lines1 = []
polys = []

for line in lines:
    line = line.strip()
    
    split = line.split(';')
    type = split[0]
    coords = split[1]
    num = split[2]
    
    if type == "point":
        cSplit = coords.split(',')
        x_coord = float(cSplit[0])
        y_coord = float(cSplit[1])
        point = HPoint(x_coord,y_coord)
        pts.append(point)
        print(pts)
    elif type == "line":
        Split = coords.split(' ')
        pointlist = []
        for coord in Split:
            split = coord.split(',')
            x_coord = float(split[0])
            y_coord = float(split[1])
            pointlist.append([x_coord, y_coord])
        line = HLineString.fromCoords(pointlist)
        lines1.append(line)
    elif type == "polygon":
        Split = coords.split(' ')
        pointlist = []
        for coord in Split:
            split = coord.split(',')
            x_coord = float(split[0])
            y_coord = float(split[1])
            pointlist.append([x_coord, y_coord])
        polygon = HPolygon.fromCoords(pointlist)
        polys.append(polygon)
        
canvas = HMapCanvas.new()
canvas.set_extent([-1,-1,50,50])
       
for point in pts:
    canvas.add_geometry(point,"magenta",50)
  

for line in lines1:
    canvas.add_geometry(line,"blue",3)

for polygon in polys:
   canvas.add_geometry(polygon,"red",1)
    





canvas.show()

    
            #line = H.LineString(pointlist)
        
        