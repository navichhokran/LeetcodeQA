from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        returnHead = head2 = head
        nodeToRemove =head
        count = 0
        
        if head.next == None:
            return []

        while head != None:
            count += 1 
            head = head.next

        nthNode = count - n + 1

        if nthNode == 1:
            return returnHead.next

        count2 = 0
        while head2 != None:
            count2 +=1
            if count2 == nthNode - 1:
                nodeToRemove = head2
                break
            head2 = head2.next
    
        nodeToRemove.next = nodeToRemove.next.next
        return returnHead

 
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:

        returnHead = nodeToRemove = head
        if head.next == None:
            return []

        listOfNNodes = deque([])
        while head != None:
            listOfNNodes.append(head)
            if len(listOfNNodes) > n + 1:
                listOfNNodes.popleft()
            head = head.next
        
        if len(listOfNNodes) < n + 1 : 
            return returnHead.next
            
        nodeToRemove = listOfNNodes[0]
        nodeToRemove.next = nodeToRemove.next.next

        return returnHead





        
      


node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
# node2.next = node3
# node3.next = node4

def printList(node):
    while node != None : 
        print('{} -> '.format(node.val), end='')
        node = node.next
    

# printList(node1)
# print('\n\n')

# sol = Solution()
# sol.removeNthFromEnd(node1,2)
# print('\n')
# printList(node1)

