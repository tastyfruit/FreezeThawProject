#read in csv file using open
import pylab
import csv

basestr = "Duluth_" #change to airport
year = 1951 #change to first year you want to process
ugly = "_ugly.csv"
ending = ".csv"

for i in range (0,82): #typically I just run it all together and cross my fingers

    #CREATING FILENAMES TO OPEN
    if i == 0:
        uglystring = basestr + str(year) + ugly #the first year
    else:
        uglystring = basestr + str(year + i) + ugly
        #adds onto year in order to create string with the correct year

    if i == 0:
        finalstring = basestr + str(year) + ending #the first year
    else:
        finalstring = basestr + str(year + i) + ending
        #adds onto year in order to create string with the correct year
    
    #OPENING FILE TO READ FROM
    fileread = open(uglystring, "r") 
    readfile = csv.reader(fileread)

    #OPENING FILE TO WRITE TO
    filewrite = open(finalstring, "w", newline = '')
    writefile = csv.writer(filewrite)

    header = next(readfile) #skipping header

    previous_hour = 12 #just a placeholder

    for line in readfile:

        #COLLECTING DATE (INDEX 1, FIRST TEN CHARACTERS)
        try:
            date = line[1][0:10]
        except IndexError:
            continue
        
        #COLLECTING HOURS (INDEX 1, 11-12TH CHARACTERS)
        try:
            hour = line[1][11:13]
        except IndexError:
            continue
        
        #COLLECTING DRY BULB TEMPERATURE (INDEX 44)
        try:
            temp = line[44]
        except IndexError:
            continue
        
        #sometimes the temperature is empty at the first measurement of the hour
        if temp == '': 
            continue #just skip it
        
        #we want to make sure we only have one measurement per hour
        if hour != previous_hour: 
            writefile.writerow([date, hour, temp])
            

        previous_hour = hour
        


    #DONT FORGET TO CLOSE YOUR FILES :)
    fileread.close()
    filewrite.close()
        

