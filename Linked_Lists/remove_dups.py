 
def remove_dups_set(n ):
    """Space complexity O(n); time complexity O(n)"""
    seen = set()
    prev = None
    
    while n:
        if n.data in seen:
            prev.next = n.next
        else:
            seen.add(n.data)
            prev = n
        n = n.next
        
def remove_dups(head):
    """space complexity O(1); time complexity O(N^2)"""
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
