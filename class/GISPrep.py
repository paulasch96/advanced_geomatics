#create a test

from pyqgis_scripting_ext.core import *


g1 = [[0,0],[5,0],[5,5],[0,5],[0,0]]
g2 = [[5,0],[7,0],[7,2],[5,2],[5,0]]
g3 = [4,1]
g4 = [5,4]
g5 = [[1,0],[1,6]]
g6 = [[3,3],[6,3],[6,6],[3,6],[3,3]]


G1 = HPolygon.fromCoords(g1)
G2 = HPolygon.fromCoords(g2)
G3 = HPoint(4,1)
G4 = HPoint(5,4)
G5 = HLineString.fromCoords(g5)
G6 = HPolygon.fromCoords(g6)


canvas = HMapCanvas.new()
canvas.set_extent([-1,-1,8,8])

canvas.add_geometry(G1,"black",1)
canvas.add_geometry(G2, "violet",1)
canvas.add_geometry(G3,"blue",1)
canvas.add_geometry(G4, "red",1)
canvas.add_geometry(G5,"green",1)
canvas.add_geometry(G6, "orange",1)


canvas.show()
