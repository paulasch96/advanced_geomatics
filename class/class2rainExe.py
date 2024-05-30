dataPath = "/Users/paulaschmidl/Desktop/GIS/01_exe_rain_data_1year.txt"

#print out 5 linesIntersection3D
with open(dataPath, "r") as file:
    lines = file.readlines()
    
date2ValuesListMap = {}
    
for line in lines:
    line = line.strip() #do ALWAYS remove white space
    if line.startswith("#") or len(line) == 0:
            continue
    #print(line)

    #parse each line to extract the date and the value 
    
    SplitLine = line.split(",")
    date = SplitLine[0]
    value = float(SplitLine[1])
    #print(date,": ",value)
    
    # extract the yaer-month from date and use as key for nect steo

    month = date[:-2]
    #print(month, ": ", value)
    
    #sum up all monthly values
    
    
#aggregate the values by date, i.e. collect all values
# for each date in a list
    values = date2ValuesListMap.get(month, [])
    values.append(value)
    date2ValuesListMap[month] = values
    
   # print(date2ValuesListMap)
    
for month, values in date2ValuesListMap.items():
    #print(month, values)   #now we have all the vlues that belong to one month
    cumRain = sum(values)
    print(f"Cumulated rain for month {month} is {cumRain}")

    