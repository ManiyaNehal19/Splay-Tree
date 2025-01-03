
class Node:
    def __init__(self, data):
        # Initialize a node with the provided data
        self.data = data
        self.parent = None  # Pointer to the parent node
        self.left = None    # Pointer to the left child node
        self.right = None   # Pointer to the right child node

class SplayTree:
    def __init__(self):
        # Initialize an empty Splay Tree with a root node
        self.root = None    # Pointer to the root node of the tree

    def maximum(self, x):
        # Find and return the maximum value node in the subtree rooted at node x
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, pivot_node):
        # Perform a left rotation around the provided pivot_node
        right_child = pivot_node.right    # Store the pivot node's right child
        pivot_node.right = right_child.left    # Move right child's left subtree to pivot_node's right subtree

        # Update parent pointers
        if right_child.left:
            right_child.left.parent = pivot_node
        right_child.parent = pivot_node.parent

        # Update root pointer if pivot_node is the root
        if not pivot_node.parent:
            self.root = right_child
        elif pivot_node == pivot_node.parent.left:
            pivot_node.parent.left = right_child
        else:
            pivot_node.parent.right = right_child

        # Attach pivot_node as left child of right_child
        right_child.left = pivot_node
        pivot_node.parent = right_child

    def right_rotate(self, pivot_node):
        # Perform a right rotation around the provided pivot_node
        left_child = pivot_node.left    # Store the pivot node's left child
        pivot_node.left = left_child.right    # Move left child's right subtree to pivot_node's left subtree

        # Update parent pointers
        if left_child.right:
            left_child.right.parent = pivot_node
        left_child.parent = pivot_node.parent

        # Update root pointer if pivot_node is the root
        if not pivot_node.parent:
            self.root = left_child
        elif pivot_node == pivot_node.parent.right:
            pivot_node.parent.right = left_child
        else:
            pivot_node.parent.left = left_child

        # Attach pivot_node as right child of left_child
        left_child.right = pivot_node
        pivot_node.parent = left_child

    def splay(self, n):
        # Splay the node n to the root of the tree using various rotation operations
        while n.parent != None:
            if n.parent == self.root:
                # Zig step: If n's parent is root, perform a single rotation
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:
                # Zig-zig or Zig-zag step: Perform double rotation based on relationship between n, its parent, and grandparent
                p = n.parent
                g = p.parent
                if n.parent.left == n and p.parent.left == p:
                    self.right_rotate(g)
                    self.right_rotate(p)
                elif n.parent.right == n and p.parent.right == p:
                    self.left_rotate(g)
                    self.left_rotate(p)
                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)
                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, n):
        # Insert a node into the Splay Tree
        if self.root is None:
            # If tree is empty, set the node as the root
            self.root = n
            return
        y = None
        temp = self.root
        while temp is not None:
            # Traverse the tree to find the appropriate position for insertion
            y = temp
            if n.data == temp.data:
                # If node with same data exists, splay it to the root and return
                self.splay(n)
                return
            elif n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        # Set parent pointer of the new node
        n.parent = y
        # Insert the node based on its value
        if n.data < y.data:
            y.left = n
        else:
            y.right = n
        # Splay the inserted node to the root
        self.splay(n)

    def search(self, n, x):
    # Search for a value x in the Splay Tree
        if n is None:
            # If the current node is None, the value x is not found in the tree
            return None
        if x == n.data:
            # If node with value x is found, splay it to the root and return it
            self.splay(n)
            return n
        elif x < n.data:
            # If value x is smaller, search in the left subtree
            return self.search(n.left, x)
        elif x > n.data:
            # If value x is larger, search in the right subtree
            return self.search(n.right, x)

    def delete(self, n):
    # Delete a node from the Splay Tree
        x = self.search(self.root, n.data)  # Search the node to be deleted to the root
        if x:
            # If the node is present in the tree
            # Create left and right subtrees
            left_subtree = SplayTree()
            left_subtree.root = self.root.left
            if left_subtree.root is not None:
                left_subtree.root.parent = None

            right_subtree = SplayTree()
            right_subtree.root = self.root.right
            if right_subtree.root is not None:
                right_subtree.root.parent = None

            if left_subtree.root is not None:
                # If left subtree is not empty
                m = left_subtree.maximum(left_subtree.root)  # Find maximum node in left subtree
                left_subtree.splay(m)  # Splay the maximum node to the root
                left_subtree.root.right = right_subtree.root  # Attach right subtree to the maximum node
                self.root = left_subtree.root  # Set the new root
            else:
                # If left subtree is empty, set right subtree as the new tree
                self.root = right_subtree.root


def preorder_traversal(node, result_list):
    # Perform a preorder traversal of the subtree rooted at node
    if node is not None:
        result_list.append(node.data)  # Add node's data to result list
        preorder_traversal(node.left, result_list)  # Recursively traverse left subtree
        preorder_traversal(node.right, result_list)  # Recursively traverse right subtree

def traversal_from_root(T):
    # Perform an inorder traversal of the entire tree starting from the root
    result_list = []
    if T.root is None:
        print("Tree is empty.")
    else:
        preorder_traversal(T.root, result_list)  # Start preorder traversal from root
    return result_list


t = SplayTree()
a = Node(12)
b = Node(13)
c = Node(6)
d = Node(2)
e = Node(11)
z = Node(15)

# Insert nodes into the tree
t.insert(a)
t.insert(b)
t.insert(c)
t.insert(d)
t.insert(e)
t.insert(a)
print("Traversal from root after insert:", traversal_from_root(t))
#Perform search operation
search_result = t.search(t.root, 6)

if search_result:
    print("Searched node found and splayed successfully:", search_result.data)
    print("Traversal from root after search:", traversal_from_root(t))
else:
    print("Searched node not found.")
t.delete(z)
t.delete(a)
print("Traversal from root after delete:", traversal_from_root(t))







