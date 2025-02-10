class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def rec(root):
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            self.sum = max(self.sum, root.val + left + right)
            return root.val + max(left, right)
        rec(root)
        return self.sum
