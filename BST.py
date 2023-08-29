class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.data) + "->", end=' ')
        inorder(root.right)
def insert(root, data):
    if root is None:
        return BST(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def minValueNode(root):
    current = root
    while(current.left is not None):
        current = current.left   
    return current
def deleteNode(root, data):
    # Return if the tree is empty
    if root is None:
        return root
    # Find the node to be deleted
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif(data > root.data):
        root.right = deleteNode(root.right, data)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)
        root.data = temp.data
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 10")
root = deleteNode(root, 8)
print("Inorder traversal: ", end=' ')
inorder(root)
