class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Result:
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def findIntersection(list1, list2):
    if list1 is None or list2 is None:
        return None
    
    result1 = getTailAndSize(list1)
    result2 = getTailAndSize(list2)
    
    if result1.tail != result2.tail:
        return None
    
    shorter = list1 if result1.size < result2.size else list2
    longer = list1 if result1.size > result2.size else list2
    
    longer = getKthNode(longer, abs(result1.size - result2))
    
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
        
    return longer

def getTailAndSize(lst):
    if lst is None: 
        return None
    
    size = 1
    current = lst
    while current.next is not None:
        size += 1
        current = current.next
    return Result(current, size)

def getKthNode(head, k):
    current = head
    while k > 0 and current is not None:
        current = current.next
        k -= 1
    return current
