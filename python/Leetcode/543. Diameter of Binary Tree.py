# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def DFS(self, root):
            if not(root.left or root.right):
                return 0
            if root.left and root.right:
                l = self.DFS(root.left)
                r = self.DFS(root.right)
                self.res = max(self.res, l+r+2)
                return max(l, r) + 1
            if root.left:
                l = self.DFS(root.left)
                self.res = max(self.res, l+1)
                return l+1
            else:
                r = self.DFS(root.right)
                self.res = max(self.res, r+1)
                return r+1
            
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.DFS(root)
        return self.res
            