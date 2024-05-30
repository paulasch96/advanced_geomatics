
def fileSummary(path, idFieldName, avgFieldName):
    with open (path, 'r') as file:
        lines = file.readlines()
    
    idIndex = None
    analyzedIndex = None #for defining a variable without value
    hSum = 0
    count = 0 
    uniqueIdsList = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            #header
            fields = line.strip('#').split(',')
            
            #getting the fields for calculating average and so on
            for index, field in enumerate(fields): #enumerate is like a for loop but also going throuhgh the index of the field
                field = field.strip()
                if field == idFieldName:    #idFieldname given in the functio and im the command with the fileSummary function below
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
        else: 
           #here the data starts
            lineSplit = line.split(',') 
            value = float(lineSplit[analyzeIndex])
            if value == -9999:
                continue
            else:
                hSum += value
                count += 1 
            
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
          
    average = hSum/count      
          
              
                    
            #print(idIndex, analyzeIndex)
            
            
    print(f"File info: {path}")
    print("====================")
    print(f"unique {idFieldName} count: {len(uniqueIdsList)}")
    print(f"Average of field {fields[analyzeIndex]}: {average}")
    print("Fields:")
    for field in fields:
        print(f"-> {field.strip()}")
        
        
        
    


fileSummary("/Users/paulaschmidl/Desktop/GIS/EX0-4_SCHMIDL_PAULA/stations.txt", "CN", "HGHT")
print("--------------------")
fileSummary("/Users/paulaschmidl/Desktop/GIS/station_data.txt", "CN", "RR")