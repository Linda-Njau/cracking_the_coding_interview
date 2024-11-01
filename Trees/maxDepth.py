from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftNode = self.maxDepth(root.left)
        rightNode = self.maxDepth(root.right)
        
        return 1 + max(leftNode, rightNode)
