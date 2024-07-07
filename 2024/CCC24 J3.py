def main():
    n = int(input())
    scores = []
    counter = 0
    for _ in range(n):
        x = int(input())
        scores.append(x)

    scores_new = list(dict.fromkeys(scores))
    scores_new.sort()
    scores_new.reverse()

    for j in range(len(scores)):
        if scores[j] == scores_new[2]:
            counter += 1
        else:
            counter += 0

    str1 = str(scores_new[2])
    str2 = str(counter)

    print(str1 +   + str2)


main()