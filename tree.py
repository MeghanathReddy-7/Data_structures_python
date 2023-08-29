class Node:
 def __init__(self,data):
     self.data=data
     self.left=None
     self.right=None
class Tree:
 def __init__(self):
     self.root=None
 def create(self):
     data=int(input())
     if data==-1:
       return
     else:
         newnode=Node(data)
         print("Enter left child:")
         newnode.left=self.create()
         print("Enter right child:")
         newnode.right=self.create()
         return newnode
 def inorder(self,root):
     if root:
         self.inorder(root.left)
         print(root.data,end=" ")
         self.inorder(root.right)
 def preorder(self,root):
     if root:
         print(root.data,end=" ")
         self.preorder(root.left)
         self.preorder(root.right)
 def postorder(self,root):
     if root:
         self.postorder(root.left)
         self.postorder(root.right)
         print(root.data,end=" ")
obj=Tree()
print("Enter root: ")
obj.root=obj.create()
print("Inorder:")
obj.inorder(obj.root)
print()
print("PreOrder:")
obj.preorder(obj.root)
print()
print("PostOrder:")
obj.postorder(obj.root)
