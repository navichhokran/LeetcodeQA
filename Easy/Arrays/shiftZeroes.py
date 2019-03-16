def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    for i in nums : 
        if(i == 0 ):
            nums.remove(i)
            nums.append(i)
    return nums

def moveZeroes2(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if nums[j] != 0:
                    nums[j-1] = nums[j]
                    nums[j] = 0
    
    return nums


def moveZeroes3(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i=0
    while i< len(nums):
        if nums[i] == 0 : 
            for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                    nums[j+1] = 0
        if nums[i] != 0:
            i = i+1
        print(i , nums[i])
        print(nums)

    return nums

nums = moveZeroes3(nums=[0,4,0,0,6])
print(nums)