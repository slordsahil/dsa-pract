#%%
class stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
        
    def peek(self):
        return self.items(len(self.items)-1)
    
    def Empty(self):
        self.items = []
        

s=stack()
s.push(13334)
s.push('sahil')
s.isEmpty()
s.pop()
s.isEmpty()
s.Empty()
s.isEmpty()
    
        
    

# %%
