# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = []
        def DFS(root):
            if not root:
                return
            if low <= root.val <= high:
                res.append(root.val)
            if low >= root.val:
                DFS(root.right)
                return
            if high <= root.val:
                DFS(root.left)
                return
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)
        return sum(res)
            