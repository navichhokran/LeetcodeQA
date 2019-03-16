# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast !=  None :
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node2

sol = Solution()

print(sol.hasCycle(node1))
