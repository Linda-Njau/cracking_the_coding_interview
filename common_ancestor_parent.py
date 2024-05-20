class TreeNode:
    def __init__(self, parent=None):
        self.parent = parent

def common_ancestor(p: TreeNode, q: TreeNode) -> TreeNode:
    """O(d) where d is the depth of the deeper node"""
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = go_up_by(second, abs(delta))

    while first != second and first is not None and second is not None:
        first = first.parent
        second = second.parent
    
    return None if first is None or second is None else first

def go_up_by(node: TreeNode, delta: int) -> TreeNode:
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


def depth(node: TreeNode) -> int:
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth
