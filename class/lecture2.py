mylist = ["merano", "Bolzano", "Trento"]

print(mylist)

print("the elements start at position 0:", mylist[0])

mylist.append("potsdam")
print(mylist)

mylist.remove("potsdam")
print(mylist)


mylist.pop(0)
print(mylist)

doIHaveBZ = "Bolzano" in mylist
print(doIHaveBZ)
doIHavePD = "potsdam" in mylist
print(doIHavePD)

for item in mylist:
    print(item)
    
colors = ["red","green","blue", "purple"]
ratios = [0.2,0.3,0.1,0.4]

for index in range(len(colors)):
    color = colors[index]
    ratio = ratios[index]
    
    print(f"{color} --> {ratio}")
    
colors2 = colors.copy()

colors.sort()


for i in range(10):

    if i == 5:
        break 
    print(f" A) {i}")
   
print("-----------")
    
for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")
    
print("-----------")

for i in range(0,10, 2):
    print(f"C) {i}")
    
print("-----------")

for i in range(10,0, -2):
    print(f"D) {i}")
    
    
mylist = ["merano", "Bolzano", "Trento"]
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse = True)
print(mylist)


mylist = ["cherry","banana","Orange","Kiwi"]
mylist.sort()
print(mylist) #---> doesent work bc differnt (upper/lower case)

mylist.sort(key = str.lower)
print(mylist)
    


numblist = ["002","01","3","004"]
numblist.sort()
print(numblist)


numblist = ["002","01","3","004"]

def toInt(string):
    return int(string)
    
#numblist.sort(key = toInt)
#print(numblist)
    

abc = ["a","b","c"]
cde = ["c","d","e"]

newabcde = abc + cde
print(newabcde)

print(";".join(newabcde))

numlist = [1.0,2.0,3.5,6,11,34,12]
print(max(numlist))
print(min(numlist))
#print(sum(numlist))


average = sum(numlist)/len(numlist)
print(average)



mysum = 0 
count = 0 
  
for item in numlist:
    mysum = mysum + item
    count += 1
    
    
average = mysum/count

print(average)

variance = 0

for item in numlist:
    nummer = (item - average)*(item-average)
    nummer/(count-1)
    print(nummer)
    
    
townsProvincesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trento": "TN"
}


print(townsProvincesMap)

print(townsProvincesMap["merano"])
    
townsProvincesMap["potsdam"] = "BR"

print(townsProvincesMap)

townsProvincesMap.pop("potsdam")
print(townsProvincesMap)

if townsProvincesMap.get("Merano") is None:
    print("key doesnt exist")
else:
    print("key exists")
    
    
print(townsProvincesMap.get("Merano", "unknown"))


for key, value in townsProvincesMap.items():
    print(key, "is in the province of", value)
    
print(townsProvincesMap.keys())
print(townsProvincesMap.values())

keys = list(townsProvincesMap.keys())
keys.sort()
print(keys)

for key in keys:
    print(key, "is in the province of", townsProvincesMap[key])
    

filePath = "/Users/paulaschmidl/Desktop/GIS/data.txt"
data = """# satationid, datetime, temperature
1, 2023-01-01 00:00, 12.3

2, 2023-01-01 00:00, 11.3
3, 2023-01-01 00:00, 10.3
"""

with open(filePath, "w") as file:
    file.write(data)

with open(filePath, "a") as file:
    file.write("\n1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")

with open(filePath, "r") as file:
    lines = file.readlines()
    
print(lines)
print("-------------------")
stationsCount = {}
for line in lines:
    line = line.strip() #removes empty spaces in beginnig e.g. \n
    if line.startswith("#") or len(line) == 0:
        continue                                #skip/ dont execute what comes after and go t next line
    lineSplit = line.split(",")
    #print(lineSplit)
    stationId = lineSplit[0]
    #print(stationId)
    
    counter = stationsCount.get(stationId, 0)
    counter += 1
    
    stationsCount[stationId]= counter
    
    print(stationsCount)
