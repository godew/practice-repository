# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = []
        res = head
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        head = res
        for x in tmp:
            head.val = x
            head = head.next
        
        return res
            
            
        