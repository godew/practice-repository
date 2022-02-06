# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = 10001
    tmp = -10001
    def minDiffInBST(self, root: TreeNode) -> int:
        def DFS(root):
            if root.left:
                DFS(root.left)
            self.res = min(self.res, root.val - self.tmp)
            self.tmp = root.val
            if root.right:
                DFS(root.right)
        DFS(root)
        return self.res