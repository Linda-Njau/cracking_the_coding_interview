from collections import deque
from enum import Enum

class State(Enum):
    Unvisited = 0
    Visited = 1
    Visiting = 2
    
class Graph:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def get_nodes(self):
        return self.nodes
    
class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.state = State.Unvisited
    
    def add_adjacent(self, node):
        self.adjacent.append(node)
    
    def get_adjacent(self):
        return self.adjacent
    
def search(g, start, end):
    """represents BFS search"""
    if start == end:
        return True
    
    q = deque()
    
    for u in g.get_nodes():
        u.state = State.Unvisited
    
    start.state = State.Visiting
    q.append(start)
    
    while q:
        u = q.popleft()
        if u:
            for v in u.get_adjacent():
                if v.state == State.Unvisited:
                    if v == end:
                        return True
                    else:
                        v.state = State.Visiting
                        q.append(v)
            u.state = State.Visited
    return False