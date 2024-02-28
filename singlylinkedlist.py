#Define a class node to describe an node of a singly linked list.
class Node:
    def __init__(self,item=None,next=None):
        self.item= item
        self.next= next
        
#Define a class SLL to implement Singly Linked List with __init__() method to create and initialise start reference variable. 
class SLL:        
    def __init__(self,start=None):
        self.start= start
        
#Define a method is_empty() to check if the linked list is empty in SLL class. 
    def is_empty(self):
        return self.start == None

#In class SLL, Define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self,data):      #yesma suruma function banaim
        new_node= Node(data,self.start)  #First ma naya node banaim, new_node bhanera ani tesma hamiley item ko value data bhanera pass garim, ani aruu node saga connect garauna self.start garim 
        self.start = new_node            #Abaa aaru node saga ta connect bhaisako tara naya node lai start saga connect garauney kaam chai yo node ley gareko chhaa

#In class SLL, Define a method insert_at_last() to insert an element at the end of the list
    def insert_at_last(self,data):
        new_node= Node(data,None)
        if not self.is_empty():           #yesma herim ki list empty ta xaina nii
            temp=self.start               #yespaxi, start ley point gareko value lai temp ley ni point garim 
            while temp.next is not None:  #temp ley none value nabhetun jel ko lagi while loop chalairakim
                temp= temp.next
            temp.next= new_node        # temp ley none bhetepaxi, temp.next ko value lai last_node lai point garna lagaim
        else:
            self.start= new_node
    
#In class SLL, define a method search() to find the node with specified element values.
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item== data:
                return temp
            temp=temp.next
        return None
        
#In class SLL, define a method insert_after() ro insert a new node after a given node of the list.
    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(data,temp.next)
            temp.next=new_node
            
#In class SLL, define a method  to print all the elements of the list.           
    def print_list(self):
        temp= self.start
        while temp is not None:
            print(temp.item, end=" ")     
            temp=temp.next 

#In class SLL, define a method delete_first() to delete first element from the list.        
    def delete_first(self):
        if self.start is not None:
            self.start= self.start.next
    
#In class SLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start= None
        else:
            temp= self.start
            while temp.next.next is not None:
                temp= temp.next
            temp.next= None
            
#In class SLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item== data:
                self.start= None
        else:
            temp=self.start
            if temp.item==data:
                self.start= temp.next
            else:   
                while temp.next is not None:
                    if temp.next.item== data:
                        temp.next= temp.next.next
                        break
                    temp=temp.next
                    
    def __iter__(self):
        return SLLIterator(self.start)
    
                    
#In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
class SLLIterator:
    def __init__(self,start):
        self.current= start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
        
               
singly_linked_list= SLL()
singly_linked_list.insert_at_start(23)
singly_linked_list.insert_at_start(10)
singly_linked_list.insert_at_last(66)
singly_linked_list.insert_after(singly_linked_list.search(10),45)
singly_linked_list.print_list()

singly_linked_list.delete_item(23)
print()
singly_linked_list.print_list()
print()

for x in singly_linked_list:
    print(x, end=" ")
    
print()
    
        