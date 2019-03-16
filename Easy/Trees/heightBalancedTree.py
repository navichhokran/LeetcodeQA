# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return None
        
        return self.sortedArrayWithRange(nums,0, len(nums)-1)
        
        
    def sortedArrayWithRange(self, nums,lowerbound, upperbound)-> TreeNode:
        mid = lowerbound+(upperbound-lowerbound)//2
         
        if lowerbound > upperbound:
            return None
        
        node=TreeNode(nums[(mid)]);
        node.val=nums[mid]
        node.left=self.sortedArrayWithRange(nums,lowerbound,mid-1)
        node.right=self.sortedArrayWithRange(nums,mid +1,upperbound)

        return node
