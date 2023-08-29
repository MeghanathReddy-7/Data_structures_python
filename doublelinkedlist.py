class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def add_at_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def add_at_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            new_node.prev=n
            n.next=new_node
    def add_at_pos(self,data,pos):
            if pos==1:
                self.add_at_begin(data)
            else:
                new_node=node(data)
                if self.head is None:
                    self.head=new_node
                else:
                    n=self.head
                    for i in range(1,pos-1):
                        n=n.next
                    new_node.next=n.next
                    new_node.prev=n
                    n.next=new_node
    def del_at_begin(self):
        if self.head is None:
            print("can't delete")
        else:
            n = self.head
            n.next.prev = None
            self.head = self.head.next
            n.next = None
    def del_at_end(self):
        if self.head is None:
            print("can't delete")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next.prev = None
            n.next = None
    def del_at_pos(self, pos):
        if self.head is None:
            print("can't delete")
        else:
            if pos == 1:
                self.del_at_begin()
            else:
                n = self.head
                for i in range(1, pos - 1):
                    n = n.next
                p = n.next
                n.next = n.next.next
                p.next.prev = n
                p.prev = None
                p.next = None
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.next
    def reverse(self):
            temp = self.head
            while (temp != None):
                a = temp.prev
                b = temp.next
                temp.prev = b
                temp.next = a
                temp = b
            self.head = a.prev
a=doublelinkedlist()
def dynamic():
    b=int(input("\n1.ADD AT START\n2.ADD AT END\n3.ADD AT A POSITION\n4.DISPLAY\n:5.REVERSE"))
    if b==1:
        c=int(input("Enter data:"))
        a.add_at_begin(c)
    elif b==2:
        c=int(input("Enter data:"))
        a.add_at_end(c)
    elif b==3:
        c=int(input("Enter data:"))
        d=int(input("Enter position:"))
        a.add_at_pos(c,d)
    elif b==4:
        a.print()
    elif b==5:
        a.reverse()
    else:
        print("no command found")
dynamic()
y=input("enter y to continue")
while y=='y' or y=='Y':
    dynamic()
    y = input("\nenter y to continue")
