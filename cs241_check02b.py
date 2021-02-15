
file = open(input("Enter file: "), "r")
w = file.read()
words = w.split()
Numlines = w.split("\n")  
Counter = 0 
for i in Numlines: 
    if i: 
        Counter += 1
          
print('The file contains', Counter,'lines and', len(words),'words.')