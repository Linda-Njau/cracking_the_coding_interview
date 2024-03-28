class StackWithMin(list):
    def push(self, value):
        new_min = min(value, self.min() if self else float('inf'))
        super().append(NodeWithMin(value, new_min))
    
    def min(self):
        if not self:
            return float('inf')
        else:
            return self[-1].min

class NodeWithMin:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

# Using Another Stack to keep track of min

class StackWithMin2:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <=self.min():
            self.min_stack.append(value)
    
    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min():
            self.min_stack.pop()
        return value
    
    def min(self):
        if not self.min_stack:
            return float('inf')
        return self.min_stack[-1]
