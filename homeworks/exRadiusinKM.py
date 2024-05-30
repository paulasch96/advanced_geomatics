from pyqgis_scripting_ext.core import *
#necessary functions
#(with splitting and not slicing you could have made one function for lat and lon


def fromLatString(latStr):
    sign = latStr[0]
    latDegrees = float(latStr[0:3]) #from 0 incl to 2 so 1-3 without 4th
    latMin = float(latStr[4:6])
    latSec = float(latStr[7:9])
    lat = latDegrees + latMin/60 + latSec/3600
    if sign == '-':
        lat = lat * -1
    
    return lat
    
def fromLonString(lonStr):
    sign = lonStr[0]
    lonDegrees = float(lonStr[0:4]) #from 0 incl to 2 so 1-3 without 4th
    lonMin = float(lonStr[5:7])
    lonSec = float(lonStr[8:10])
    lon = lonDegrees + lonMin/60 + lonSec/3600
    if sign == '-':
        lon = lon * -1
    return lon
    

#here script starts
lon = 11.34999
lat = 46.49809
radiusKm = 20.0

path = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/stations.txt"

centerPoint = HPoint(lon,lat)


with open (path, 'r') as file:
    lines = file.readlines()
    
#buffer = centerPoint.buffer(radiusKm)  --> problem becaus here it would take degrees and not km!! so we need to use a projectionAcronym

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632) #this projection is in km look it up at spatialreference.org

centerPoint32632 = crsHelper.transform(centerPoint)

buffer = centerPoint32632.buffer(radiusKm*1000)  


for line in lines[1:]:
    line = line.strip()
    #print(line)
    
    lineSplit = line.split(",")
    latStr = lineSplit[3]
    lonStr = lineSplit[4]
    name = lineSplit[1].strip()
    
    latDec = fromLatString(latStr)
    lonDec = fromLonString(lonStr)
    
   
    
    
    point = HPoint(lonDec,latDec)
    point32632 = crsHelper.transform(point)
   
    
    if buffer.intersects(point32632):
        distance = point32632.distance(centerPoint32632)
        print(name,"is approximately", round(distance/1000,2),"km away from", point )
    
    
    
    