# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        if head.next.next == None:
            newHead = head.next
            newHead.next = head
            head.next = None
            return newHead

        prev = head
        cur = head.next
        nxt = cur.next
        prev.next = None

        while True : 
            if cur.next == None:
                cur.next = prev
                break
            cur.next = prev
            prev = cur
            if nxt != None : 
                cur = nxt
                nxt = nxt.next
        return cur
 
    def reverseListRecur(self,prev,cur):
        if cur is None:
            return prev
        
        nxt = cur.next
        cur.next = prev

        return self.reverseListRecur(cur,nxt)

    def reverseList2(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            
            prev = None
            cur = head

            return self.reverseListRecur(prev,cur)     

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
    

printList(node1)

sol = Solution()
cur = sol.reverseList2(node1)
print('\n')
printList(cur)