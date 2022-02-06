import sys
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        a = res = ListNode()
        lists_tmp = lists[:]
        for i in range(len(lists)):
            if lists[i] is None:
                lists_tmp.remove(None)
        lists = lists_tmp
        
        while lists:
            MIN = sys.maxsize
                
            for i in range(len(lists)):
                if MIN > lists[i].val:
                    MIN = lists[i].val
                    idx = i
            a.next = lists[idx]
            a = a.next
            lists[idx] = lists[idx].next
            
            if lists[idx] is None:
                lists.pop(idx)
        
        return res.next