# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack=[(root,1)]
        maxDepth = 0

        while(stack):
            node,depth = stack.pop()
            if depth > maxDepth:
                maxDepth = depth
            
            if node.left is not None:
                stack.append((node.left,depth+1))

            if node.right is not None:
                stack.append((node.right,depth+1))

            return maxDepth        

            

