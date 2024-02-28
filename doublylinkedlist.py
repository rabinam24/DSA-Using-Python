#Define a class Node to describe a node of a doubly linked list.
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev= prev
        self.item= item
        self.next= next

#Define a class DLL to implement Doubly Linked List with __init__() method to create and initialise start reference variable  
class DLL:
    def __init__(self,start=None):
        self.start=start

#Define a method is_empty() to check if the linked list is empty in DLL class.

    def is_empty(self):
        return self.start is None
    
#In class DLL, define a method insert_at_start() to insert an element at the starting position of the list.
    def insert_at_start(self,data):
        new_node=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=new_node
        self.start= new_node
        
#In class DLL, define a method insert_at_last() to an element at the end position of the list       
    def insert_at_last(self,data):
        temp=self.start
        if self.start!= None:
          while temp.next is not None:
            temp= temp.next
        new_node=Node(temp,data,None)
        if temp==None:
            self.start= new_node
        else:
            temp.next= new_node
        
# In class DLL, define a method search() to find the node with specified element value.
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

# If not found while traversing forward, try traversing backward
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.prev

        return None

#In class DLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=new_node
            temp.next=new_node
            
#In class DLL, define method to print all the elements of the list    
    def print_list(self):
        temp= self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp= temp.next
            
#In class DLL, delete first item
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
                
#Define delete_last()
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start= None
        else:
            temp= self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next= None

#delete item
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                    if temp.item==data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev is not None:
                            temp.prev.next=temp.next
                        else:
                            self.start=temp.next
                        break
                    temp= temp.next
                
#iterator

    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self,start):
        self.current=start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data= self.current.item
        self.current= self.current.next
        return data
    

Doubly_linked_list=DLL()
Doubly_linked_list.insert_at_start(23)
Doubly_linked_list.insert_at_last(35)
Doubly_linked_list.insert_after(Doubly_linked_list.search(23),67)
Doubly_linked_list.print_list()
print()

for x in Doubly_linked_list:
    print(x, end=' ')
print()

        