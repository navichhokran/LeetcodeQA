def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1)==0 or len(nums2)==0 or nums1 is None or nums2 is None:
        return []
        
    i = 0 
    j = 0

    nums1.sort()
    nums2.sort()
    intersectionList = []
    while i < len(nums1) and j < len(nums2) : 
        if nums1[i] == nums2[j] : 
            intersectionList.append(nums1[i])
            i = i+1
            j = j+1
        elif nums1[i] < nums2[j] : 
            i = i+1
        else:
            j = j+1

    return intersectionList

intersectedElements = intersect(nums1=[1,2,4,12,6,2], nums2=[5,6,3,9,12,2,9,2])

print(intersectedElements)