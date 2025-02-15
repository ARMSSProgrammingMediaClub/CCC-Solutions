# super ugly solution but it works lol

n = int(input())
xcor = []
ycor = [] 
for i in range(n): #splits x coordinates and y coordinates into 2 different lists
    cor = input()
    x = cor.split(',')
    xcor.append(x[0])
    ycor.append(x[1])


# find the minimum or maximum points of each and add or subtract 1 to make frame fit
minx = int(min(xcor)) - 1 
miny = int(min(ycor)) - 1
maxy = int(max(ycor)) + 1
maxx = int(max(xcor)) + 1

#formatting answer 
bottomleft = str(minx) + "," + str(miny)
topright = str(maxx) + "," + str(maxy)

print(bottomleft)
print(topright)
