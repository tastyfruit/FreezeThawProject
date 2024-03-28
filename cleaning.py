######################################################################
#
#     This is basically just going the count the number of freezes
# that occur during the csv file. super basic code
#     There are a few times that they input the data with a char and
#that means I cant int it so I did hardcode for those
#     I'll probably change that to a try and except loop
#
#######################################################################


import csv

basestr = "AirportName_"
ending = ".csv"

#added the code below because it is much more descript
readfolderdir = ".\\" #current directory
writefolderdir = "output\\" #output directory. will make a new one if it doesn't exist


for i in range (0,80):
    previous_temp = 0
    freezecount33_32 = 0
    freezecount32_31 = 0
    freezecount40_32 = 0
    freezecountdays = 0
    previous_day = "no"
    previous_over40 = "no"
    
    
    
    
    year = str(1951 + i) #change to start year
    
    string = readfolderdir + basestr + year + ending #creating the string to open
    
    file = open(string, "r") #opening up the desired file using string built above
    reader = csv.reader(file) #using csv.reader
    
    filewrite = open(writefolderdir + "AirportNameNumOfEvents.csv", "a", newline = '')
    writefile = csv.writer(filewrite) #append instead of write

    
    if i == 0: #header line
        writefile.writerow(["Year","32-->31","33-->32","40-->32","Days Below Freezing"])
    
    
    
    
    
    
    for line in reader: #looping through the file
    
        #GATHERING DATA POINTS
        date = line[0]
        hour = line[1]
        
        #there were some issue with consistency specifically in the temp column
        try: 
            temp = int(line[2])
            
        except ValueError: 
            if line[2] == '*': #only encountered this once but just as a precaution
                continue
            else:
                temp = int(line[2][:-1]) 
                #sometimes the number is like "65s" or "24s" so just take the num
                
        except IndexError:
            continue #unable to locate for now so we just skip over
            
        
        #FREEZING EVENTS 32 --> 31
        if previous_temp >= 32 and temp < 32: 
            freezecount32_31 += 1 
            
        #FREEZING EVENTS 33 --> 32
        if previous_temp >= 33 and temp < 33: 
            freezecount33_32 += 1 #freezing events 33-->32
            
            
        #FREEZING FROM WATER'S HIGHEST DENSITY (39.8) TO FROZEN(SUB 32)
        if temp <= 32 and previous_over40 == "yes":
            freezecount40_32 += 1
            previous_over40 = "no" #using this as a flag
            
        if temp >= 40:
            previous_over40 = "yes"             
            
        #DAYS WITH SUB 32 TEMPS
        if temp <= 32:
            if previous_day != date:
                previous_day = date
                freezecountdays += 1
        
        previous_temp = temp
            
    #WRITING TO NUMOFEVENTS FILE
    writefile.writerow([year, freezecount32_31, freezecount33_32, freezecount40_32, freezecountdays])
  
        
      #REMEMBER TO CLOSE UR FILES :)
    file.close()
    filewrite.close()

