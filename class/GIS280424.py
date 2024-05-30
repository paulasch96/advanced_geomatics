from pyqgis_scripting_ext.core import *
point = HPoint(30.0,10.0)
print(point.asWkt())  #print as Well known text


coords = [[31,11],[10,30],[20,40],[40,40]]
line = HLineString.fromCoords(coords)
print(line.asWkt())




coords = [[32,12],[10,20],[20,39],[40,49],[32,12]]
polygon = HPolygon.fromCoords(coords)
print(polygon)


exterioPoints = [[35,10],[10,20],[15,40],[45,45],[35,10]]
holePoints = [[20,30],[35,35],[30,20],[20,30]]
doughnut = HPolygon.fromCoords(exterioPoints)
holeRing = HLineString.fromCoords(holePoints)

doughnut.add_interior_ring(holeRing)

print(doughnut)



#multis

coords1 = [[10,40],[40,30],[10,30],[10,40]]
multipoints = HMultiPoint.fromCoords(coords1)
print(multipoints)

coords2 = [[40,40],[30,30],[40,20],[40,40]]
coords3 = [[20,20],[10,20],[10,10],[20,20]]
multilines = HMultiLineString.fromCoords([coords1, coords2])
print(multilines)


multiPolygon = HMultiPolygon.fromCoords([coords1, coords2, coords3])

subGeometries = multiPolygon.geometries()
colorList = ["red", "blue", "green"]

coordinates = polygon.coordinates()
'''for coord in coordinates:
    print(f"coord x = {coord[0]} / coord y = {coord[1]})'''

canvas = HMapCanvas.new()

#canvas.add_geometry(multipoints,"red",1)
#canvas.add_geometry(multilines, "violet",7)

#canvas.add_geometry(multiPolygon, "red",10)

#canvas.add_geometry(doughnut,"chocolate",2)
#canvas.add_geometry(point,"brown",4)
#canvas.add_geometry(polygon,"brown",10)



for i in range(len(subGeometries)):
    canvas.add_geometry(subGeometries[i], colorList[i])

canvas.set_extent([0,0,50,50])

canvas.show()

##create a test
g1 = [[0,0],[5,0],[5,5],[0,5],[0,0]]
g2 = [[5,0],[7,0],[7,2],[5,2],[5,0]]
g3 = [4,1]
g4 = [5,4]
g5 = [[1,0],[6,1]]
g6 = [[3,3],[6,3],[6,6],[3,6]]


G1 = HPolygon.fromCoords(g1)
G2 = HPolygon.fromCoords(g2)
G3 = HPoint.fromCoords(g3)
G4 = HPoint.fromCoords(g4)
G5 = HLineString.fromCoords(g5)
G6 = HPolygon.fromCoords(g6)



