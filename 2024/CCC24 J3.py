"""
CCC '24 J4 "Bronze Count"
Problem Link: https://dmoj.ca/problem/ccc24j3
Score Received: 15/15
See Practice Solutions folder for much faster solution
"""

def main():
    n = int(input()) # take in first input which is the number of participants
    scores = [] # create list of all the scores recieved 
    counter = 0 # counter for number of people that acheived bronze
    
    for _ in range(n): # forloop in range of # of participants 
        x = int(input()) 
        scores.append(x) #take in input on each line and add to scores list

    scores_new = list(dict.fromkeys(scores)) # create a new list with removed duplicates
    scores_new.sort() # sort list numerically
    scores_new.reverse() # reverse list --> this is to easily find the score-value of bronze by indexing scores[2]
    
    """
    Explanation of how to use list(dict.fromkeys(scores)) function:
    1. using dict.fromkeys() take in a list and convert into dictionary keys which automatically removes duplicates.
    2. use list() function to convert back into a list.
    3. new list is now stored in scores_new variable.

    """

    for j in range(len(scores)): # forloop to count number of bronze medals 
        if scores[j] == scores_new[2]: # check if current value in list is the same as bronze place score
            counter += 1 # if the value in list is equal to the bronze place score then add one to counter.
        else:
            counter += 0 # if not equal then add 0 and repeat foir loop until end

    bronze_value = str(scores_new[2])
    number_of_bronze = str(counter)

    print(bronze_value + " " + number_of_bronze) # print the bronze place score + a space + the counter value of how many people got the bronze place score


main()
