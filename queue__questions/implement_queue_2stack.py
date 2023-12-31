class queue_2stack():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def enqueue(self,item):
        self.stack1.append(item)
        
    def dequeue(self):
        if self.stack2==[]:
            while self.stack1!=[]:
                self.stack2.append(self.stack1.pop())
        else:
            return self.stack2.pop()
        return self.stack2.pop()

q=queue_2stack()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print(q.dequeue())
