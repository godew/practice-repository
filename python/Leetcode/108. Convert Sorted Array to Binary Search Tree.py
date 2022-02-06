from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        bst = TreeNode(nums[len(nums) // 2])    
        bst.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        bst.right = self.sortedArrayToBST(nums[(len(nums) // 2)+1:])
        
        return bst
        
        
