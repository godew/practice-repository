class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next # 트랜잭션이 한번에 실행된다.
        return rev
        