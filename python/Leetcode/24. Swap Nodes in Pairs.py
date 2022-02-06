# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        l1 = head

        while l1 and l1.next:
            l1.val, l1.next.val = l1.next.val, l1.val
            l1 = l1.next.next
        
        return head