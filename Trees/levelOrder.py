from typing import Optional
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        
        while queue:
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levels)
        return result
