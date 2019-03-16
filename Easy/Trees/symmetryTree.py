# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.checkSym(root.left, root.right)
    
    def checkSym(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        elif leftNode.val == rightNode.val:
            return self.checkSym(leftNode.left, rightNode.right) and self.checkSym(leftNode.right, rightNode.left)
        else:
            return False

