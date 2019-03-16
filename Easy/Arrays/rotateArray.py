
def rotate(nums,k):
    
    while k>0:
        i=len(nums)-1
        j=len(nums)-2
        temp=nums[len(nums)-1]

        while i>0:
            nums[i]=nums[j]
            j=j-1
            i=i-1
        nums[0]=temp
        k=k-1

    return nums

def rotate2(nums,k):

    k = k%len(nums)
    while(k>0):
        i=0
        j=1

        while(j<len(nums)):
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp
            j=j+1
        k=k-1

nums = [1,2,3,4,5,6,7]
rotate2(nums,3)

print(nums)