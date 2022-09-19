class Queue:
    def __init__(self,size): 
        self.items = [0]*size
        self.max_size = size
        self.head,self.tail,self.size = 0,0,0,
    
    def enqueue(self,item):
        if self.is_full():
            print("queue is full .")
            return 
        print("inserting an element",item)
        self.items[self.tail]=item
        self.tail = (self.tail +1)% self.max_size
        self.size +=1
    
    def dequeue(self):
        if self.is_empty():
            print("que is empty ")
            return 
        item = self.items[self.head]
        del self.items[self.head]
        self.head = (self.head +1) % self.max_size
        self.size -=1
        return item
        
    def is_full(self):
        if self.size == self.max_size:
            return True
        return False
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def print_queue(self):
        if not self.is_empty():
            print(self.items)
            return 
    def size(self):
        return self.size
    
    def queue_top(self):
        if  self.is_empty():
            print("queue is empty !")
        return self.items[self.head]

q = Queue(3)
q.enqueue('pinto')
q.enqueue('ratul')
q.enqueue('niloy')
q.enqueue("prince")
item = q.dequeue()
print(item)
q.print_queue()
print(q.head)
print(q.tail)
print(q.queue_top())
