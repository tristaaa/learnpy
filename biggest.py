def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggestDict = {}
    for k in aDict.keys():
        biggestDict[len(aDict[k])] = k
    if len(biggestDict) ==0:
        return None
    biggestKey = max(biggestDict.keys())
    return biggestDict[biggestKey]
print(biggest({'a':['aa'],'b':['bb'],'c':['cc'],'d':['dd','ddd'],'e':['e','ee']}))
print(biggest({}))