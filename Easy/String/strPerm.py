
def perm(theStr, count, result,level):
    if level == len(result):
        print(result)
        return
    
    for i in range(len(theStr)):
        if count[i] == 0:
            continue
        else:
            result[level] = theStr[i]
            count[i]-=1
            perm(theStr, count, result, level + 1)
            count[i]+=1


def printPerms(string):

    countDict = {}
    for ch in string:
        if ch in countDict:
            countDict[ch]+=1
        else:
            countDict[ch] = 1
    
    keys = sorted(countDict)
    result = [0 for i in range(len(string))]
    count=[]
    theStr=[]
    for key in keys:
        count.append(countDict[key])
        theStr.append(key)
    
    perm(theStr, count, result, 0)


printPerms('aa')