"""This class represents a node in a general tree"""
class TreeNode:
    """ A node has a name, children saved in lists and data (in a dictionary)"""
    def __init__(self,name):
        self.name = name
        self.data = {}
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Adds a child to the node"""
        child.parent = self
        self.children.append(child)

    def add_data(self, file_name, size):
        """Add a file to the directory(node)"""
        self.data[file_name] = size
    
    def get_children(self):
        return self.children

    def print_tree(self):
        print(f"Node {self.name} has data: {self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_sum(self):
        tot = 0
        for value in self.data.values():
            tot += value
        for child in self.children:
            tot += child.get_sum()
        return tot