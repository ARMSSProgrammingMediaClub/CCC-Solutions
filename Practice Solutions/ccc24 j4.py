#finally solved 
pressed = input()
displayed = input()

pressed_set = set(pressed)
displayed_set = set(displayed)
difference_pressed = pressed_set.difference(displayed_set) # in pressed but not in displayed
difference_displayed = displayed_set.difference(pressed_set) # in displayed but not in pressed
difference_pressed = list(difference_pressed)
difference_displayed = list(difference_displayed)

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
