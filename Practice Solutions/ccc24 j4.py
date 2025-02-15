#finally solved 

"""
Thinking process:
1. Find unique characters by creating sets of pressed and displayed characters 
2. Find possible troublesome keys by finding differences between both sets (two differenced sets, one for if in pressed but not in displayed and another for in displayed and not in pressed)
3. If there is only 1 troublesome key, we know that there is no quiet key so we immediately know which keys are silly
4. To differentiate between quiet and silly keys, we will test both possible troublesome keys by mimicking the effects of both the silly and quiet key onto pressed
5. If not the first case, its the other.

"""
pressed = input() 
displayed = input()

pressed_set, displayed_set = set(pressed), set(displayed) #find unique characters
difference_pressed, difference_displayed = pressed_set.difference(displayed_set), displayed_set.difference(pressed_set) # in pressed but not in displayed and in displayed but not in pressed
difference_pressed, difference_displayed  = list(difference_pressed), list(difference_displayed) #turn into list for indexing

if len(difference_pressed) == 1: #if there is only 1 troublesome key, that is the silly key. there is no quiet key
    print(*difference_pressed, *difference_displayed)
    print(*'-')

else: #now we need to figure out which of the two troublesome keys is silly and which is quiet
    x = pressed.replace(difference_pressed[0], difference_displayed[0]) #to mimic silly key: have difference_pressed[0] as silly, and difference_pressed[1] as quiet
    y = x.replace(difference_pressed[1], '')# to mimic quiet key: if correct this will equal displayed
    if y == displayed:
        print(difference_pressed[0], difference_displayed[0]) #first possible trouble key is the silly key
        print(difference_pressed[1])
    else:
        print(difference_pressed[1], difference_displayed[0]) #if not, the trouble keys are filled, only other case
        print(difference_pressed[0])
