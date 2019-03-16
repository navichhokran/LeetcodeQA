
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsDict = {}
    for i in nums:
        numsDict[i]=0
    
    for i in nums:
        numsDict[i]=numsDict[i]+1

    print(numsDict)
    for k,v in numsDict.items():
        if v==1:
            number = k
            break;

def singleNumber2(A):
    ans = A[0]
    print(ans)
    print('----------')
    for i in range(1, len(A)):
        ans = ans ^ A[i]
        print(ans)
    return ans

nums = [1,1,2,3,3]
print(singleNumber2(nums))

