from pyqgis_scripting_ext.core import *

crsHelper = HCrs()
crsHelper.from_srid(4326) #srid stands for a special reference system
crsHelper.to_srid(32632)

#--> now the helper can be used to transfrom geometrie

point4326 = HPoint(11,46)
point32632 = crsHelper.transform(point4326)

print(f"{point4326}-->{point32632}")


# OSM 3857 -> for UTM exercise (the original is 4326)

backTo4326 = crsHelper.transform(point32632, inverse = True) #back to 4326
print(backTo4326)
