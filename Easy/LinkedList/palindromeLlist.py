# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        list = []
        while head != None:
            list.append(head.val)
            head = head.next
        
        return list == list[::-1]

