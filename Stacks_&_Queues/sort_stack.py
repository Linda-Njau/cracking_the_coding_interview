def sort(s):
    """Time complexity O(N^2) space complexity O(N)"""
    r = Stack()
    
    while not s.isEmpty():
        tmp = s.pop()
        
        while not r.isEmpty() and r.peek() > tmp:
            s.push(r.pop())
        
        r.push(tmp)
        
    while not r.isEmpty():
        s.push(r.pop())
