from TreeNode import TreeNode
def build_tree_from_input():
    """Builds a tree based on the TreeNode class and text input """
    # Hard code first node -> start reading input from 2nd row
    root = TreeNode("/")
    current_node = root
    with open("complete_input.txt",'r', encoding='utf_8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            instruction = line.replace("$", "").strip().split()
            if instruction[0] == 'dir':
                create_node(current_node, instruction[1])
                continue
            # if numeric -> file to add
            if instruction[0].isnumeric():
                add_node_data(current_node,instruction[0], instruction[1])
                continue
            if instruction[0] != 'cd':
                continue
            if instruction[1] == '..':
                current_node = current_node.parent
                continue
            current_node = go_to_appropriate_node(current_node, instruction[1])
    return root

def add_node_data(current_node,size, file_name):
    current_node.data[file_name] = int(size)
    return

def create_node(current_node, name_of_new_node):
    """If not already created, create a node called name and"""
    for child in current_node.get_children():
        if child.name == name_of_new_node:
            return 0
    current_node.add_child(TreeNode(name_of_new_node))
    return 1

def go_to_appropriate_node(current_node, name_of_node):
    """Takes in the node you're currently at and the name of the node"""
    # You want to go to. Set it as current node if valid child
    child_nodes = current_node.get_children()
    for child in child_nodes:
        if child.name == name_of_node:
            current_node = child
            return current_node
    return 0

def main():
    # Part 2: find smallest directories to delete so free space >= 30000000
    dirs_big_enough = []
    dirs_and_their_size = {}
    # get current data size from size of root directory
    root = build_tree_from_input()
    current_data_amount = root.get_sum()
    free_space = 70000000 - current_data_amount
    clean_up_needed = 30000000 - free_space
    print(clean_up_needed)
    #print(f"\n currently storing: {current_data_amount} bytes")
    #print(f"\n Clean up needed: {clean_up_needed} bytes")
    # root.print_tree()
    # Sum for all nodes by summing for one node and 
    # add its child nodes to the stack
    stack = [root]
    while len(stack) >0:
        node = stack.pop()
        dirs_and_their_size[node.name] = node.get_sum
        #if node.get_sum() < 100000:
         #   tot += node.get_sum()
        if node.get_sum() >= clean_up_needed:
         dirs_big_enough.append(node.get_sum())
        for child in node.children:
            stack.append(child)
    print(min(dirs_big_enough))
    #print(dirs_big_enough)
if __name__ == "__main__":
    main()