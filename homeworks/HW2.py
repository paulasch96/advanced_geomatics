#exercise 1

import pip
pip.main(['install', 'pyqgis-scripting-ext'])

from pyqgis_scripting_ext.core import *

#load file

file = '/Users/paulaschmidl/Desktop/GIS/02_exe0_geometries.csv'

with open (file, 'r') as file:
    lines = file.readlines()
    print(lines)

#get values 
coordinates = []
for line in lines:
    line = line.split(';')
    type = line[0]
    coords = line[1]
    thickness = line[2]
    
    coord = coords.split() #list with all coords per item as str
    
    if type == point:
        for i in coord:
        x = float(i.split(',')[0])
        y = float(i.split(',')[1])
        coordinate = [x,y]
        
  
        
        
        coordinates.append(coordinate)
        
        
    
print(coordinates)
    

  

