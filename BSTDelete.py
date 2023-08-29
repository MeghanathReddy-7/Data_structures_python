#DELETIONS IN BST
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if root==None:
            return node(data)
        else:
            if root.data==data:
                return root
            elif root.data<data:
                root.right=self.insert(root.right,data)
            else:
                root.left=self.insert(root.left,data)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def search(self,root,key):
        if root is None:
            return None
        if root.data==key:
            return root
        elif root.data>key:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    def inOrderSuccessor(self,root):
        current=root
        while current.left is not None:
            current=current.left
        return current
    def delete(self,root,key):
        if root ==None:
            return root
        if root.data<key:
            root.right=self.delete(root.right,key)
        elif root.data>key:
            root.left=self.delete(root.left,key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            else:
                temp=self.inOrderSuccessor(root.right)
                root.data=temp.data
                root.right=self.delete(root.right,temp.data)
        return root

a=tree()
a.root=a.insert(a.root,5)
a.root=a.insert(a.root,3)
a.root=a.insert(a.root,50)
a.root=a.insert(a.root,4)
a.inorder(a.root)
print()
a.root=a.delete(a.root,5)
a.inorder(a.root)