# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validBST(root, float('-inf'), float('inf'))

    def validBST(self,root: TreeNode, lowerBound, upperBound):
        if root is None:
            return True

        if root.val > lowerBound and root.val < upperBound:
            return self.validBST(root.left,lowerBound, root.val) and self.validBST(root.right,root.val, upperBound)
        else:
            return False
       