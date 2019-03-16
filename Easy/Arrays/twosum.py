
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    i = 0
    j= len(nums)-1
    indexes=[]
    nums2 = sorted(nums)
    while i < len(nums2)-1 and j >= 0 and i!=j:
        result = nums2[i] + nums2[j]
        if result > target  :
            j = j-1
        elif result < target:
            i = i+1
        else:
            index1 = nums.index(nums2[i])
            index2 = nums.index(nums2[j])
            if index1 == index2 : 
                index2 = nums.index(nums2[j], index1+1)

            indexes = [index1,index2]
            break;
    return indexes


def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexes=[]
    lookup = {v:i for i,v in enumerate(nums)}

    for i in range(0,len(nums)-1) : 
        diff = target - nums[i]
        if lookup.get(diff) !=None and lookup.get(diff) != i:
            index = lookup[diff]
            indexes = [i,index] 
    return indexes

indexes = twoSum2(nums=[3,3],target=6)
print(indexes)