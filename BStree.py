class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class tree :
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if root==None:
            return node(data)
        elif root.data>data:
            root.left=self.insert(root.left,data)
        elif root.data<data:
             root.right=self.insert(root.right,data)
        return root
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
    def Inorder(self,root): 
        if root:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    
a=tree()
data=0
while(data!=-1):
    data=int(input("Enter data : "))
    a.root=a.insert(a.root,data)

print("In Preorder : ",end=" ")
a.preorder(a.root)
print()
print("In Postorder : ",end=" ")
a.postorder(a.root)
print()
print("In Inorder : ",end=" ")
a.Inorder(a.root)
