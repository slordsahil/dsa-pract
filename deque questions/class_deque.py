class deque(object):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items==[]
    
    def add_front(self,item):
        self.items.insert(0,item)
        
    def add_rear(self,item):
        self.items.insert(-1,item)
        
    def remove_front(self):
        self.items.remove(self.items[0])
        
    def remove_rear(self):
        self.items.pop()
        
    def size(self):
        return len(self.items)
        
# %%
