class Node:
    def __init___(self, data):
        self.data = data
        self.next = None

def NthToLast(head, k):
    """Time & Space Complexity O(n)"""
    def nth_to_last(node, k, i):
        if node is None:
            return None, i
        nd, i = nth_to_last(node.next, k, i)
        i += 1
        if i == k:
            return node, i
        return nd, i
    return nth_to_last(head, k, 0)[0]

def NthToLastIterative(headnode, k):
    """Time complexity is O(n) & space complexity is O(1)"""
    p1 = headnode
    p2 = headnode
    
    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next
    
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
        
    return p2
