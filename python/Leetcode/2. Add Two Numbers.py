# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = y = ListNode()
        a = b = 0
        
        i = 0
        while l1:
            a += l1.val*(10**i)
            i += 1
            l1 = l1.next
        
        i = 0
        while l2:
            b += l2.val*(10**i)
            i += 1
            l2 = l2.next
        
        res = a+b
        if res == 0:
            return y
        
        while res>0:
            x.next = ListNode()
            x = x.next
            x.val = res%10
            
            res = res // 10
        
        return y.next
            
        
        
        