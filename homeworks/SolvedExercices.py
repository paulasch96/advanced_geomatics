folder = "/Users/paulaschmidl/Desktop/PaulaSCHMIDL_GIS_1"
#exercise 1

age = 25
name = "Mario Rossi"
job = "engineer"
activity = "skating"

print(f"Hei, my name is {name} and i am {age} years old.\nI like {activity} and i am working as an {job}")

#exercise 2

csvPath = f"{folder}/01_exe2_data.csv"

with open(csvPath, 'r') as file:
    lines = file.readlines()
   
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    print(analogSplit)
    x1 = float(analogSplit[1])
    
    
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    #print(x1, y2)
    
    maxanalogString = lineSplit[2]
    maxanalogSplit = maxanalogString.split(":")
    x2 = float(maxanalogSplit[1])
    print(x1, x2, y2)
    
    y1 = y2 * x1/x2

    print(x1, x2, y1, y2)


#exercise  3
string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
newString = string.replace(",",";")
print(newString)

#exercise 4

myList = (1, 2, 3, 4, 5)

for item in myList:
    print(item)

#exercise 5

for item in myList:
    print(f"Number {item}")
    
#exercise 6

numberList = [10,20,30,40,50,60,70,80,90,100]

for item in numberList[:5]:
    print(f"Number {item}")

#exercise 7

list1=[1,2,3,4,5]
list2 = ["first", "second", "third", "fourth", "fifth"]

for item in range(len(list1)):
        print(f"{list2[item]} is {list1[item]}")
        
#exercise 8

string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

print(f"Characters count: {len(string)}")

stringNoSpaces = string.replace(" ", "")
print(f"Characters without white space: {len(stringNoSpaces)}")

stringWords = string.split(" ")

print(f"Word Count: {len(stringWords)}")


#exercise 9
csv2 = f"{folder}/01_exe9_data.csv"

