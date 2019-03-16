
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    numsDict = {i:0 for i in nums }
    for i in nums : 
       numsDict[i] = numsDict[i] + 1 
       if numsDict[i] > 1 : 
           return True
    
    return False

def containsDuplicate2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    if nums is None or len(nums) == 0 or len(nums) ==1 : 
        return False

    nums.sort()
    for i in range(0,len(nums)-1) : 
       if nums[i] == nums[i+1] :
           return True
    
    return False

hasDuplicate = containsDuplicate2(nums=None)
        
print(hasDuplicate)