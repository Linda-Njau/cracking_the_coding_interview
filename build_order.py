from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = []
        
    def get_or_create_node(self, name):
        node = next((n for n in self.nodes if n.name == name), None)
        if not node:
            node = Project(name)
            self.nodes.append(node)
        return node
    
    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)

class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dependencies = 0
    
    def add_neighbor(self, node):
        if node not in self.children:
            self.children.append(node)
            node.increment_dependencies()
    
    def increment_dependencies(self):
        self.dependencies += 1
    
    def decrement_dependencies(self):
        self.dependencies -= 1

def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.nodes)

def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)
    
    for depenency in dependencies:
        first, second = depenency
        graph.add_edge(first, second)
    
    return graph

def order_projects(projects):
    order = []
    end_of_list = add_non_dependent(order, projects, 0)
    to_be_processed = 0
    
    while to_be_processed < len(order):
        current = order[to_be_processed]
        
        if current is None:
            return None
        
        children = current.children
        for child in children:
            child.decrement_dependencies()
            
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
        
    return order

def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.dependencies == 0:
            order[offset] = project
            offset += 1
    return offset
        