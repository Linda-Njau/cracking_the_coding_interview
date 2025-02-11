from typing import Optional
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        
        while queue:
            levels = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(result) % 2 == 0:
                    levels.append(node.val)
                else:
                    levels.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(levels))
        return result
