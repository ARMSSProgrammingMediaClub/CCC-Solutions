#cool brute force solution using nested forloops to splice indexes, might try using implementation of manacher's algorithm as well
lengths = []
for i in range(len(n)):
    for j in range(len(n)):
        substring = n[i:j+1] 
        if substring == substring[::-1]:
            lengths.append(len(substring))         
print(max(lengths))
