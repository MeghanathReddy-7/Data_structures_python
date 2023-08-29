class node:
    def __init__(self,data,priority):
        self.data=data
        self.next=None
        self.priority=priority
class priorityqueue:
    def __init__(self):
        self.front=None
    def enqueue(self,data,priority):
        new_node=node(data,priority)
        if self.front is None:
            self.front=new_node
        else:
            if self.front.priority >priority:
                new_node.next=self.front
                self.front=new_node
            else:
                n=self.front
                while(n):
                    if n.priority < priority:
                        break
                    n=n.next
                new_node.next = n.next
                n.next = new_node

    def display(self):
        n=self.front
        while n is not None:
            print(n.data,"-->",end="")
            n=n.next
a=priorityqueue()
a.enqueue(5,3)
a.enqueue(9,4)
a.enqueue(6,2)
a.enqueue(45,1)
a.enqueue(89,0)
a.display()



