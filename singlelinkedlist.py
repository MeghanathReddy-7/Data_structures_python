#deletion in single linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.next
    def del_at_begin(self):
        if self.head is None:
            print("can't delete")
        else:
            n=self.head
            self.head=n.next
            n=None
    def del_at_end(self):
        if self.head is None:
            print("can't delete")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
    def del_by_value(self,val):
        if self.head is None:
            print("can't delete")
        else:
          if val==self.head.data:
               self.head=None
          else:
            n=self.head
            while n.next is not None:
                if n.next.data==val:
                    break
                n=n.next
            if n.next is None:
                print("that value is not found in list")
            else:
                n.next=n.next.next
    def del_by_pos(self,pos):
      if pos==1:
          a.del_at_begin()
      else:
        if self.head is None:
            print("can't delete")
        else:
            n=self.head
            for i in range(1,pos-1):
                n=n.next
            p=n.next
            n.next=n.next.next
            p.next=None
    def add_at_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def add_at_end(self,data):
        new_node=node(data)
        n=self.head
        if self.head is None:
            self.head=new_node
        else:
            while n.next is not None:
                n=n.next
            n.next=new_node
    def add_at_pos(self,data,pos):
        new_node=node(data)
        n=self.head
        if pos==1:
            self.add_at_begin(data)
        else:
            for i in range(1,pos-1):
                n=n.next
            new_node.next=n.next
            n.next=new_node
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            p = current.next
            current.next = prev
            prev = current
            current = p
        self.head = prev
a=linkedlist()
def dynamic():
    b=int(input("\n1.ADD AT START\n2.ADD AT END\n3.ADD AT A POSITION\n4.DELETE AT START\n5.DELETE AT END\n6.DELETE AT POSITION\n7.DELETE BY VALUE\n8.DISPLAY\n9.REVERSE\n:"))
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
        a.del_at_begin()
    elif b==5:
        a.del_at_end()
    elif b==6:
        c=int(input("Enter postion to delete"))
        a.del_by_pos(c)
    elif b==7:
        c=int(input("enter data to"
                    ""
                    " delete"))
        a.del_by_value(c)
    elif b==8:
        a.print()
    elif b==9:
        a.reverse()
    else:
        print("no command found")
dynamic()
y=input("enter y to continue")
while y=='y' or y=='Y':
    dynamic()
    y = input("enter y to continue")

