#finally solved 

"""
Thinking process:
1. Find unique characters by creating sets of pressed and displayed characters 
2. Find possible troublesome keys by finding differences between both sets (two differenced sets, one for if in pressed but not in displayed and another for in displayed and not in pressed)
3. If there is only 1 troublesome key, we know that there is no quiet key so we immediately know which keys are silly
4. To differentiate between quiet and silly keys, we will test both possible troublesome keys by mimicking the effects of both the silly and quiet key onto pressed
5. If not the first case, it is the other.

"""
pressed = input() 
displayed = input()

#figure out possible troublesome keys
pressed_set, displayed_set = set(pressed), set(displayed) 
difference_pressed, difference_displayed = pressed_set.difference(displayed_set), displayed_set.difference(pressed_set)
difference_pressed, difference_displayed  = list(difference_pressed), list(difference_displayed)

if len(difference_pressed) == 1: #Case 1 if no quiet key: there will only be 1 possible troublesome key
    print(*difference_pressed, *difference_displayed)
    print(*'-')

else: #Differentiate between silly and quiet key
    x = pressed.replace(difference_pressed[0], difference_displayed[0]) #mimic silly key using first possible trouble key
    y = x.replace(difference_pressed[1], '') #mimic quiet key with second possible trouble key
    if y == displayed:
        print(difference_pressed[0], difference_displayed[0]) 
        print(difference_pressed[1])
    else: #flipped 
        print(difference_pressed[1], difference_displayed[0]) 
        print(difference_pressed[0])
