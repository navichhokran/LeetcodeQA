
import datetime
print('Removing duplicates')

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i=0
    j=1
    
    while j<len(nums) :
        if(nums[j]==nums[i]):
            nums.remove(nums[j])
        else:
            j=j+1
            i=i+1
    print(nums)
    return len(nums)
    

nums = [1,1,1,2,3,4,4,4,5,6,7,8,8,8,8]


def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)-1,0,-1):
        if nums[i]==nums[i-1]:
           del nums[i]
        
    print(nums)
    return len(nums)
    

nums = [1,1,1,2,3,4,4,4,5,6,7,8,8,8,8]

# startTime= datetime.datetime.now()
# print(removeDuplicates(nums))
# endTime= datetime.datetime.now()

# diff1 = endTime-startTime
# print('time taken - {}'.format(diff1.total_seconds() * 1000))

startTime2= datetime.datetime.now()
print(startTime2)

print(removeDuplicates2(nums))
endTime2= datetime.datetime.now()
print(endTime2)

difference = endTime2-startTime2
print(difference)

diff2 = (endTime2-startTime2).total_seconds() * 1000
print(type(diff2))
print('time taken - {}'.format(diff2))