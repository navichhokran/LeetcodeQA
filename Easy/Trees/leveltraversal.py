# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        listOfLists = []
        self.levelTraversal(root, listOfLists,0)
        return listOfLists
    
    def levelTraversal(self,node: TreeNode, listOfLists, level):
        if node is None:
            return
        
        if len(listOfLists) < level + 1:
            listOfLists.append([node.val])
        else:
            listOfLists[level].append(node.val)
        
        self.levelTraversal(node.left, listOfLists, level+1)
        self.levelTraversal(node.right,listOfLists,level+1)


    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []

        listOfLists = []
        q = [root]
        
        while q:
            listOfLists.append([])
            nxtq = []
            for node in q:
                listOfLists[-1].append(node.val)
                if node.left:
                    nxtq.append(node.left)
                if node.right:
                    nxtq.append(node.right)
            q = nxtq
        
        return listOfLists



    