#create a test

from pyqgis_scripting_ext.core import *


G1 = HPolygon.fromCoords([[0,0],[5,0],[5,5],[0,5],[0,0]])
G2 = HPolygon.fromCoords([[5,0],[7,0],[7,2],[5,2],[5,0]])
G3 = HPoint(4,1)
G4 = HPoint(5,4)
G5 = HLineString.fromCoords([[1,0],[1,6]])
G6 = HPolygon.fromCoords([[3,3],[6,3],[6,6],[3,6],[3,3]])

print("polygon boundingbox:", G1.bbox())

print("polygon length:", G1.length())
print("polygon area:", G1.area())

print("line length:", G5.length())
print("line area:", G5.area())

print("pt length:", G3.length())
print("pt area:", G3.area())

print("dist btw line and pt:", G5.distance(G3))



#PREDICATES

#intersects

print("does G1 intersect G2?", G1.intersects(G2))
print(G1.intersects(G3))
print(G1.intersects(G4))
print(G1.intersects(G5))
print(G1.intersects(G6))

#touches -- touches at least one point, but not the interior


print("does G1 touch G2?", G1.touches(G2))
print(G1.touches(G3))
print(G1.touches(G4))
print(G1.touches(G5))
print(G1.touches(G6))

#contains --> one shape is completely inside the other one

print("does G1 contain G2?", G1.contains(G2))
print(G1.contains(G3))
print(G1.contains(G4))
print(G1.contains(G5))
print(G1.contains(G6))

#FUNCTIONS --> returns an actual geometry, either point, line or poly depending on what is intersecting

print("intersection")
print(G1.intersection(G2))
print(G1.intersection(G3))
print(G1.intersection(G4))
print(G1.intersection(G6))

print("symdifference") #--> opposite of intersect, returning all the area that is not intersecting. only homogenuous if junction is broad enough. might return multipolygon
print(G1.symdifference(G2))
print(G1.symdifference(G3))
print(G1.symdifference(G4))
print(G1.symdifference(G6))


print("union") #--> unites/merges the two polygons to one
print(G1.union(G2))
print(G1.union(G3))
print(G1.union(G4))
print(G1.union(G6))


print("difference") #--> like a.minus(b). so the order of the geometries is important
print(G1.difference(G2))
print(G1.difference(G3))
print(G1.difference(G4))
print(G1.difference(G6))
print(G6.difference(G1))


print("buffers") #--> enlarging it in each direction
b0 = (G1.buffer(1))
b0_5 = (G3.buffer(3))
b1 = (G1.buffer(1,1))#--> the second valuze gives the precision of the circle (in computers a circle is never perfectly round. the defaultz value is 8)
b2 = G5.buffer(1) #lines get a rounded buffer at the ends
b3 = G5.buffer(1,-1, JOINSTYLE_ROUND, ENDCAPSTYLE_ROUND) #-1 = don use it/ use default
b4 = G5.buffer(1,-1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE) #-1 = don use it/ use default


print("")
collection = HGeometryCollection([G1,G2,G3,G4,G5,G6])
hull = collection.convex_hull() #hull cna be used to set extent: canvas.set_extent(hull.bbox())

canvas = HMapCanvas.new()
canvas.set_extent(hull.bbox())

canvas.add_geometry(G1,"black",1)
canvas.add_geometry(G2,"black",1)
canvas.add_geometry(G3,"black",1)
canvas.add_geometry(G4,"black",1)
canvas.add_geometry(G5,"black",1)
canvas.add_geometry(G6,"black",1)
canvas.add_geometry(hull,"beige",1)

#canvas.add_geometry(G1,"black",1)
#canvas.add_geometry(G2, "violet",1)
#canvas.add_geometry(G3,"blue",1)
#canvas.add_geometry(G4, "red",1)
#canvas.add_geometry(G5,"green",1)
#canvas.add_geometry(G6, "orange",1)
#canvas.add_geometry(b2)
#canvas.add_geometry(b3)
#canvas.add_geometry(b4)


#canvas.add_geometry(G1.intersection(G6), 'magenta', 5)
#canvas.add_geometry(G1.symdifference(G6), 'green', 5)
#canvas.add_geometry(G1.difference(G6), 'orange', 5)
#canvas.add_geometry(G3.buffer(1), 'magenta', 1)
#canvas.add_geometry(G3.buffer(1,1), 'green',1)


canvas.show()
