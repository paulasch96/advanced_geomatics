from pyqgis_scripting_ext.core import *


path = "/Users/paulaschmidl/Desktop/github/advanced_geomatics/data/stations.txt"
with open (path, 'r') as file:
     lines = file.readlines()
   
for line in lines:
    line = line.strip()
    #print(line)
    
coordinates = []
names = []
    
for line in lines:
    if len(line) == 0 or line.startswith('#'):
        continue
    line = line.split(',')
    name = line[1].strip()
    country = line[2]
    lat = line[3] #-84to84
    lon = line[4] #-180to180
    lat_d = int(lat.split(':')[0].strip('+'))
    lat_min = int(lat.split(':')[1])/60
    lat_sec = int(lat.split(':')[2])/3600
    
    lat_decimal = lat_d+lat_min+lat_sec
    
    lon_d = int(lon.split(':')[0].strip('+'))
    lon_min = int(lon.split(':')[1])/60
    lon_sec = int(lon.split(':')[2])/3600
    
    lon_decimal = lon_d+lon_min+lon_sec
    
   
    
    stations = HPoint(lon_decimal,lat_decimal)
    #print(stations)
    coordinates.append(stations)
    names.append(name)
    
coords_names = {}

for a in range(len(names)):
    coords_names[names[a]] = coordinates[a]







proj_stations = []  #ranking=name 

for i in coordinates:
     proj_stations.append(i)



uni = HPoint(11.34999, 46.49809)



dists = []

for j in proj_stations:
    dist = uni.distance(j)
    dists.append(dist)

dists_stats = {}

for k in range(len(proj_stations)):
    dists_stats[dists[k]] = names[k]
    

#sort  after distances
keys = list(dists_stats.keys())
keys.sort(reverse = True)




for key in keys[-1:]:
    print(dists_stats[key], "is the closest station and has the coordinates", coords_names[dists_stats[key]])



    
    




    