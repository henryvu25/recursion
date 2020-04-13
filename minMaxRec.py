def minMaxRec(numList, min, max): 
    if len(numList) == 0:
        return min,max

    if numList[0] < min:
        min = numList[0]
    if numList[0] > max:
        max = numList[0]
    return minMaxRec(numList[1:], min, max)


numList = [3,5,7,-55]

print(minMaxRec(numList, numList[0], numList[0]))