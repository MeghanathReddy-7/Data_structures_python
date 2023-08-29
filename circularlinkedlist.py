class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class circular:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while 1:
                print(n.data,"-->",end="")
                if n.next is self.head:
                    break
                n=n.next
    def add_at_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
        else:
            new_node.next=self.head
            n=self.head
            while n.next is not self.head:
                n=n.next
            n.next=new_node
            self.head=new_node
    def add_at_end(self,data):
        new_node=node(data)
        n=self.head
        while n.next is not self.head:
            n=n.next
        new_node.next=self.head
        n.next=new_node
    def add_at_pos(self,data,pos):
        n=self.head
        new_node=node(data)
        for  i in range(1,pos-1):
            n=n.next
        new_node.next=n.next
        n.next=new_node
    def del_at_begin(self):
        n=self.head
        while n.next is not self.head:
            n=n.next
        n.next=self.head.next
        p=self.head
        self.head=self.head.next
        p.next=None
    def del_at_end(self):
        n=self.head
        while n.next.next is not self.head:
            n=n.next
        p=n.next
        p.next=None
        n.next=self.head
    def del_at_pos(self,pos):
        n=self.head
        for  i in range(1,pos-1):
            n=n.next
        p=n.next
        n.next=n.next.next
        p.next=None
a=circular()
a.add_at_begin(45)
a.add_at_begin(15)
a.add_at_begin(458)
a.add_at_begin(459)
a.add_at_end(592)
a.print()
a.add_at_pos(56,3)
print()
a.print()
a.del_at_begin()
print()
a.print()
a.del_at_end()
print()
a.print()
a.del_at_pos(2)
print()
a.print()