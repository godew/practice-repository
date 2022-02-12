# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def DFS(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            elif root.left and not root.right:
                l = DFS(root.left)
                if root.left.val == root.val:
                    self.res = max(self.res, l+1)
                    return l+1 
                else:
                    return 0
            elif not root.left and root.right:
                r = DFS(root.right)
                if root.right.val == root.val:
                    self.res = max(self.res, r+1)
                    return r+1
                else:
                    return 0
            else:
                l = DFS(root.left)
                r = DFS(root.right)
                if root.left.val == root.val and root.right.val == root.val:
                    self.res = max(self.res, l+r+2)
                    return max(l, r)+1 
                elif root.left.val == root.val and root.right.val != root.val:
                    self.res = max(self.res, l+1)
                    return l+1
                elif root.left.val != root.val and root.right.val == root.val:
                    self.res = max(self.res, r+1)
                    return r+1
                else:
                    return 0
        DFS(root)
        return self.res
            