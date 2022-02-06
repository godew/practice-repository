# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode()
        def DFS(root, inorder):
            root.val = preorder[0]
            preorder.pop(0)
            idx = inorder.index(root.val)
            
            if idx != 0:
                root.left = TreeNode()
                DFS(root.left, inorder[:idx])
            
            if not preorder:
                return
            
            if idx+1 != len(inorder):
                root.right = TreeNode()
                DFS(root.right, inorder[idx+1:])
            
        DFS(root, inorder)
        return root


        
