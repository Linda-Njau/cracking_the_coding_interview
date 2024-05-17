from enum import Enum

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

class State(Enum):
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"
    BLANK = "BLANK"

class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.state = State.BLANK
    
    def add_neighbors(self, node):
        if node not in self.children:
            self.children.append(node)
            
def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)
    for dependency in dependencies:
        first, second = dependency
        graph.add_edge(first, second)
        
def do_dfs(project, stack):
    if project.state == project.state.PARTIAL:
        return False
    
    if project.state == project.state.BLANK:
        project.state = project.state.PARTIAL
        for child in project.children:
            if not do_dfs(child, stack):
                return False
            project.state = project.state.COMPLETE
            stack.append(project)
    return True

def order_project(projects):
    stack = []
    for project in projects:
        if project.state == project.state.BLANK:
            if not do_dfs(project, stack):
                return None
    return stack[::-1]

def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_project(graph.nodes)
