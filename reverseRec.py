def reverseRec(numList, newList):
    if len(numList) == 0:
        return newList
    
    newList.append(numList[len(numList)-1])
    return reverseRec(numList[:len(numList)-1],newList)


numList = [3,5,7,-55]
newList = []

print(reverseRec(numList,newList))