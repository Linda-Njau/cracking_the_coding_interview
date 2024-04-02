class SetOfStacks:
    def __init__(self):
        self.stacks = []
    
    def push(self, v):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(v)
        else:
            stack = Stack(capacity)
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

class EmptyStackException(Exception):
    pass
    