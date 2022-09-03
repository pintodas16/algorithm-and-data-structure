import this


class Stack:
    def __init__(self) :
        self.top = -1
        self.items = []
        # self.size = 1000
        # self.items = [self.size]
    def push(self,item):
        self.top +=1
        self.items.append(item)
        # self.items[self.top] = item
        
    def pop(self):
        if not Stack.is_empty(self):
            x = self.items[self.top]
            del self.items[self.top]  # just delete the top value does not return anythong  and del is a keyword 
            self.top -=1 
            return x
            
        else:
            return "the stack is empty "
            
    def top_element(self):
       
        return self.items[self.top]
    def size(self):
        return self.top + 1
    def is_empty(self):
        if self.top != -1:
            return False
        return True
    
    def print(self):
        if not Stack.is_empty(self):
            print(self.items)
        else:
            print("stack is empty")


s = Stack()
print("push 2" ,end=" ")
s.push(2)
print("\npush 5",end=" ")
s.push(5)
print("\nprint the stack : ",end=" ")
s.print()
print("print the size of the stack : ",s.size())
print("pop an element of our stack : ",s.pop())

print('after pop our stack : ',end=" ")
s.print()
print("the top element : " ,s.top_element())
print("check our stack is empty or not !:", s.is_empty())
 