#For the assignment we will 1)prompt user for a file 2)parse through the file line by line
#3)Return the values and format the display 4)In main function we will call functions and print data
#Some code used from Brother Mellor tutorial video
def prompt_file():
    #prompts the user for a file
    fileName = input("Please enter the data file: ")
    return fileName

def parseFile(fileName):
    # function reads the file line by line
    f = open(fileName,'r') 
    average = 0.0
    low_com = 5000
    max = 0.0
    total = 0
    lineMax = ""
    lineMin = ""    
    for line in f:
        try:
            #code is going to try to see if total is greater than 0 than it will run the code if not we will get a except return with bad values
            if(total > 0):
                File = float(line.split(",")[6])
                average += File
                if(max < File):
                    max = File
                    lineMax = line
                if(low_com > File):
                    low_com = File
                    lineMin = line
            total += 1
        except:
            return 0.0, "bad", "bad", "", ""
    average = average / float(total -1) #Calulate the average of the comm rate
    f.close()
    return average, max, low_com, lineMin, lineMax
            
def layout(uName, zipCode,state,commRate):
        print("{} ({}, {}) - ${}".format(uName,zipCode,state,commRate))
        #The display format for the data in csv file

def main():
    #main function will call all varibles
    fileName = prompt_file()
    print()
    average,maxRate,  minRate, minLine, maxLine = parseFile(fileName)
    print("The average commercial rate is: {}".format(average))
    #Prints out the average commercial rate out of all the data
    print()
    print("The highest rate is:")
    maxLineArray = maxLine.split(",")
    layout(maxLineArray[2], maxLineArray[0], maxLineArray[3],float(maxLineArray[6]))
    #prints out the lowest rate in the array in display function format
    print()
    print("The lowest rate is:")
    minLineArray = minLine.split(",")
    layout(minLineArray[2], minLineArray[0], minLineArray[3],float(minLineArray[6]))
    #prints out the lowest rate in the array in display function format
if __name__ == "__main__":
    main()