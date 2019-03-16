import collections
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    
    charDict = {}
    
    for char in s:
        if(char not in charDict):
            charDict[char] = 0    
        charDict[char] = charDict[char] + 1
    
    for i in range(len(s)):
        if(charDict[s[i]] == 1):
            return i

    return -1

def firstUniqChar2(s):
    index=[s.index(l) for l in s if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1

def firstUniqChar3(s):
    letters='abcdefghijklmnopqrstuvwxyz'
    for i in letters:
        if s.count(i) ==1:
            return s.index(i)

index = firstUniqChar3('loveleetcode')
print(index)
