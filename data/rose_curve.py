#110424
#rose_curves
from math import cos,sin,radians
from pyqgis_scripting_ext.core import *


#define angle bc thats the only unknown variable
maxAngle = 360
n = 69
d = 20
points = []

for angle in range(0,100*maxAngle,1):
    radAngle = radians(angle)
    k=n/d
    r = cos(k*radAngle)
    x=r*cos(radAngle)
    y=r*sin(radAngle)

    
    point = [x,y]
    points.append(point)
    
print(points[2])

pointsLine = HLineString.fromCoords(points)
    

canvas = HMapCanvas.new()


canvas.set_extent(pointsLine.bbox())
canvas.add_geometry(pointsLine,"brown",0.5)
canvas.show()
    