with open (csv2, 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("#") or len(line) == 0:
            continue
        
        print(line)
        
#exercise 10
csv2 = f"{folder}/01_exe9_data.csv"

with open (csv2, 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        splitLine = line.split(" ")
        
       
        

        
        if line.startswith("#") or len(line) == 0:
            continue
            
        value1 = float(splitLine[1].strip())
        if  value1 >= 1000:
            continue
            
        print(line)
    


#exercice 11

data11 = f"{folder}/01_exe11_data.csv"

with open (data11, 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        stripline = line.strip("\n")
        splitline = stripline.split("=")
        height = splitline[2].strip()
        secvalue = splitline[1].split("cm")
        base = secvalue[0].strip()
        base = int(base)
        height = float(height)
        sum = base *height
        
        print(f"base * height / 2 = {base} * {height} = {sum}cm2")
        
#exercise 12

who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
}
what={
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
}
where = {
    44: "to town.",
    11: "in her bed.",
    201: "in the livingroom.",
    23: "up the mountain."
}


swapped_who = dict(zip(who.values(), who.keys()))
print(swapped_who)

wholist = list(swapped_who.keys())
whatlist = list(what.keys()).sort()
wherelist = list(where.keys()).sort()

wholist.sort()
print(wholist)

for item in wholist:
    print(swapped_who[item], what[item], where[item])


#exercise 13
list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

liste = list1 + list2 + list3 + list4
print(liste)

acount = 0
bcount = 0 
ccount = 0
dcount = 0
ecount =0
fcount=0
gcount=0
hcount=0

for item in liste:
    if item == 'a':
        acount = acount + 1
    elif item == 'b':
        bcount += 1
    elif item == 'c':
        ccount += 1
    elif item == 'd':
        dcount += 1
    elif item == 'e':
        ecount += 1
    elif item == 'f':
        fcount += 1
    elif item == 'g':
        gcount += 1
    elif item == 'h':
        hcount += 1
    else:
        continue
        
print(f" count of a = {acount}\n count of b = {bcount}\n count of c = {ccount}\n count of d = {dcount}\n count of e = {ecount}\n count of f = {fcount}\n count of g = {gcount}\n count of h = {hcount}\n")
    
#exercise 14:
stationsdata = f"{folder}/stations.txt"

with open (stationsdata, 'r') as file:
    lines = file.readlines()[:19]
        
for line in lines:
    print(line.strip())
    
        
    
#exercise 15:

stationsdata = f"{folder}/stations.txt"

with open (stationsdata, 'r') as file:
    lines = file.readlines()

counter = 0

for line in lines:
    if line.startswith("#") or len(line) == 0:
        continue
    line = line.split(",")
    line[0] = int(line[0])
    if line[0] > counter:
        counter = counter +1 
print(f"there are {counter} stations in the file")

#exercise 16
stationsdata = f"{folder}/stations.txt"

with open (stationsdata, 'r') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.split(",")
    
print(f" there are {len(line)} columns")

#exercise 17
stationsdata = f"{folder}/stations.txt"

with open (stationsdata, 'r') as file:
    lines = file.readlines()[:21]
    
for line in lines:
    if line.startswith("#"):
        continue
    line = line.split(",")
    print(line[0], line[1])
    
#exercise 18
stationsdata = f"{folder}/stations.txt"

with open (stationsdata, 'r') as file:
    lines = file.readlines()
    
summe = 0
for line in lines:
    if line.startswith("#") or len(line) == 0:
        continue
    line = line.split(",")
    line[5] = int(line[5])
    summe = summe + line[5]
average = summe/counter
print(f"The average height of the {counter} stations is app. {round(average,2)}m asl")



#exercise 19
stationsdata = f"{folder}/stations.txt"

def datasummary(stationsdata):
    
    fileparts = stationsdata.split("/")

    with open (stationsdata, 'r') as file:
        lines = file.readlines()

    counter = 0
#lstationscounter
    for line in lines:
        if line.startswith("#") or len(line) == 0:
            continue
        line = line.split(",")
        line[0] = int(line[0])
        if line[0] > counter:
            counter = counter +1 
    
#average


    summe = 0
    for line2 in lines:
        if line2.startswith("#") or len(line) == 0:
            continue
        line2 = line2.split(",")
        line2[5] = int(line2[5])
        summe = summe + line2[5]
    average = summe/counter
    average = round(average)

#fields???


    for line3 in lines:
        if line3.startswith("#"):
            i = line3.split(",")
        else: 
            continue
        
#firstlines



    lines = lines[:5]

    

        
    print(f"File info: {[-1]}\n----------------\nStations count: {counter} \nAverage value: {average}\nAvailable Fields:\n-->{i[0].strip()}\n-->{i[1].strip()}\n-->{i[2].strip()}\n-->{i[3].strip()}\n-->{i[4].strip()}\n-->{i[5].strip()}\nFirst datalines:")
    for line in lines:
        print(line.strip())
        
    return


datasummary(stationsdata)

    



#exercise 20

stations = f"{folder}/station_data.txt"
fileparts = stations.split("/")


with open (stations,'r') as stations2:
    
    count = 0
    summe = 0
    
    for line in stations2:
        if line.startswith('#') or len(line) == 0 or line.split(",")[3] == '-9999':
            continue
        count += 1
        summe += int(line.split(',')[3])
       
    ave = round(summe/count)
 
with open (stations,'r') as stations3:
    for lines in stations3:
        if lines.startswith('#'):
            l = lines.split(',')


print(f"File info: {fileparts[-1]}\n----------------\nStations count: {count} \nAverage value: {ave}\nAvailable Fields:\n-->{l[0]}\n-->{l[1].strip()}\n-->{l[2].strip()}\n-->{l[3].strip()}\n-->{l[4].strip()}\nFirst datalines:")
with open (stations,'r') as stations4:
    p = 0
    for lines in stations4:
        if p <= 5:
            print(lines)
        p += 1

#exercise 21

n=10
m= 5

for i in range(n):
    stars = "*" * m
    print(stars)
    
#exercise 22

n = 10 
count = 1 

for i in range(n):
    stars = "*" * count
    print(stars)
    count += 1
    
#exercise 23

n = 10


for i in range(n):
    stars = "*" * n
    print(stars)
    n = n - 1
    
#exercise 24

a = 10
summe = 0 
for i in range(0,a,2):
    summe = summe + i
    print(summe)
    
#exercise 25

numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
summe = 0 
evennumbers = []
for number in numbers:
    if number%2 == 0:
        summe = summe + number
        evennumbers.append(number)
    else:
        continue

print(summe, evennumbers)

print('_____________________')

#exercise 26

data1 = f"{folder}/01_exe26_dataset1.csv"
data2 = f"{folder}/01_exe26_dataset2.csv"

with open(data1, 'r') as file:
    d1 = file.readlines()

    
with open(data2, 'r') as file:
    d2 = file.readlines()

dict1 = {}
dict2 = {}

for i in d1[1:]:
    dict1[i.split(',')[0]] = [i.split(',')[1], i.split(',')[2].rstrip()]
    
for j in d2[1:]:
    dict2[j.split(',')[0]] = j.split(',')[1].rstrip()
    
    
for key in dict1.keys():
    dict1[key] += [dict2[key]]



newdata = dict1

print(newdata)



    




    
    
    
    

    

   