class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def sum_nodes(l1, l2, carry):
    if l1 is None and l2 is None and carry is None:
        return None
    result = LinkedListNode()
    value = carry
    
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data
    
    result.data = value % 10
    
    if l1 is not None or l2 is not None:
        more = sum_nodes(l1.next if l1 is not None else None,
                         l2.next if not None else None,
                         1 if value >= 10 else 0 )
        result.next = more
    return result