# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        curNode = firstNode = ListNode(0)   
        i = l1
        j = l2

        while i != None and j!= None :
            if i.val <= j.val :
                nextNode1 = i.next 
                curNode.next = i 
                curNode = i
                i = nextNode1 
            else:
                nextNode2 = j.next
                curNode.next = j 
                curNode = j
                j = nextNode2
            
        
        while i!=None:
            curNode.next = i
            curNode = i
            i = i.next
        
        while j!=None:
            curNode.next = j
            curNode = j
            j = j.next
        
        return firstNode.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node5= ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3

node5.next = node6
node6.next = node7


def printList(node):
    list = []
    while node != None : 
        list.append(node.val)
        node = node.next
    print(list)

printList(node1)
printList(node5)

sol = Solution()
newNode = sol.mergeTwoLists(node1,node5)
printList(newNode)

# 1 - 2 - 4 
# 1 - 3 - 4
# 
# 0 - 1 - 1 - 2 