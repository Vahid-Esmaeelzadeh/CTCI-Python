'''
Largest Smaller BST Key
BST Infimum of a key in
'''



# A node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    # Largest Smaller BST Key
    def find_largest_smaller_key(self, num):
        prev_val = -1
        current_node = self.root

        while current_node:
            if num <= current_node.key:
                current_node = current_node.left
            else:
                prev_val = current_node.key
                current_node = current_node.right

        return prev_val

        # Given a binary search tree and a number, inserts a

    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while (currentNode is not None):
            if (key < currentNode.key):
                if (currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if (currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);

result = bst.find_largest_smaller_key(23)

print("Largest smaller number is %d " % (result))
