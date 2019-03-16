# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

    

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

def printList(node):
    while node != None : 
        print('{} -> '.format(node.val), end='')
        node = node.next
    

printList(node1)

sol = Solution()
sol.deleteNode(node3)
print('\n')
printList(node1)