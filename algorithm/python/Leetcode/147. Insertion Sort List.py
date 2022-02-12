# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        res = ListNode()
        tmp = res
        while head:
            while True:
                if tmp.next is None:
                    tmp.next = ListNode(head.val)
                    tmp = res
                    break
    
                if head.val < tmp.next.val:
                    tmp = tmp.next
            
                else:
                    tmp.next, tmp.next.next = ListNode(head.val), tmp.next
                    tmp = res
                    break
            head = head.next
        
        # 연결리스트 뒤집기
        res = None
        tmp = tmp.next
        while tmp:
            res, res.next, tmp = tmp, res, tmp.next
            
        return res
                
        
        