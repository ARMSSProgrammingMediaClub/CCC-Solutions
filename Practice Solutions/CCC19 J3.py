#simple solution using fstring and splice
n = int(input())
for i in range(n): #n = number of lines
    x = input() #take in a new line each time
    y = "" #string for the encoded line
    c = 0 #counter
    for j in range(len(x)): #run loop for each character in input
        if j+1 != len(x) and x[j] == x[j+1]: #check if j+1 is in range 
            c += 1 #if the the current and next value are the same add 1 to counter
        else:
            y = (f"{y} {c+1} {x[j]}") #add c+1 and current index to y string
            c = 0 #reset counter
    print(y[1:]) #print values from index 1 as there is a space at index 0
