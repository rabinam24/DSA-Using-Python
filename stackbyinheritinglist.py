class Stack(list):
    # def __init__(self,items=None):
    #     self.items=[]
        
    def is_empty(self):
        return len(self) ==0
    
    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise IndexError("Stack is empty")
    
    
    