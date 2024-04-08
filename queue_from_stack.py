class MyQueue:
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack() 
        self.size = self.stackNewest.size + self.stackOldest.size
        
    def add(self, value):
        self.stackNewest.push(value)
    
    def shiftStacks(self):
        if self.stackOldest.isEmpty():
            while not self.stackNewest.isEmpty():
                self.stackOldest.push(self.stackNewest.pop())
    
    def peek(self):
        self.shiftStacks()
        return self.stackOldest.peek()
    
    def remove(self):
        self.shiftStacks()
        return self.stackOldest.pop()
    
    
        
    
