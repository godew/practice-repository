import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append([root,1])
        while q:
            new = q.popleft()
            res = new[1]
            if new[0].left:
                q.append([new[0].left, new[1]+1])
            if new[0].right:
                q.append([new[0].right, new[1]+1])
                
        return res