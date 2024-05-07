class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
        
    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]
    
    def push(self, v):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(v)
        else:
            stack = Stack(self.capacity)
            stack.push(v)
            self.stacks.append(stack)
    
    def pop(self):
        last = self.get_last_stack()
        if not last:
            raise EmptyStackException()
        v = last.pop()
        if last.size == 0:
            self.stacks.pop()
        return v
    
    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()
    
    def pop_at(self, index):
        return self.left_shift(index, True)
    
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        if remove_top:
            removed_item = stack.pop()
        else:
            removed_item = stack.remove_bottom()
            
        if stack.is_empty():
            self.stacks.pop(index)
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        return removed_item
class EmptyStackException(Exception):
    pass

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0
    
    def is_full(self):
        return self.size == capacity
    
    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below
    
    def push(self, value):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(value)
        if self.size == 1:
             self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True
    
    def pop(self):
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def is_empty(self):
        return self.size == 0
    
    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.szie -= 1
        return b.value
    
class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None
