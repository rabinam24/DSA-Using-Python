class Stack:
    def __init__(self,items=None):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)
        
        
mystack= Stack()

mystack.push(10)
mystack.push(20)
mystack.push(30)

print("Top element is ",mystack.peek())
print(f'Stack: {mystack.items}')
print("Removed element is ",mystack.pop())
print(f'Stack: {mystack.items}')