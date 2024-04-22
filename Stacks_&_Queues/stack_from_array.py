class FullStackException(Exception):
    pass

class EmptyStackException(Exception):
    pass

class FixedMultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
    
    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise FullStackException()
    
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value
         
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStackException()
        
        top = self.index_of_top(stack_num)
        value = self.values[top]
        self.values[top] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStackException()
        
        return self.values[self.index_of_top(stack_num)]
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity
    
    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size -1
