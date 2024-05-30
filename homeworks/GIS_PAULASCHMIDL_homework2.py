#Homework 28.04.2024

import pip
pip.main(['install', 'pyqgis-scripting-ext'])

from pyqgis_scripting_ext.core import *

#exercise0

file = '/Users/paulaschmidl/Desktop/GIS/02_exe0_geometries.csv'

with open (file, 'r') as file:
    lines = file.readlines()
    print(lines)

# Dieter version start
results = []
dict_res = {}

thickness = []

for line in lines:
    thick = int(line.split(';')[2])
    coord = line.split(';')[1].split()
    name = line.split(';')[0] + "_" + line.split(';')[2]
    name = name.strip()
    
    thickness.append(thick)
    
    #print(coord)
    
    # if line
    
    if len(coord)==1:
        res = coord[0].split(",")
        fin_res = [int(float(i)) for i in res]
        #print(fin_res)
        results.append(fin_res)
        dict_res[name] = fin_res
        
    elif len(coord)>1:
        
        res1 = []
        for i in coord:

            var = [int(i) for i in i.split(',')]
            #print(var)
            res1.append(var)
        results.append(res1)
        dict_res[name] = res1
        
            
            
        
    else:
        print("error")
    
    
print(dict_res)
#for key,value in dict_res.items():
    
    #print(dict_res[value])
canvas = HMapCanvas.new()
canvas.set_extent([0,0,50,50])

colors = ["pink","blue","red","red","blue"]
count = 0

for key,value in dict_res.items():
    
    type = key.split("_")[0]
    
    if type == "polygon":
        k = HPolygon.fromCoords(value)
    elif type == "line":
        k = HLineString.fromCoords(value)
    elif type == "point":
        #k = HPoint(value.strip('[]'))#problem: coord in []
        print("point")
  
#for key, value in dict_res.items():


    
    canvas.add_geometry(k, colors[count], thickness[count])
    count+=1

    canvas.show()

#would have been easier with several lists and not with dict!








