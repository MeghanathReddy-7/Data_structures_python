class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularqueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new_node=node(data)
        if self.front==None and self.rear==None:
            self.front=self.rear=new_node
            self.rear.next=self.front
        else:
            self.rear.next=new_node
            new_node.next=self.front
            self.rear=new_node
    def dequeue(self):
        if self.front and self.rear == None:
            print("empty")
        else:
            self.front=self.front.next
            self.rear.next=self.front
    def display(self):
        if self.front and self.rear == None:
            print("empty")
        else:
            n=self.front
            while(1):
               print(n.data,"-->",end="")
               if n.next==self.front:
                   break
               n=n.next
a=circularqueue()
a.enqueue(5)
a.enqueue(15)
a.enqueue(89)
a.display()
print()
a.dequeue()
a.display()
print()
