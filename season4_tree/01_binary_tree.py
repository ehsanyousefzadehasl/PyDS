# Our nodes are from this Node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Our Binary Tree
class BinaryTree(object):
    # Our tree is going to be created with a node that is its root
    def __init__(self, root):
        self.root = Node(root)

    # This function searches for the key in our tree 
    def search(self, key):
        return self.preorder_search(tree.root, key)

    # This function prints all of the elements of the tree in pre-order DFS
    def print_tree(self):
        # We don't want to see the last dash and the [:-1] is for that :D
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, key):
        if start:
            if start.value == key:
                return True
            else:
                return self.preorder_search(start.left, key) or self.preorder_search(start.right, key)
        return False

    def preorder_print(self, start, traversal):
        if start:
            # preorder => check off as we visit the node
            traversal += (str(start.value) + "-")
            # first we visit left child then right child
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))

# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())