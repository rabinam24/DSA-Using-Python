class Node():
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class DLL():
    def __init__(self,start):
        self.start=start
        
    def is_empty(self):
        return self.start is None

    def insert_at_first(self,data):
        new_node=Node(data,None,self.start)
        if not self.is_empty():
            self.start.prev=new_node
        self.start=new_node
        
    def insert_at_last(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
        new_node=Node(data,temp,None)
        if temp== None:
            self.start= new_node
        else:
            temp.next=None  
        
        
        
        
        