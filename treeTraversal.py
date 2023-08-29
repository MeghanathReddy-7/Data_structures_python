class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class tree :
    def __init__(self):
        self.root=None
    def insert(self):
        data=int(input())
        if data==-1:
            return
        xtra=node(data)
        print("Enter left child : ",end="")
        xtra.left=self.insert()
        print("Enter right child : ",end="")
        xtra.right=self.insert()
        return xtra
    def preorder(self,root): 
        if root!=None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root): 
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def Inorder(self,root): 
        if root!=None:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    
a=tree()
print("Enter root : ",end="")
a.root=a.insert()
print("In Preorder : ",end="")
a.preorder(a.root)
print()
print("In Postorder : ",end="")
a.postorder(a.root)
print()
print("In Inorder : ",end="")
a.Inorder(a.root)
