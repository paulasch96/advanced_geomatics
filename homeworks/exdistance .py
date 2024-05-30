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

path = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/stations.txt"

centerPoint = HPoint(lon,lat)


with open (path, 'r') as file:
    lines = file.readlines()
    
minDistance = 9999999
nearestStationName = "none" #obecet that contains a string wit none
nearestDistancePoint = None #object that contains nothing

for line in lines[1:]:
    line = line.strip()
    #print(line)
    
    lineSplit = line.split(",")
    latStr = lineSplit[3]
    lonStr = lineSplit[4]
    name = lineSplit[1].strip()
    latDec = fromLatString(latStr)
    lonDec = fromLonString(lonStr)
    print(name, latDec, lonDec)
    
    point = HPoint(lonDec, latDec)
    
    distance = point.distance(centerPoint)
    if distance < minDistance:
        minDistance = distance
        nearestStationName = name
        nearestDistancePoint = point
        
print(nearestStationName, "-->", nearestDistancePoint)
    

    
    
    

