#Define a class node to describe an node of a circular linked list.

class Node:
    def __init__(self,item=None,next=None):
        self.item= item
        self.next= next

#Define a class CLL to implement Circulated Linked List with __init__() method to create and initialise last reference variable. 
class CLL:
    def __init__(self,last=None):
        self.last=last

#Define a method is_empty() to check if the linked list is empty in CLL class. 
    def is_empty(self):
        return self.last is None
    
#In class CLL, Define a method insert_at_start() to insert an element at the starting of the list

    def insert_at_start(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node  # Pointing itself for a circular list
            self.last= new_node
        else:
            new_node.next= self.last.next
            self.last.next=new_node
            
# insert_at_last
    def insert_at_last(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node
            
#search function      
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp != self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
   
#insert_after
    def insert_after(self,temp,data):
        if temp is not None:
            new_node= Node(data,temp.next)
            temp.next= new_node
            if temp== self.last:
                self.last=new_node
                
#Print all
    def print_list(self):
        if not self.is_empty():
            temp= self.last.next
            while temp != self.last:
                print(temp.item, end=" ")     
                temp=temp.next 
            print(temp.item)

#deletefirst

    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last= None
            else:
                self.last.next=self.last.next.next
                   
#DelelteLAST
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last= None
            else:
                temp= self.last.next
                while temp.next !=self.last:
                    temp=temp.next
                temp.next =self.last.next
                self.last=temp
               
#Deleteitem
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next
                    while temp != self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
                    
    def __iter__(self):
        if self.last== None:
            return CLLIterator(None)
        else: 
            return CLLIterator(self.last.next)
#Iterable

class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
      
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
            
        data=self.current.item
        self.current=self.current.next
        return data

cll=CLL()
cll.insert_at_start(10)
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.insert_after(cll.search(10),50)     

for x in cll:
    print(x, end=" ")
print()   

cll.print_list()
            
                
            
            
            
            
        
        
        
           