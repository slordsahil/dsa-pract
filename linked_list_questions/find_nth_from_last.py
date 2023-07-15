#%%
class node():
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
    def from_last(n,head):
        node_list=[]
        while head:
            node_list.append(head)
            head=head.nextnode
            
        return node_list[-n]
            
# %%
#do
a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
# %%
target=node.from_last(2,a)
# %%
target.value
# %%
