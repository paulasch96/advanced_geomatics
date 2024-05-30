from pyqgis_scripting_ext.core import *
folder = "/Users/paulaschmidl/Desktop/GIS/EX0-4_SCHMIDL_PAULA"
path = f"{folder}/stations.txt"

with open (path, 'r') as file:
     lines = file.readlines()
   
for line in lines:
    line = line.strip()
    #print(line)
    
coordinates = []
countries = []
counted = {}
    
for line in lines:
    if len(line) == 0 or line.startswith('#'):
        continue
    line = line.split(',')
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
    
    #print(lat_decimal,lon_decimal)
    
    stations = HPoint(lon_decimal,lat_decimal)
    #print(stations)
    coordinates.append(stations)
    countries.append(country)


#print(coordinates)

#transform

crsHelper = HCrs()
crsHelper.from_srid(4326) 
crsHelper.to_srid(3857) #3857 is for OSM

proj_stations = []

for i in coordinates:
    var = crsHelper.transform(i)
    proj_stations.append(var)
#print(proj_stations)
    
    
canvas = HMapCanvas.new()



osm = HMap.get_osm_layer()
canvas.set_layers([osm])


for station in proj_stations:
    canvas.add_geometry(station,"red",2)
    
    
canvas.set_extent([-1500000,4000000,6000000,10000000]) #vom aequator und greenich (jeweils 0) ausgehen. in km 



    
    
canvas.show()


for i in countries:
    if i in counted:
        counted[i] += 1
    else:
        counted[i] = 1
        
values = list(counted.values())
values.sort()
print(values)

for va in values:
    print(f"{counted[va]} : {va}")
    
