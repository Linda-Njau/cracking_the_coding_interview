from collections import deque

class Animal:
    def __init__(self, n):
        self.order = 0
        self.name = n
    
    def set_order(self, order):
        self.order = order
    
    def get_order(self):
        return self.order
    
    def is_older_than(self, a):
        return self.order < a.get_order()
    
    
class AnimalQueue:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0
        
    def enqueue(self, a):
        a.set_order(self.order)
        self.order += 1
        
        if isinstance(a, Dog):
            self.dogs.append(a)
        elif isinstance(a, Cat):
            self.cats.append(a)
        
    def dequeue_any(self):
        if len(self.dogs) == 0:
            return self.dequeue_cats()
        elif len(self.cats) == 0:
            return self.dequeue_cats()
        
        dog = self.dogs[0]
        cat = self.cats[0]
        
        if dog.is_older_than_cat(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()
        
    def dequeue_dogs(self):
        return self.dogs.popleft()
    
    def dequeue_cats(self):
        return self.cats.popleft()
    
class Dog(Animal):
    def __init__(self, n):
        super().__init__(n)
        
class Cat(Animal):
    def __init__(self, n):
        super().__init__(n)