class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        
    def add_Node(self, value , node = None):
        if not node:
            node = self.root
        if value < node.value:
            if node.left:
                self.add_Node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.add_Node(value, node.right)
            else:
                node.right = Node(value)
        
    def get_min(self):
        node = self.root
        while node.left:
            node = node.left
        return node.value
    
    def get_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value
    
    def contains(self, value, node=None):
        if not node:
            node = self.root
        if value == node.value:
            return True
        elif value < node.value:
            if node.left:
                return self.contains(value, node.left)
            else:
                return False
        else:
            if node.right:
                return self.contains(value, node.right)
            else:
                return False
            
    def print_in_order(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.print_in_order(node.left)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)

#### homework ####

def bst_decorator(func):
    def wrapper(list):
        result = BinarySearchTree(list[0])
        for i in list[1:]:
            result.add_Node(i)
        func(result)
    return wrapper

@bst_decorator
def print_bst(list):
    list.print_in_order()
    return

print_bst([5, 3, 7, 1, 2, 6, 8])


