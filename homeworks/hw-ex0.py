
import pip
pip.main(['install', 'pyqgis-scripting-ext'])

from pyqgis_scripting_ext.core import *

#exercise0

file = '/Users/paulaschmidl/Desktop/GIS/02_exe0_geometries.csv'

with open (file, 'r') as file:
    lines = file.readlines()
    print(lines)

coordinates = []   

for line in lines:
    thick = int(line.split(';')[2])
    coords = line.split(';')[1].split()
    type = line.split(';')[0] 
    
    print(coords)
    
    c = 0
    for i in coords:
         coordinate = float(i.split(',')[c])
         c+=1
    
    
 
    
    
        
    
    
    
    
    
'''if type == "polygon":
        k = HPolygon.fromCoords(value)
    elif type == "line":
        k = HLineString.fromCoords(value)
    elif type == "point":
        #k = HPoint(value.strip('[]'))#problem: coord in []
        print("point")
'''