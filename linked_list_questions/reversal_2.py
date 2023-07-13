#%%
class node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
    def reversal(head):
        current =head
        previous="none"
        
        
        while head:
            nextnode=current
            current.nextnode=previous
            current=current.nextnode
            previous=nextnode
        return previous


            
            
# %%
a=node(1)
b=node(2)
c=node(3)
d=node(4) 
a.nextnode=b
b.nextnode=c
c.nextnode=d
# %%
node.reversal(a)
# %%
