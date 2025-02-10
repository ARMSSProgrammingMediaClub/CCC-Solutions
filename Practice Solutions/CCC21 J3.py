#Full scoring submission 15/15

direction = "" #define variables
while True:
    num = input()
    firstTwo = int(num[0]) + int(num[1]) #adds the integer values of first two numbers
    if num != "99999":
        if firstTwo % 2 == 0 and firstTwo != 0: #if even and not zero direction is right
            direction = "right"
        elif firstTwo % 2 != 0: #if odd direction is left
            direction = "left"
        else: pass # if equal to zero, takes in last direciton used
        print(direction, num[2:]) #prints decoded version to console before looping again
    else: break
