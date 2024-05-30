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


crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)


proj_stations = []  #ranking=name 

for i in coordinates:
    coord = crsHelper.transform(i)
    proj_stations.append(coord)



uni = HPoint(11.34999, 46.49809)



dists = []

for j in proj_stations:
    dist = uni.distance(j)
    dists.append(dist)

proj_stat_names = {}

for k in range(len(proj_stations)):
    proj_stat_names[proj_stations[k]] = names[k]
    
#no i have a dict with stations (val) and dists(keys) to uni.

#sort  after distances
keys = list(dists_stats.keys())
keys.sort(reverse = True)





uni_t = crsHelper.transform(uni)
#make radius of 30km distance

uni_buffer = uni_t.buffer(30000)

close_stations = []

for x in proj_stations:
    if uni_buffer.contains(x):
        close_stations.append(x)
        
print("Following stations are within a 30km radius of UniBz:")
    
for y in close_stations:
     print(proj_stat_names[y])
    
#close_stations contains the trandformed coords of 6 stations
#i need a dict with transformed stations and names to print the names of the 6 stations
        
      

# canvas = HMapCanvas.new()
# osm = HMap.get_osm_layer()
# canvas.set_layers([osm])


# canvas.set_extent([-1500000,4000000,6000000,10000000])
# canvas.add_geometry(uni_buffer,"red",3)
# canvas.show()
    
# print(uni)
    




    