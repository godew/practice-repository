# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def DFS(root1, root2):
            if root1 and root2:
                root1.val += root2.val
            elif not root1 and root2:
                return root2
            elif root1 and not root2:
                return root1
            else:
                return
            root1.left = DFS(root1.left, root2.left)
            root1.right = DFS(root1.right, root2.right)
            return root1
            
        return DFS(root1, root2)
        
        